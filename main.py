from datetime import datetime

from bs4 import BeautifulSoup
from discord.ext import tasks, commands
import requests
import discord


intents = discord.Intents(messages=True, message_content=True)
bot = commands.Bot(command_prefix=">", intents=intents)

BOT_TOKEN = ""

prev_results = {}
started_tasks = {}


@bot.event
async def on_ready() -> None:
    current_time = datetime.now().strftime("%H:%M")
    print(f"[{current_time}] Bot en ligne.")


@bot.command(name="start")
async def start(ctx: commands.context.Context, arg: str = None) -> None:
    if ctx.author.id in started_tasks:
        embed = discord.Embed(title="Recherche déjà en cours.", color=0xc20000)
        await ctx.channel.send(embed=embed)
        return

    if arg is None:
        embed = discord.Embed(title="Aucune URL entrée.", color=0xc20000)
        await ctx.channel.send(embed=embed)
        return

    task = tasks.loop(minutes=1)(scrap)
    task.start(ctx, arg)
    started_tasks[ctx.author.id] = task
    prev_results[ctx.author.id] = set()

    current_time = datetime.now().strftime("%H:%M")
    print(f"[{current_time}] Recherche commencée.")
    embed = discord.Embed(title="Recherche commencée.", color=0x0f8000)
    await ctx.channel.send(embed=embed)


@bot.command(name="stop")
async def stop(ctx: commands.context.Context) -> None:
    if ctx.author.id not in started_tasks:
        embed = discord.Embed(title="Aucune recherche en cours.", color=0xc20000)
        await ctx.channel.send(embed=embed)
        return

    started_tasks[ctx.author.id].cancel()
    del started_tasks[ctx.author.id]
    del prev_results[ctx.author.id]

    current_time = datetime.now().strftime("%H:%M")
    print(f"[{current_time}] Recherche arrêtée.")
    embed = discord.Embed(title="Recherche arrêtée.", color=0xc20000)
    await ctx.channel.send(embed=embed)


async def scrap(ctx: commands.context.Context, url: str) -> None:
    current_time = datetime.now().strftime("%H:%M")

    response = requests.get(url)

    if response.status_code != 200:
        print(f"[{current_time}] Erreur lors du téléchargement de la page.")
        embed = discord.Embed(title="Erreur lors du téléchargement de la page.", color=0xc20000)
        await ctx.author.send(embed=embed)
        return

    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")
    elements = soup.find_all("li", class_="fr-col-12 fr-col-sm-6 fr-col-md-4 svelte-11sc5my fr-col-lg-4")
    names = {element.find("a").text for element in elements}

    if len(names) == 0:
        print(f"[{current_time}] Aucun logement trouvé.")
        prev_results[ctx.author.id] = names
        return

    names = names - prev_results[ctx.author.id]

    if len(names) == 0:
        print(f"[{current_time}] Aucun nouveau logement trouvé.")
        return

    prev_results[ctx.author.id] = names

    print(f"[{current_time}] Logement.s trouvé.s ({len(names)}):")
    print("-" + "\n-".join(names))
    embed = discord.Embed(title=f"Logement.s trouvé.s ({len(names)}):",
                          description="-" + "\n-".join(names),
                          color=0x0f8000)
    await ctx.author.send(embed=embed)


bot.run(BOT_TOKEN)

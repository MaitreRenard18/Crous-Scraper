from datetime import datetime

from bs4 import BeautifulSoup
from discord.ext import tasks, commands
import requests
import discord


intents = discord.Intents(messages=True, message_content=True)
bot = commands.Bot(command_prefix=">", intents=intents)

BOT_TOKEN = ""

bot.prev_result = []


@bot.event
async def on_ready() -> None:
    print("Bot is now online.")


@bot.command(name="start")
async def start(ctx: commands.context.Context, arg: str = None) -> None:
    if arg is None:
        embed = discord.Embed(title="Aucune URL entrée.", color=0xc20000)
        await ctx.channel.send(embed=embed)
    else:
        embed = discord.Embed(title="Recherche commencée.", color=0x0f8000)
        await ctx.channel.send(embed=embed)
        scrap.start(ctx, arg)


@bot.command(name="stop")
async def stop(ctx: commands.context.Context) -> None:
    embed = discord.Embed(title="Recherche arrêtée.", color=0xc20000)
    await ctx.channel.send(embed=embed)
    scrap.cancel()


@tasks.loop(seconds=10)
async def scrap(ctx: commands.context.Context, url: str) -> None:
    current_time = datetime.now().strftime("%H:%M")

    names = []
    for page in range(5):
        response = requests.get(f"{url}?page={page}")

        if response.status_code != 200:
            embed = discord.Embed(title="Erreur lors du téléchargement de la page", color=0xc20000)
            await ctx.author.send(embed=embed)
            scrap.cancel()
            return

        html_content = response.text
        soup = BeautifulSoup(html_content, "html.parser")
        elements = soup.find_all("li", class_="fr-col-12 fr-col-sm-6 fr-col-md-4 svelte-11sc5my fr-col-lg-4")
        names += sorted([element.find("a").text for element in elements])

    names = list(set(names) - set(bot.prev_result))

    if len(names) == 0:
        print(f"[{current_time}] Aucun logement trouvé.")
        return

    bot.prev_result = names

    print(f"[{current_time}] Logements trouvés ({len(names)}):")
    print("-" + "\n-".join(names))

    embed = discord.Embed(title=f"Logement.s trouvé.s ({len(names)}):",
                          description="-" + "\n-".join(names),
                          color=0x0f8000)
    await ctx.author.send(embed=embed)


bot.run(BOT_TOKEN)

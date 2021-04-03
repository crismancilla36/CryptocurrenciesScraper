from settings import *
import discord
from discord.ext import commands
from urllib import request
from bs4 import BeautifulSoup

bot = commands.Bot(command_prefix = PREFIX, description = 'Este es un bot scraper')
bot.remove_command('help')

@bot.command()
async def prefix(ctx, prefix):
    bot.command_prefix=prefix
    await ctx.send("El prefijo ha sido actualizado")

@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title = "Lector de precios de criptomonedas",
        description = f"""Este bot permite consultar el información de las criptomonedas.\n
                        **{bot.command_prefix}prefix [PREFIX]**: Ajusta el prefijo para llamar un comando.
                        **{bot.command_prefix}help**: Permite consultar los comandos disponibles.
                        **{bot.command_prefix}price [CRIPTOMONEDA]**: Muestra información actual de la moneda.
                        **{bot.command_prefix}history [CRIPTOMONEDA]**: Muestra historial de la moneda.


                        Todos estos datos son tomados de [CoinMarketCap](https://coinmarketcap.com)
                """)
    embed.set_thumbnail(url = "https://s2.coinmarketcap.com/static/img/coins/64x64/1.png")
    await ctx.send(embed=embed)

@bot.command()
async def price(ctx, *args):
    await ctx.send("Buscando...")
    cripto = "-".join(args)
    url = "https://coinmarketcap.com/currencies/"+cripto
    try:
        with request.urlopen(url) as response:
            if response.getcode() == 200:
                soup = BeautifulSoup(response.read(), 'html.parser')
    except Exception:
        await ctx.send("Ha ocurrido algún error :cry:, revisa el nombre de la criptomoneda")
    coin = soup.find(class_="sc-fzqBZW")
    embed = discord.Embed(title=f"{coin.contents[0]} {coin.contents[1].get_text()}", url=url)
    price_tag = soup.find(class_="priceTitle___1cXUG")
    embed.add_field(name="Price", value=price_tag.div.get_text())
    embed.add_field(name="Change 24h", value=price_tag.span.get_text())
    embed.set_thumbnail(url=soup.find("img")['src'])
    await ctx.send(embed=embed)

bot.run(TOKEN)

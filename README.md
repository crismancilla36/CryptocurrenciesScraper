# CriptocurrenciesBot

Este es un bot scraper que permite obtener distintos datos de distintas criptomonedas desde el chat de discord, tomando datos de la página [CoinMarketCap](https://coinmarket.com).


## Comandos
**!prefix [PREFIX]** Actualiza el nuevo prefijo para hacer uso de los comandos.

**!help** Muestra información general del bot.

**!price [Criptomoneda]:** Muestra el precio actual de Criptomoneda.


## Instrucciones para desarrollador
Si desea hacer uso del código puede tiene que crear un docuemnto settings.py con una estructura similar a settings.example.py.

Este repositorio hace uso de las librerías [discord.py](https://discordpy.readthedocs.io/en/latest/), [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) y [Matplotlib](https://matplotlib.org/), los cuales no están incluidos en la librería estandar de python, necesitará instalarlo.

Si usted tiene instalado [pipenv](https://pipenv.pypa.io/en/latest/) puede crear un entorno virtual y ejecutar los siguientes comandos:

```
pipenv shell
pipenv install
```
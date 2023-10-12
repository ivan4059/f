import discord

import random

 

intents = discord.Intents.default()

intents.typing = False

intents.presences = False

 

client = discord.Client(intents=intents)

 

@client.event

async def on_ready():

    print(f'Connesso come {client.user.name}')

 

@client.event

async def on_message(message):

    if message.author == client.user:

        return

 

    if message.content.startswith('/testa_o_croce'):

        risultato = random.choice(['Testa', 'Croce'])

        await message.channel.send(f'Hai lanciato una moneta e è uscito: {risultato}')

 

# Inserisci il tuo token del bot Discord qui

TOKEN ='MTE1NzYxOTY4NDkyMTg1MjAxNQ.G_tw-Q.JipNFgCMJahNF6qA7RKFWjcSOCRAzzObxyOlK4'

client.run(TOKEN) 

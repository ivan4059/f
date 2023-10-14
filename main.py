import discord
import random

# Assicurati che gli intents siano definiti
intents = discord.Intents.default()
intents.messages = True

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

    elif message.content.startswith('/sasso_carta_forbici'):
        user_choice = message.content[len('/sasso_carta_forbici'):].strip()
        choices = ['sasso', 'carta', 'forbici']
        if user_choice not in choices:
            await message.channel.send("Per favore scegli sasso, carta o forbici.")
            return
        
        bot_choice = random.choice(choices)
        await message.channel.send(f'Ho scelto: {bot_choice}')
        
        if user_choice == bot_choice:
            await message.channel.send('Pareggio!')
        elif (user_choice == 'sasso' and bot_choice == 'forbici') or \
             (user_choice == 'carta' and bot_choice == 'sasso') or \
             (user_choice == 'forbici' and bot_choice == 'carta'):
            await message.channel.send('Hai vinto!')
        else:
            await message.channel.send('Ho vinto io!')

    elif message.content.startswith('/battuta'):
        battute = [
            "Perché i libri di matematica sono sempre tristi? Perché hanno troppe radici quadre.",
            "Perché il semaforo non gioca mai a nascondino? Perché si nasconde sempre male!",
            "Perché gli scuba divers si immergono sempre all’indietro e mai in avanti? Perché altrimenti ancora si bagnano!"
        ]
        await message.channel.send(random.choice(battute))

# Inserisci il tuo token del bot Discord qui
TOKEN = 'import discord'
import random

# Assicurati che gli intents siano definiti
intents = discord.Intents.default()
intents.messages = True

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

    elif message.content.startswith('/sasso_carta_forbici'):
        user_choice = message.content[len('/sasso_carta_forbici'):].strip()
        choices = ['sasso', 'carta', 'forbici']
        if user_choice not in choices:
            await message.channel.send("Per favore scegli sasso, carta o forbici.")
            return
        
        bot_choice = random.choice(choices)
        await message.channel.send(f'Ho scelto: {bot_choice}')
        
        if user_choice == bot_choice:
            await message.channel.send('Pareggio!')
        elif (user_choice == 'sasso' and bot_choice == 'forbici') or \
             (user_choice == 'carta' and bot_choice == 'sasso') or \
             (user_choice == 'forbici' and bot_choice == 'carta'):
            await message.channel.send('Hai vinto!')
        else:
            await message.channel.send('Ho vinto io!')

    elif message.content.startswith('/battuta'):
        battute = [
            "Perché i libri di matematica sono sempre tristi? Perché hanno troppe radici quadre.",
            "Perché il semaforo non gioca mai a nascondino? Perché si nasconde sempre male!",
            "Perché gli scuba divers si immergono sempre all’indietro e mai in avanti? Perché altrimenti ancora si bagnano!"
        ]
        await message.channel.send(random.choice(battute))

# Inserisci il tuo token del bot Discord qui
TOKEN = 'miotoken'
client.run(TOKEN)

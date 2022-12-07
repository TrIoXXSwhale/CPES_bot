import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.members = True

bot = commands.Bot(intents = intents, command_prefix = "!")

@bot.event
async def on_ready():
    print("Le bot est prêt.")

@bot.command()
async def bienvenue(ctx):
    server = ctx.guild
    serverDescription = server.description
    numberOfTextChannels = len(server.text_channels)
    numberOfPerson = server.member_count
    serverName = server.name
    message = f"> **Bienvenue sur le serveur {serverName} !**\n\n > **Il est composé de {numberOfPerson} personnes (CPES1,CPES2,ESIEE_Student,ENSG_Student,ect...)  !** \n\n > **Ce serveur possède {numberOfTextChannels} salons écrits où tu peux poser des questions sur tes cours, travailler, ou juste discuter...**"
    await ctx.send('\n' + message)

@bot.command()
async def say(ctx,*File):
    await ctx.send(" ".join(File))

bot.run("MTA0OTM2NDE5OTc0MDAyNjkxMA.G5QQ-4.uUxEVumY11FhAwGy5DIc373LY5Qd-uZvGnHMuk")


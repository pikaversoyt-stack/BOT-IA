import discord
from discord.ext import commands
from modelo import detector
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(
                detector(image_path=f"./{attachment.filename}",model_path = "./keras_modelo.h5", labels_path = "labels.txt")
            )
    else:
        await ctx.send("Olvidaste subir la imagen")
bot.run("MTUwNDI2NzE2Mjc0MTkwMzM4MA.GBrB_b.o-HcZ9jDTKLjRzK9Yx   JhgqK5eDlWtGZAgoa4o8I")
import discord
import os
from typing import List, Dict
from emoji import emojize
from discord import app_commands
from itertools import chain
from uuid import UUID, uuid4
from moderate import filterMessage

intents = discord.Intents(messages=True, message_content=True)
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
toggle = False

filterDict = {}

def run_discord_bot():
	# Change your token here
	TOKEN = os.getenv("DISCORD_TOKEN")

	@client.event
	async def on_ready():
		await tree.sync(guild=discord.Object(id=1077598123892945067))
		await tree.sync()
		print(f'{client.user} is now running!')

	@client.event
	async def on_message(message: discord.Message):
		try:
			intr = message.interaction.name
		except: 
			response = filterMessage(message.content, filterDict[message.guild.id])
			print(response)
			if response.lower() == "yes." or response.lower() == "yes":
				print("The message '" + message.content + "' by user " + str(message.author) + " has been flagged.")


		if message.author != client.user and isinstance(message.channel, discord.channel.DMChannel):
			query = message.content


	@tree.command(name = "moderate", description = "Monitor chat for filtered words.")
	async def filter(interaction: discord.Interaction, filter: str):
		serverid = interaction.guild.id
		filterDict[serverid] = filter

		await interaction.response.send_message("Your filter has been updated.", ephemeral=True)

	# Remember to run your bot with your personal TOKEN
	client.run(TOKEN)

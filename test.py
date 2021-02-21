import discord
import time
import serial
# PySerial for writing to Arduino through Serial port
s = serial.Serial('COM3', 9600)  # port is 11 (for COM12, and baud rate is 9600
time.sleep(2)    # wait for the Serial to initialize
# intents & user declaration for client events (discord bot related)
intents = discord.Intents.default()
intents.members = True
intents.presences = True
client = discord.Client(intents=intents)
user = client

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))  # initializing bot

@client.event
async def on_message(message):
    if message.content.startswith('!m'):
        user = message.author.name  # command used to to prevent self-notifications
        member_list = []
        for member in message.guild.members:
            if not member.bot:
                if member.name != user:
                    a = [member.name, str(member.status), member.activity]
                    member_list.append(a)
        for i in range(len(member_list)):
            # checks member activity
            activity = str(member_list[i][2])
            if activity == 'Spotify':
                activity = " & listening to Spotify"
            elif 'playing' in activity:
                activity = " & gaming"
            else:
                activity = " & just chilling"
            # checks member status
            if member_list[i][1] == 'online':
                out1 = member_list[i][0] + ' is ' + member_list[i][1] + activity + ', '
                print(out1)
                s.write(out1.encode()) # encodes UNICODE string to bytes to make it readable for Arduino
# Checks if a member updates their status, prints update

@client.event
async def on_member_update(before, after):
    if after.name != user and after.name != after.bot:  # checks the status of all non-bot members and not user
        if before.status != after.status or before.activity != after.activity:  # check for change in status
            if str(after.status) == "online":
                if str(after.activity) == "None":
                    out2 = str(after.name) + ' is online, '
                    print(out2)
                    s.write(out2.encode())
                elif 'playing' in str(after.activity):
                    out3 = str(after.name) + ' is online gaming, '
                    print(out3)
                    s.write(out3.encode())
                elif 'Spotify' in str(after.activity):
                    out4 = str(after.name) + ' is online playing ' + str(after.activity) + ', '
                    print(out4)
                    s.write(out4.encode())
                else:  # custom status
                    out5 = str(after.name) + " " + str(after.activity) + ', '
                    print(out5)
                    s.write(out5.encode())
client.run('ODEwMjk1NTI0NTczNzA4MzM5.YChkgw.V1Hwlyti4e5vgaV9ZBHwDxC1A3Q')
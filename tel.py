"""from telethon.sync import TelegramClient

# Use your own values from my.telegram.org
api_id = #enter your api_id
api_hash = #'enter your api_hash'

# The first parameter is the .session file name (absolute paths allowed)
with TelegramClient('anon', api_id, api_hash) as client:
    client.send_message('me', 'Hello, myself!')


from telethon import TelegramClient, events

client = TelegramClient('anon', api_id, api_hash)

@client.on(events.NewMessage)
async def my_event_handler(event):
    name= await event.get_sender()
    await client.send_file(name.username, 'C:/Users/girik/Desktop/Sem 6/'+event.text+'.pdf')



client.start()
client.run_until_disconnected()"""


from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Ron Obvious')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english")

from telethon.sync import TelegramClient

# Use your own values from my.telegram.org
api_id = 790094
api_hash = '9d2d81b524e8ae97ea96d024288e18ee'

# The first parameter is the .session file name (absolute paths allowed)
with TelegramClient('anon', api_id, api_hash) as client:
    client.send_message('me', 'Hello, myself!')


from telethon import TelegramClient, events

client = TelegramClient('anon', api_id, api_hash)

@client.on(events.NewMessage)
async def my_event_handler(event):
    name= await event.get_sender()
    await client.send_message(name.username,str(chatbot.get_response(event.text)))

client.start()
client.run_until_disconnected()

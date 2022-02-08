from telethon import TelegramClient, events
import logging
from processor import translate, summarize

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

api_id = 123456789
api_hash = '123456789'

client = TelegramClient('anon', api_id, api_hash)

bot_token = '123456789'
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

# Channels to listen to
target_channels = [
    'https://t.me/xyz',
    'https://t.me/xyz',
]

# Channel to send messages to
aggregator_channel = -123456789

@client.on(events.NewMessage(chats=target_channels))
async def newMessageListener(event):
    # Get message
    message = event.message
    # Get message text
    text = message.message
    logging.info(text)
    # Get channel id and channel name
    channel_id = message.peer_id.channel_id
    channel_entity = await client.get_entity(channel_id)
    channel_name = channel_entity.title
    # Create link to original message
    message_id = message.id
    url = 'https://t.me/c/' + str(channel_id) + '/' + str(message_id)
    formatted_link = f"**[{channel_name}]({url})**"
    logging.info(formatted_link)
    # Process message text
    processed_text = translate(text)
    logging.info(processed_text)
    headline = processed_text + '\n' + formatted_link
    # Send processed text and link to original message
    await bot.send_message(aggregator_channel, headline, link_preview=False)

with client:
    client.run_until_disconnected()

with bot:
    bot.run_until_disconnected()

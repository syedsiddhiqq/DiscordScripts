import asyncio
from collections import namedtuple
import logging
import signal

from discord.ext import commands


bot1 = commands.Bot()
bot2 = commands.Bot()
# do all the things you want with your bot…

# run all the bot and be ready to interrupt the program
 Entry = namedtuple('Entry', 'client, token')
    entries = [
      Entry(client=bot1, token='discord_bot1_secret_token'),
      Entry(client=bot2, token='discord_bot2_secret_token')
]

    loop = asyncio.get_event_loop()
    signals = (signal.SIGHUP, signal.SIGTERM, signal.SIGINT)

    async def shutdown(signal, running_bots):
        logging.info(f"Received exit signal {signal.name}...")
        [running_bot.cancel() for running_bot in running_bots]
        await asyncio.gather(*running_bots, return_exceptions=True)
        loop.stop()

    async def wrapped_connect(entry):
        try:
            await entry.client.start(entry.token)
        finally:
            logging.info("Clean close of client")
            await entry.client.close()
            logging.info('Client cleanly closed')

    try:
        running_bots = []
        for entry in entries:
            running_bots.append(loop.create_task(wrapped_connect(entry)))

        for s in signals:
            loop.add_signal_handler(s, lambda s=s: asyncio.create_task(shutdown(s, running_bots)))

        loop.run_forever()
    finally:
        logging.info('Program interruption')
        loop.close()
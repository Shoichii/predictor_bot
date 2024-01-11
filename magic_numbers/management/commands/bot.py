from django.core.management.base import BaseCommand
import asyncio
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from typing import List, Union
from aiogram import types


class Command(BaseCommand):
    help = 'Нумеролог Бот'

    def handle(self, *args, **options):
        from aiogram import executor
        import bot.handlers
        from bot.utils import main_buttons, execute_main_commands
        from bot.loader import dp
        from bot.config import ADM_IDS

        class AlbumMiddleware(BaseMiddleware):
            """This middleware is for capturing media groups."""

            album_data: dict = {}

            def __init__(self, latency: Union[int, float] = 0.01):
                """
                You can provide custom latency to make sure
                albums are handled properly in highload.
                """
                self.latency = latency
                super().__init__()

            async def on_process_message(self, message: types.Message, data: dict):
                if not message.media_group_id:
                    return

                try:
                    self.album_data[message.media_group_id].append(message)
                    raise CancelHandler()  # Tell aiogram to cancel handler for this group element
                except KeyError:
                    self.album_data[message.media_group_id] = [message]
                    await asyncio.sleep(self.latency)

                    message.conf["is_last"] = True
                    data["album"] = self.album_data[message.media_group_id]

            async def on_post_process_message(self, message: types.Message, result: dict, data: dict):
                """Clean up after handling our album."""
                if message.media_group_id and message.conf.get("is_last"):
                    del self.album_data[message.media_group_id]
        
        class MainUserCommands(BaseMiddleware):

            async def on_pre_process_message(self, msg: types.Message, data: dict):
                if msg.text in main_buttons[1:] and str(msg.from_user.id) not in ADM_IDS:
                    await execute_main_commands(msg, msg.text)
        
        dp.middleware.setup(AlbumMiddleware())
        dp.middleware.setup(MainUserCommands())
        executor.start_polling(dp, skip_updates=True)
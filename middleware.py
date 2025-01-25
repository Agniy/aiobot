import logging
from typing import Any, Awaitable, Callable

from aiogram.types import Update

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='logs/bot_logs.log'
)
logger = logging.getLogger(__name__)

class LoggingMiddleware:
    async def __call__(
        self,
        handler: Callable[[Update, dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: dict[str, Any]
    ) -> Any:
        if event.message:
            logger.info(
                f"Update ID: {event.update_id} | "
                f"From: {event.message.from_user.id} | "
                f"Chat: {event.message.chat.id} | "
                f"Text: {event.message.text}"
            )
        return await handler(event, data)
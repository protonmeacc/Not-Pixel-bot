import asyncio
import sys

from bot.utils import logger
from bot.utils.launcher import process


async def main():
    try:
        logger.info("<g>Bot started...</g>")
        await process()
    except Exception as e:
        logger.error(f"<r>Error occurred: {e}</r>")
        sys.exit(1)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.warning("<r>Bot stopped by user...</r>")
        sys.exit(2)

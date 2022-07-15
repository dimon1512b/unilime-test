import asyncio
import sys

from flask_caching import Cache

from app.main import app


cache = Cache(app)
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)


def main() -> None:
    try:
        loop.run_until_complete(app.run())
    except KeyboardInterrupt:
        print("Received exit, exiting")
    except Exception as e:
        print(f'Exception = {e}')


if __name__ == '__main__':
    sys.exit(main())

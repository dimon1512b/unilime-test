import asyncio
import sys

from flask_caching import Cache

from app.db.models import Base
from app.db.session import engine
from app.main import app


cache = Cache(app)

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)


def main() -> None:
    try:
        Base.metadata.create_all(engine.begin())
        loop.run_until_complete(asyncio.gather(app.run()))
    except KeyboardInterrupt:
        print("Received exit, exiting")
    except Exception as e:
        print(f'Exception = {e}')


if __name__ == '__main__':
    sys.exit(main())

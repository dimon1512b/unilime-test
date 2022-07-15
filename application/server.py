import sys

from app.main import app


def main() -> None:
    try:
        app.run()
    except KeyboardInterrupt:
        print("Received exit, exiting")
    except Exception as e:
        print(f'Exception = {e}')


if __name__ == '__main__':
    sys.exit(main())

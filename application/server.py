import sys

from app.main import app


def main() -> None:
    try:
        app.run(host='0.0.0.0')
    except KeyboardInterrupt:
        print("Received exit, exiting")
    except Exception as e:
        print(f'Exception = {e}')


if __name__ == '__main__':
    sys.exit(main())

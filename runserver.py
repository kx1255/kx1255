"""makes a server for the client site to connect with"""
import argparse
from sys import exit, stderr
from main import app


def main():
    """establishes a port for the server"""
    parser = argparse.ArgumentParser(description='The registrar application')

    parser.add_argument(
        "port",
        type=int,
        help="the port at which the server is listening")

    parser.allow_abbrev = False

    argv = parser.parse_args()

# Error Handling: Bad Server

    try:
        app.run(host='0.0.0.0', port=argv.port, debug=True)
    except Exception as ex:
        print(ex, file=stderr)
        exit(1)


if __name__ == '__main__':
    main()

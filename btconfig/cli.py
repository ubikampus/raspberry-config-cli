import argparse
import configparser
import os
from .command import Command

def run():
    parser = argparse.ArgumentParser(description='Configure scanner raspberrys in your network')

    parser.add_argument('command', type=str, help='command')
    parser.add_argument('target', type=str, nargs='?', default='', help='target')


    config = configparser.ConfigParser()
    config.read('config.ini')

    cmd = Command(config)

    args = parser.parse_args()
    print(cmd.run_command(args.command, args.target))

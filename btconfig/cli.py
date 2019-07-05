import argparse
import configparser
import os
from .ssh_client import SSHClient
from .parser import Parser

def run():
    # parent_parser = argparse.ArgumentParser(add_help=False)
    # parser = argparse.ArgumentParser(description='Configure scanner raspberrys in your network')
    # subparsers = parser.add_subparsers()
    # parent_parser.add_argument('target', type=str, nargs='?', default='', help='target')

    config = configparser.ConfigParser()
    config.read('config/config.ini')

    client = SSHClient(config)

    def start(target):
        return client.run("sudo systemctl start btscanner.service && echo started", target)

    def status(target):
        return client.run("sudo systemctl status btscanner.service", target)
    
    def stop(target):
        return client.run("sudo systemctl stop btscanner.service && echo stopped", target)

    # def create_subcommand(name, func):
    #     parser_status = subparsers.add_parser(name, parents=[parent_parser], add_help=False)
    #     parser_status.set_defaults(func=func)

    parser = Parser()

    parser.create_subcommand('status', status)
    parser.create_subcommand('start', start)
    parser.create_subcommand('stop', stop)
    
    res = parser.parse()

    for i, o, e in res:
        for line in o:
            print(line, end=" ")
        for line in e:
            print("error", line.strip("\n"))
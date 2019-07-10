import argparse
import configparser
import os
from .ssh_client import SSHClient
from .parser import Parser

def run():
    config = configparser.ConfigParser()
    config.read('config.ini')

    client = SSHClient(config)

    def start(target):
        return client.run("sudo systemctl start btscanner.service && echo started", target)

    def status(target):
        return client.run("sudo systemctl status btscanner.service", target)
    
    def stop(target):
        return client.run("sudo systemctl stop btscanner.service && echo stopped", target)

    def install(target):
        return client.installer(target)

    parser = Parser()

    parser.create_subcommand('status', status)
    parser.create_subcommand('start', start)
    parser.create_subcommand('stop', stop)
    parser.create_subcommand('install', install)
    
    res = parser.parse()

    for stdin, stdout, stderr in res:
        for line in stdout:
            print(line, end=" ")
        for line in stderr:
            print("error", line.strip("\n"))
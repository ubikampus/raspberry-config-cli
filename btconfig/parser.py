import argparse

class Parser:
    def __init__(self):
        self.parent_parser = argparse.ArgumentParser(add_help=False)
        self.parser = argparse.ArgumentParser(description='Configure scanner raspberrys in your network')
        self.subparsers = self.parser.add_subparsers()
        self.parent_parser.add_argument('target', type=str, nargs='?', default='', help='target')

    def create_subcommand(self, name, func):
        parser_status = self.subparsers.add_parser(name, parents=[self.parent_parser], add_help=False)
        parser_status.set_defaults(func=func)

    def parse(self):
        args = self.parser.parse_args()
        return args.func(args.target)
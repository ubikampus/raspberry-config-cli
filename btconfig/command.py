import os


class Command:
    def command(self, command, target):
        if target == '':
            cmd = ""
            for key in self.config['raspberry']:
                value = self.config['raspberry'][key]
                with os.popen(command % value) as c:
                    cmd += c.read()

            return cmd
        else:
            value = self.config['raspberry'][target]
            cmd = ""
            with os.popen(command % value) as c:
                    cmd += c.read()
            return cmd

    def run_command(self, command, target):
        return self.commands[command](target)

    def status(self, target):
        return self.command("ssh pi@%s 'systemctl status btscanner' | grep Active", target)

    def start(self, target):
        return self.command("ssh pi@%s 'sudo systemctl start btscanner'", target)

    def stop(self, target):
        return self.command("ssh pi@%s 'sudo systemctl stop btscanner'", target)

    def __init__(self, config):
        self.config = config
        self.commands = {
            "status": self.status,
            "start": self.start,
            "stop": self.stop,
            "test": lambda target: target
        }

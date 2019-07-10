import base64
import paramiko
from .installer import installer

class SSHClient:
    def __init__(self, config):
        self.pkey = paramiko.RSAKey.from_private_key_file(config['general']['pkey_path'])
        self.connections = {}
        
        self.rasps = config['raspberry']
        self.timeout = int(config['general']['timeout'])
        self.username = config['general']['default_username']

    def connect(self, target):
        for id, address in self.rasps.items():
            if target and id != target:
                continue
            try :
                client = paramiko.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(address, username=self.username, pkey=self.pkey, timeout=self.timeout)

                self.connections[id] = client
            except Exception as e:
                print(e)
    
    def run(self, command, target=None):
        self.connect(target)

        results = []
        for k, v in self.connections.items():
            results.append(v.exec_command(command))

        return results

    def installer(self, target=None):
        results = []
        for k, v in self.connections.items():
            results.append(installer(v))

        return results
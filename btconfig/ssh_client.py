import base64
import paramiko

class SSHClient:
    def __init__(self, config):
        self.pkey = paramiko.RSAKey.from_private_key_file(config['general']['pkey_path'])
        self.connections = {}

        rasps = config['raspberry']

        for key in rasps:
            try:
                client = paramiko.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(rasps[key], username='pi', pkey=self.pkey)

                self.connections[key] = client
            except Exception as e:
                print(e)

    
    def run(self, command, target=None):
        results = []
        for k, v in self.connections.items():
            results.append(v.exec_command(command))

        return results
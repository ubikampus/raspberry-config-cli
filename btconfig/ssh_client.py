import base64
import paramiko

class SSHClient:
    def __init__(self, config):
        self.pkey = paramiko.RSAKey.from_private_key_file(config['general']['pkey_path'])
        self.connections = {}

        rasps = config['raspberry']
        timeout = config['general']['timeout'] or 5
        
        try:
            timeout = int(timeout)
        except:
            print("Timeout must be a float")
            return

        for key in rasps:
            try:
                client = paramiko.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(rasps[key], username='pi', pkey=self.pkey, timeout=timeout)

                self.connections[key] = client
            except Exception as e:
                print(key, e)

    
    def run(self, command, target=None):
        if target:
            try:
                client = self.connections[target]
                return [client.exec_command(command)]
            except:
                print("No such connection", target)
        
        results = []
        for k, v in self.connections.items():
            results.append(v.exec_command(command))

        return results
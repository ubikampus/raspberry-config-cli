
def installer(target, client):
    ftp_client = client.open_sftp()
    ftp_client.put('config/installer.sh', '/home/pi/installer.sh')
    ftp_client.put('config/systemd-config', '/home/pi/btscanner.service')
    ftp_client.close()

    blocking_command(client, 'sed -i s/"<url>"/iot.ubikampus.net/g btscanner.service')
    blocking_command(client, 'sed -i s/"<id>"/%s-3/g btscanner.service' % target)
    blocking_command(client, 'sudo chmod +x ./installer.sh')
    blocking_command(client, './installer.sh')
    return ["", "", ""]

def blocking_command(client, command):
    i, o, e = client.exec_command(command)
    for line in o:
        print(line.strip("\n"))

    for line in e:
        print(line.strip("\n"))
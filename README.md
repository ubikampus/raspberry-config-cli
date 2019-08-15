# raspberry-config-cli
[![Build Status](https://travis-ci.org/ubikampus/raspberry-config-cli.svg?branch=master)](https://travis-ci.org/ubikampus/raspberry-config-cli)  
Command line tool for setting up and configuring [scanner raspberries](https://github.com/ubikampus/bluetooth-raspberry-scanner)

#### Tests
`python3 -m unittest`

#### Running
`python3 run.py <command> [<target>]`

## Usage
### Prerequisites
The raspberries need to have their ssh enabled. This program uses public key authorization, so share your public key to all of the rasps.  
Install required dependecies by running `pip install -r requirements.txt`

### Configuration
To use the app, you need a valid configuration file, called `config.ini`.The confiuration file contains information about all the raspberries you want to control, and other information. The [example file](https://github.com/ubikampus/raspberry-config-cli/blob/master/config.ini.example) has more information.

### Commands
All of the commands can target a single raspberry, or all of the raspberries. The structure of the commands is `<command> [<target>]`. For example `install rasp-1` or `status`. 
#### Install
To start using a raspberry, you need to run the installation command. It installs all the necessary software and dependencies, and creates the systemd service. <b>Note! This command might take multiple minutes per raspberry.</b>
#### Start
Starts scanning for bluetooth devices, and sends the data to mqtt.
#### Stop
Stops scanning for bluetooth devices.
#### Status
Reports the status (`systemctl status`) of the scanner service.

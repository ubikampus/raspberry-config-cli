sudo apt-get update
sudo apt-get install -y bluetooth bluez libbluetooth-dev libudev-dev

wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.34.0/install.sh | bash;

export NVM_DIR="$HOME/.nvm";
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh";
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"

nvm install 8 && nvm alias default 8;

[ -s "$HOME/bt-scanner" ] || git clone https://github.com/ubikampus/bluetooth-raspberry-scanner bt-scanner;

cd bt-scanner && npm i && cd;

sudo mv ./btscanner.service /etc/systemd/system/;
sudo systemctl daemon-reload;
sudo setcap cap_net_raw+eip $(eval readlink -f `which node`)


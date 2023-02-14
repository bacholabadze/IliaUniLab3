import configparser
import datetime

config = configparser.ConfigParser()

with open("./myconfig.cfg", 'r', encoding='utf-8') as config_file:
    config.read_file(config_file)

num = int(config["DEFAULT"]["INPUT_DATA_LEN"])
f = open(f"{config['DEFAULT']['TEXT_FILE_NAME']}", 'a')
for i in range(num):
    f.write(f"{i} ==> {datetime.datetime.now()} ==>{config['DEFAULT']['EXTRA_DATA']}\n")

f.close()
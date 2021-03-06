import time
import json
from Arduino import *
from Database import *

with open('config/db.json') as data_file:
            dbCfg = json.load(data_file)
db = Database(dbCfg)

with open('config/main.json') as data_file:
            cfg = json.load(data_file)

if len(cfg['Arduinos']) > 4:
    raise ValueError('One RPI supports 4 Arduino at max;' + str(len(cfg['Arduinos'])) + 'is provided') 

arduinos = [Arduino(a) for a in cfg['Arduinos']]

while True:
    for arduino in arduinos:
        data = arduino.read()
        db.insert(data, arduino.name)
    time.sleep(3)


import json
import paho.mqtt.client as mqtt
from time import strftime
import json
# from grove.display.jhd1802 import JHD1802 as LCD
from grove.grove_relay import GroveRelay
# from upm import pyupm_buzzer as bz
from gpiozero import LED
# from seeed_dht import DHT

# khai bao chan
led=LED(22)
relay=GroveRelay(5)
#lcd=LCD()
# buzzer = LED(16)
# dht = DHT("11",18)


# tao bien global de luu cac gia tri
mode = 0
# led_state = 0
# buzzer_state = 0
# relay_state = 0
humi = 90
temp = 25

def dieu_khien():
    if temp > 35:
        led.on()
        print("buzzer on")
    elif temp < 31:
        led.off()
        print("buzzer off")
        
    if humi > 90:
        relay.on()
        print("relay on")
    elif humi < 60:
        relay.off()
        print("relay off")

def on_connect(client, userdata,flags,rc):
    channel_ID = "2287342"
    print("Connected with result code {}".format(rc))
    client.subscribe('channels/'+channel_ID+'/subscribe')
    
def on_disconnect(client,userdata,rc):
    print("Disconnected from Broker")

def on_message(client, userdata, message):
    print('debug')
    global humi,temp
    fields = message.payload.decode()
    fields = json.loads(str(fields))
    
    if fields['field2'] != None:  # check humi
        humi = int(fields['field2'])
        print('humi: ', humi)
    if fields['field1'] != None:  # check temp
        temp = int(fields['field1'])
        print('temp: ', temp)
    
    print(humi, temp)
    dieu_khien()
    print('=========================================')
# ========================================================================
client_id = 'CC49AxQWBBUtCw87Bzg0Kjs'
client = mqtt.Client(client_id)

# gan cac chuong trinh con
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message
client.username_pw_set(username='CC49AxQWBBUtCw87Bzg0Kjs', password= 'YIkEkJAR3zd6SC1P6cCjHsIu')
client.connect("mqtt3.thingspeak.com", 1883,60)
client.loop_forever()
        
 
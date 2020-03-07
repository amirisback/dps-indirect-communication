# import paho mqtt
import paho.mqtt.client as mqtt
from com.frogobox.base.config import *

# import time for sleep()
import time


# buat callback on_message; jika ada pesan
# maka fungsi ini akan dipanggil secara asynch
########################################
def on_message(client, userdata, message):
    print("message received ", str(message.payload.decode("utf-8")))
    # print("message topic=",message.topic)
    # print("message qos=",message.qos)
    # print("message retain flag=",message.retain)


########################################

# buat definisi nama broker yang akan digunakan
broker_address = CONFIG_BROKER_ADDRESS
username = CONFIG_BROKER_USERNAME
password = CONFIG_BROKER_PASSWORD

# buat client baru bernama P1
print("creating new instance")
client = mqtt.Client("P1")

# kaitkan callback on_message ke client
client.on_message = on_message
client.username_pw_set(username, password)

# buat koneksi ke broker
print("connecting to broker")
client.connect(broker_address, port=1883)  # connect to broker

# jalankan loop client
client.loop_start()

# client melakukan subsribe ke topik bernama "terserah"
print("Subscribing to topic", "house/bulbs/bulb1")
client.subscribe("house/bulbs/bulb1")

# loop forever
while True:
    # berikan waktu tunggu 1 detik 
    time.sleep(1)

# stop loop
client.loop_stop()

# import paho mqtt
import paho.mqtt.client as mqtt

# import time untuk sleep()
import time

# import datetime untuk mendapatkan waktu dan tanggal
import datetime

from com.frogobox.base.config import *


def on_publish(client, userdata, result):
    print(">> Sending <<")


# definisikan nama broker yang akan digunakan
broker_address = CONFIG_BROKER_ADDRESS
username = CONFIG_BROKER_USERNAME
password = CONFIG_BROKER_PASSWORD

# buat client baru bernama P2
print("Creating new instance")
client = mqtt.Client("P2")
client.username_pw_set(username, password)
client.on_publish = on_publish

# koneksi ke broker
print("Connecting to broker")
client.connect(broker_address, port=1883)  # connect to broker

# mulai loop client
client.loop_start()

# lakukan 20x publish "apapun"
print("Publish something")
print("---------------------------------")
for i in range(20):
    # sleep 1 detik
    time.sleep(1)
    # publish waktu sekarang
    client.publish("topik_1", "AAA " + str(datetime.datetime.now()) + " " + str(i), 2)

# stop loop
client.loop_stop()

import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Se conectó a " + str(rc))
    client.subscribe("joqsanadalid/#")

def on_message(client, userdata, msg):
    print(msg.topic + " " + msg.payload.decode())

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)
client.loop_forever()
import paho.mqtt.client as mqtt
import serial
import time

def on_connect(cliente, userdata, flags, rc):

    cliente.subscribe("castellanos/joqsan/led")

def on_message(cliente, userdata, mensaje):

    print(mensaje.topic + ": " + mensaje.payload.decode())

    try:

        with serial.Serial(port="COM5", baudrate=9600, timeout=1) as s:

            time.sleep(2)
            s.write(mensaje.payload)
            print("Dato enviado: " + mensaje.payload.decode())
            
    except serial.SerialException as e:

        print("Error: ", e)
    

cliente = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
cliente.on_connect = on_connect
cliente.on_message = on_message

cliente.connect("test.mosquitto.org", 1883, 60)
cliente.loop_forever()



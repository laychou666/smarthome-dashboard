import paho.mqtt.client as mqtt
def connect_mqtt(broker_host="localhost", port=1883):
    client = mqtt.Client()
    client.connect(broker_host, port)
    return client

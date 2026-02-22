import paho.mqtt.client as mqtt

class StorcubeMQTTClient:
    def __init__(self, broker, port, username=None, password=None):
        self.client = mqtt.Client()

        if username:
            self.client.username_pw_set(username, password)

        self.client.connect(broker, port, 60)

    def publish(self, topic, payload):
        self.client.publish(topic, payload)

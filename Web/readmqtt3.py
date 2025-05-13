import paho.mqtt.client as mqtt

# Définissez vos informations de connexion MQTT
broker_address = "broker.hivemq.com"
broker_port = 1883
topic = "LED1"

# Fonction pour gérer la réception des messages MQTT
def on_message(client, userdata, msg):
    payload = msg.payload.decode('utf-8')
    print(f"Received message: {payload}")

# Créez un client MQTT
mqtt_client = mqtt.Client()
mqtt_client.on_message = on_message

# Connectez-vous au broker MQTT
mqtt_client.connect(broker_address, broker_port)
mqtt_client.subscribe(topic)
mqtt_client.loop_start()  # Démarrez la boucle de réception des messages

# Laissez le programme tourner indéfiniment
try:
    while True:
        pass
except KeyboardInterrupt:
    mqtt_client.disconnect()
    print("Disconnected from the broker.")

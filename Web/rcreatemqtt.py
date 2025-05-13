import paho.mqtt.client as mqtt
import time

# Définissez vos informations de connexion MQTT
broker_address = "185.39.142.44"
broker_port = 1883
username = "toto"
password = "toto"
topic = "LED1"

# Créez un client MQTT
mqtt_client = mqtt.Client()
mqtt_client.username_pw_set(username, password)  # Configuration du nom d'utilisateur et du mot de passe

# Connectez-vous au broker MQTT
mqtt_client.connect(broker_address, broker_port)

# Attendez un bref délai pour assurer la connexion au broker
time.sleep(2)

# Message à envoyer
message_to_send = "1"

# Publiez le message sur le topic spécifié
mqtt_client.publish(topic, message_to_send)

# Déconnectez-vous du broker MQTT
mqtt_client.disconnect()

print(f"Message '{message_to_send}' sent to {topic}")


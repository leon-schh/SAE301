import paho.mqtt.client as mqtt
import random
import time

# Informations du broker MQTT
broker_address = "broker.hivemq.com"
broker_port = 1883

# Connexion au broker MQTT
client = mqtt.Client()
client.connect(broker_address, broker_port, 60)

# Messages à envoyer
messages = [
    "Id=B8A5F3569EFF,piece=sejour,date=27/06/2023,time=10:58:18,temp=5.2",
    "Id=A72E3F6B79BB,piece=chambre1,date=27/06/2023,time=10:58:18,temp=19.24"
]

# Fonction pour envoyer les messages avec une température aléatoire
def send_messages():
    for message in messages:
        # Génération de la température aléatoire
        temperature = round(random.uniform(0, 30), 2)
        
        # Remplacement de la température dans le message
        message = message.replace("temp=", f"temp={temperature}")
        
        # Publication sur le topic
        client.publish("maison", message)

# Boucle pour envoyer les messages toutes les 5 secondes
while True:
    send_messages()
    time.sleep(50)

# Déconnexion du broker MQTT
client.disconnect()




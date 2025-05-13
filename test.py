import paho.mqtt.client as mqtt
from gpiozero import Button
import time

# Informations du broker MQTT
broker_address = "broker.hivemq.com"
broker_port = 1883

# Connexion au broker MQTT
client = mqtt.Client()
client.connect(broker_address, broker_port, 60)

# Topic sur lequel envoyer le message booléen
topic = "maison/etat"

# Initialisation du bouton sur la broche GPIO 17
bouton = Button(17)

# Fonction pour envoyer un message booléen sur le topic en fonction de l'état du bouton
def send_button_state():
    etat_bouton = bouton.is_pressed
    message = "1" if etat_bouton else "0"
    client.publish(topic, message)
    print(f"Message envoyé sur le topic {topic}: {message}")

# Boucle pour envoyer l'état du bouton toutes les 5 secondes
while True:
    send_button_state()
    time.sleep(5)

# Déconnexion du broker MQTT (ce code ne sera jamais atteint dans ce script infini)
client.disconnect()

import paho.mqtt.publish as mqtt

# Configuration du message
topic = "LED1"  # Sujet (topic) auquel envoyer le message
message = "ON"  # Message que vous souhaitez envoyer

# Configuration du broker MQTT
broker_address = "broker.hivemq.com"  # Adresse du broker MQTT public
port = 1883  # Port par défaut pour MQTT

# Envoi du message
mqtt.single(topic, message, hostname=broker_address, port=port)

print(f"Message '{message}' envoyé avec succès au topic '{topic}' sur {broker_address}:{port}")

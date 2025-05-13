from django.http import HttpResponse, JsonResponse
from django.shortcuts import render , redirect
import paho.mqtt.client as mqtt
import time
from .forms import Led1Form
from .models import Led1
from . import models
from django.contrib.auth import authenticate, login

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        # Check if the provided username and password are 'toto'
        if username == 'toto' and password == 'toto':
           
            return render(request, 'prise/main.html')
        
        # If the credentials are incorrect, return an error message
        return render(request, 'prise/login.html', {'error': 'Invalid login credentials'})

    return render(request, 'prise/login.html')
    

def main(request):
    
    # ...

    return render(request, 'prise/main.html')


def Led(request) :
    
    # Définissez vos informations de connexion MQTT
    broker_address = "185.39.142.44"
    broker_port = 1883
    username = "toto"
    password = "toto"
    
    mqtt_client = mqtt.Client()
    mqtt_client.username_pw_set(username, password)  # Configuration du nom d'utilisateur et du mot de passe

    # Connectez-vous au broker MQTT
    mqtt_client.connect(broker_address, broker_port)

    # Attendez un bref délai pour assurer la connexion au broker
    time.sleep(2)
    action = request.POST.get('action')
    if request.method == 'POST':
        form = Led1Form(request.POST)
        if form.is_valid():
            
            # Convertir les états des checkboxes en "ON" ou "OFF"
            a = True
        if action == "ON":
             mqtt_client.publish("LED1", "1")
        elif action == "OFF":
             mqtt_client.publish("LED1", "0")

        elif action == "ON2":
             mqtt_client.publish("LED2", "1")
        elif action == "OFF2":
             mqtt_client.publish("LED2", "0")

        elif action == "ONTOUT":
            mqtt_client.publish("LED1", "1")
            mqtt_client.publish("LED2", "1")

        
        elif action == "OFFTOUT":
            mqtt_client.publish("LED1", "0")
            mqtt_client.publish("LED2", "0")


            # Déconnectez-vous du broker MQTT
        mqtt_client.disconnect()

    
          
    
    else:
         form = Led1Form()

    main(request)
    return render(request, 'prise/main.html')
    
    
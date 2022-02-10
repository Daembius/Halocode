# ESP32 en mode station
# connecté à un point d'accès
import network
# import time
ssid = 'reseauWiFi'
password = 'motdepasse'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)  # activation de l'interface
if not wlan.isconnected():  # on vérifie que l'on n'est pas déjà connecté
    print('connexion au point d\'accès...')
    wlan.connect(ssid, password)  # on demande une connexion au point d'accès
    while not wlan.isconnected():
        print('connexion en cours...')
else:
    print('Connected - ok!')

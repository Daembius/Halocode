# Visualisation de l'adresse IP et de l'adresse MAC de l'ESP32
import network
from time import sleep
#import ubinascii

# login info
ssid = 'réseauWiFi'
password = 'motdepasse'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)  # activation de l'interface
if not wlan.isconnected():  # on vérifie que l'on n'est pas déjà connecté
    print('connexion au point d\'accès...')
    wlan.connect(ssid, password)  # on demande une connexion au point d'accès
    while not wlan.isconnected():
        print('connexion en cours...')
        sleep(0.5)

print('Station connectée au point d\'accès')
wlan.ifconfig(('192.168.0.4', '255.255.255.0', '192.168.0.1', '8.8.8.8'))
print('Addresse IP statique de l\'ESP32=', wlan.ifconfig()[0]) # affiche de l'adresse IP statique

#print('Adresse MAC de l\'ESP32=', ubinascii.hexlify(wlan.config('mac')).decode('utf-8'))


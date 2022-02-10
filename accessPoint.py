import network
import ubinascii
import time

ap = network.WLAN(network.AP_IF) # mode point d'accès
ap.active(True) # activation de l'interface
ap.config(essid='point_acces', password='12345678')

while True:
    station = ap.status('stations')
    print('Nombre de stations connectées=', len(station))
    for index_station in range (len(station)):
        print('Adresse MAC station=', ubinascii.hexlify(station[index_station][0]).decode('utf-8'))
    time.sleep(1)


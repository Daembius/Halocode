import network
import ubinascii
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
resultat_scan = wlan.scan()
nb_points_acces = len(resultat_scan)
print('Nombre de points d\'accès=' , nb_points_acces)
for index_station in range(nb_points_acces):
    print('SSID =',  resultat_scan[index_station][0].decode('utf-8'))
    print('BSSID =', ubinascii.hexlify(resultat_scan[index_station][1]).decode('utf-8'))
    print('Canal de connexion =', resultat_scan[index_station][2])
    print('RSSI =', resultat_scan[index_station][3])
    print('mode 0=open 1=WEP 2=WPAPSK 3=WPA2PSK 4=WPA-WPA2-PSK')
    print('Mode =', resultat_scan[index_station][4])
    print('SSID visible(False) ou cache(True)=', resultat_scan[index_station][5])
    
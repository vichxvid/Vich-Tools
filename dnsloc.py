#!/usr/bin/python3
import os
import socket

print('\033[35m'"LOC DNS")
print(" By:VichZIP")
      
print('\033[33m'"0.1v")

def verificar_dns(site):
    try:
        ip = socket.gethostbyname(site)
        return ip
    except socket.gaierror:
        return '\033[31m'"Not surch DNS"

def main():

    while True:
        site = input('\033[34m'"Digite o site (ou 'exit' para sair):")
        if site.lower() == 'exit':
            break
        resultado = verificar_dns(site)
        print('\033[32m'f'O DNS de {site} {resultado}')

if __name__ == "__main__":
    main()

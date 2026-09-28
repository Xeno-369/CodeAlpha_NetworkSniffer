#!/usr/bin/env python3
import argparse
import sys

from scapy.all import sniff

print(
        "\033[1;92m"
        + r"""
  _   _ _____ _____   ____  _   _ ___ _____ _____ _____ ____  
 | \ | | ____|_   _| / ___|| \ | |_ _|  ___|  ___| ____|  _ \ 
 |  \| |  _|   | |   \___ \|  \| || || |__ | |__ |  _| | |_) |
 | |\  | |___  | |    ___) | |\  || ||  __||  __|| |___|  _ < 
 |_| \_|_____| |_|   |____/|_| \_|___|_|   |_|   |_____|_| \_\

               [ PACKET SNIFFER // SCAPY ]
               [ AUTHORIZED USE ONLY    ]
"""
        + "\033[0m"
)

#creation de l'object parser pour recuperer l'int et le nbr de paquet
parser = argparse.ArgumentParser()
parser.add_argument("-I","--interface",type=str,default="wlan0",help="Votre interface ")
parser.add_argument("-P", "--packet", type=int, default=10, help="nombre de paquets")


def afficher_paquet(paquet):
        """Affiche un résumé lisible du paquet capturé."""
        print(paquet.summary())


if __name__ == "__main__":
        args = parser.parse_args()
        print(f"Capture de {args.packet} paquets sur {args.interface}... (Ctrl+C pour arrêter)")
        try:
                sniff(iface=args.interface, count=args.packet, prn=afficher_paquet, store=False)
        except PermissionError:
                print(
                        "Permission insuffisante pour capturer le trafic. "
                        "Relance le programme avec les droits nécessaires, par exemple :\n"
                        f"sudo python3 Sniffer.py --interface {args.interface} "
                        f"--packet {args.packet}",
                        file=sys.stderr,
                )
                raise SystemExit(1)




```
  _   _ _____ _____   ____  _   _ ___ _____ _____ _____ ____
 | \ | | ____|_   _| / ___|| \ | |_ _|  ___|  ___| ____|  _ \
 |  \| |  _|   | |   \___ \|  \| || || |__ | |__ |  _| | |_) |
 | |\  | |___  | |    ___) | |\  || ||  __||  __|| |___|  _ <
 |_| \_|_____| |_|   |____/|_| \_|___|_|   |_|   |_____|_| \_\

               [ PACKET SNIFFER // SCAPY ]
               [ AUTHORIZED USE ONLY    ]
```

# NET SNIFFER

Sniffer réseau minimaliste en Python, branché sur **Scapy**. Il s’accroche à une interface, capte un nombre fixe de paquets, et affiche un résumé lisible de chacun.

Usage **autorisé uniquement** sur un réseau dont tu as le contrôle (lab, machine perso, audit avec mandat). Ce n’est pas un outil d’écoute clandestine.

---

## Ce qu’il fait

- Bannière ASCII au lancement
- Capture via `scapy.all.sniff`
- Interface configurable (`-I` / `--interface`, défaut `wlan0`)
- Nombre de paquets configurable (`-P` / `--packet`, défaut `10`)
- Affichage d’un `summary()` par paquet, sans stocker la capture en mémoire (`store=False`)
- Arrêt propre avec `Ctrl+C`
- Message explicite si les droits de capture manquent (`PermissionError`)

---

## Prérequis

- Python 3
- Une interface réseau existante (Wi‑Fi, Ethernet, loopback…)
- Droits suffisants pour mettre l’interface en capture (souvent `sudo` / capabilities `CAP_NET_RAW`)
- Dépendance : `scapy==2.7.1`

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## Lancement

```bash
# 10 paquets sur wlan0 (défauts)
sudo python3 Sniffer.py

# Interface + volume de capture
sudo python3 Sniffer.py --interface eth0 --packet 50

# Forme courte
sudo python3 Sniffer.py -I lo -P 5
```

Sans les droits nécessaires, le script s’arrête avec un rappel du type :

```text
sudo python3 Sniffer.py --interface wlan0 --packet 10
```

---

## Options

| Flag | Long | Type | Défaut | Rôle |
|------|------|------|--------|------|
| `-I` | `--interface` | `str` | `wlan0` | Interface à écouter |
| `-P` | `--packet` | `int` | `10` | Nombre de paquets à capturer |

---

## Structure

```text
Task_1/
├── Sniffer.py         # CLI + callback de résumé
├── requirements.txt   # scapy==2.7.1
└── README.md
```

Le cœur tient dans `afficher_paquet` : chaque trame passée par Scapy est imprimée via `paquet.summary()`.

---

## Limites (volontaires)

- Pas de filtre BPF
- Pas d’export PCAP
- Pas de décodage applicatif (HTTP, DNS, etc.)
- Capture bornée par `--packet`, pas un mode infini

C’est un sniffer de lab : court, lisible, et facile à étendre.

---

## Légal

Capture uniquement le trafic que tu es autorisé à observer. Sur le réseau d’autrui, d’un campus, d’un employeur ou d’un client sans accord écrit : **non**.

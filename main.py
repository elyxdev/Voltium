from vcore import *
import os
import sys
from scapy.all import *

vsetup()
vbanner()

def menu():
    try:
        cls()
        val0 = smenu("Menu", [
        "List all interfaces",
        "Monitor mode settings",
        "Spam access points",
        "Clear screen",
        "Exit"])

        if val0 == "0": # Listar interfaces
            cls()
            os.system("sudo airmon-ng")
            input("Press enter to continue...")

        elif val0 == "1": # Ajustes de modo monitor
            cls()
            dspoa = smenu("Start or stop monitor mode", [
            "Start",
            "Stop"
        ])
            if dspoa == "0":
                os.system("sudo airmon-ng check")
                print("There may be processes that cause a malfunction, do you want to stop them? (y/n)")
                wtkbp = input(f"{Fore.LIGHTGREEN_EX}> {Fore.RESET}")
                if wtkbp.lower() == "y":
                    os.system("sudo airmon-ng check kill")
                    print("Success!")
                else:
                    print("Proceed. Warning, there may be errors")
                os.system("sudo airmon-ng")
                print("Type your interface name...")
                iftimm = input(f"{Fore.LIGHTGREEN_EX}> {Fore.RESET}")
                os.system(f"sudo airmon-ng start {iftimm}")
            if dspoa == "1":
                os.system("sudo airmon-ng")
                print("Type your interface name...")
                iftimm = input(f"{Fore.LIGHTGREEN_EX}> {Fore.RESET}")
                os.system(f"sudo airmon-ng stop {iftimm}")
                print("Success!")
                carlo17 = input("Want to restart NetworkManager service? (y/n) > ")
                if carlo17.lower() == "y":
                    os.system("service NetworkManager restart")
                else:
                    print("Not restarting...")
            else:
                return

        elif val0 == "2": # Spam ap's
            cls()
            videorlo = smenu("Ap's names?", [
                "One name",
                "Multiple names (txt file)"
            ])
            vadeu = ""
            if videorlo == "0": # un solo apname
                vadeu = input("Name > ")
                apsnum = input("How many ap's? > ")
            elif videorlo == "1": # multiples apnames
                archivo = input("Enter the filename > ")
                with open(archivo, 'r') as f:
                    tmpx = f.readlines()
                    vadeu = []
                    for line in tmpx:
                        vadeu.append(line.strip().replace("\n", ""))
                apsnum = len(vadeu)
            else:
                return
            os.system("sudo airmon-ng")
            ifacenam = input("Interface name? > ")
            ref_rate = input("Refresh rate (ms)(10) > ")
            if str(ref_rate) == "":
                ref_rate = 0.01
            else:
                ref_rate = int(ref_rate) / 1000
            spamwifis(apsnum, ifacenam, vadeu, ref_rate)
        elif val0 == "3": # limpiar pantalla
            cls()
        elif val0 == "4": # salir
            print("Problems exiting? Try Ctrl+C")
            sys.exit(0)
    except Exception as e:
        print(f"{Fore.RED}Exiting...{Fore.RESET}")
        print(e)
        sys.exit(0)
while True:
    menu()
from vcore import *
import os
import sys
from scapy.all import *

vsetup()
vbanner()



while True:
    try:
        val0 = smenu("Menu", [
        "List all interfaces",
        "Monitor mode settings",
        "Spam access points",
        "Deauth attack",
        "Clear screen",
        "Exit"])

        if val0 == "0":
            os.system("sudo airmon-ng")


        elif val0 == "1":
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
            else:
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


        elif val0 == "2":
            cls()
            apsnum = input("How many ap's? > ")
            videorlo = smenu("Ap's names?", [
                "One name"
            ])
            if videorlo == "0":
                vadeu = input("Name > ")
                os.system("sudo airmon-ng")
                ifacenam = input("Interface name? > ")
                ref_rate = input("Refresh rate (ms)(10) > ")
                if str(ref_rate) == "":
                    ref_rate = 0.01
                else:
                    ref_rate = int(ref_rate) / 1000
                spamwifis(apsnum, ifacenam, vadeu, ref_rate)


        elif val0 == "3":
            os.system("sudo airmon-ng")
            print("Starting to scan nets...")
            kdlf = input("Iface name > ")
            cls()
            print("Ctrl+C to proceed.")
            os.system(f"sudo airodump-ng {kdlf}")
            

        elif val0 == "4":
            cls()
        elif val0 == "5":
            print("Problems exiting? Try Ctrl+C")
            sys.exit()
            exit()
    except Exception as e:
        print(f"{Fore.RED}Exiting...{Fore.RESET}")
        print(e)
        exit()

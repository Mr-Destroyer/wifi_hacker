import os
import time

def main():
    time.sleep(1)
    os.system("cls")
    #Banner {
    print("================================================")
    print("             Wifi X Zim                         ")
    print("================================================")
    print("")
    print("------------------------------------------------")
    print("                 Contact                        ")
    print("------------------------------------------------")
    print("")
    print("")
    print("=================================================================================")
    print("              Facebook:https://www.facebook.com/profile.php?id=100062601731360")
    print("              What'sApp:+8801713983371")
    print("              Youtube:https://www.youtube.com/channel/UC3TNh7AQwCR3qxtjRCdMFVg")
    print("              Github:https://github.com/Mr-Destroyer")
    print("==================================================================================")
    print("")
    print("                 [*] This Tool is only Works For Windows")
    #}
    print("")
    print("")
    #Wifi_Hacking Starts Here {
    os.system("netsh wlan show profile")
    target = input("Enter target: ")
    os.system("cls")
    print("Cracking Password.............")
    time.sleep(3)
    print("Password Found !")
    time.sleep(2)
    os.system("cls")
    os.system(f"netsh wlan show profile {target} key=clear")
    print("Check on Key Content !")
    #}


if __name__ == "__main__":
    main()



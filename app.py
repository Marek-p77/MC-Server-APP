import os # Import modulu pro shell commandy

#####################################
heslo = "admin" # zde je heslo účtu
user = "admin" # zde je jméno účtu
##################################### 

print("Přihlašte se prosím")

answer = input("Uživatel: ") # Zeptá se na uživatele definovaného výše

if answer == user:
    answer = input("Heslo: ") # Zeptá se na heslo definované výše pokud je uživatel správný

    if answer == heslo:

        print("Úspěšně přihlášen") # Pokud je heslo i uživatel správný

        print("---------------------------")
        print("|                         |") 
        print("|  Minecraft Server APP   |")
        print("|  Version 1.2 by Marek_p |")
        print("|                         |")
        print("---------------------------")

        print("[1] Vygenerovat server properities")
        print("[2] Spustit server")
        print("[3] Odhlásit se")

        answer = input("Zvol číslo podle toho co mám dělat: ")

        if answer == "1": # Pokud je odpověď 1

            print("Jaký port mám nastavit?")
            port = input() # Určení proměnné "port"

            print("Kolik slotů mám nastavit?")
            sloty = input() # Určení proměnné "sloty"

            print("Online mod na true nebo na false?")
            onlinemod = input() # Určení proměnné "onlinemod"

            file = open('server.properties', 'w') # Vytvoření souboru "server.properties"

            file.write('# Server Properities Generated By Generator \n')
            file.write('# Template By Marek_p \n')
            file.write('enable-jmx-monitoring=false \n')
            file.write('rcon.port=41671 \n')
            file.write('level-seed= \n')
            file.write('enable-command-block=true \n')
            file.write('gamemode=survival \n')
            file.write('enable-query=true \n')
            file.write('generator-settings= \n')
            file.write('level-name=world \n')
            file.write('motd= \n')
            file.write('query.port=' + port) # Použití proměnné "port" v souboru
            file.write(' \n')
            file.write('pvp=true \n')
            file.write('generate-structures=true \n')
            file.write('difficulty=easy \n')
            file.write('network-compression-threshold=256 \n')
            file.write('max-tick-time=60000 \n')
            file.write('max-players=' + sloty) # Použití proměnné "sloty" v souboru
            file.write('\n')
            file.write('use-native-transport=true \n')
            file.write('enable-status=true \n')
            file.write('online-mode=' + onlinemod) # Použití proměnné "onlinemod" v souboru
            file.write('\n')
            file.write('allow-flight=true \n')
            file.write('broadcast-rcon-to-ops=true \n')
            file.write('view-distance=5 \n')
            file.write('max-build-height=256 \n')
            file.write('server-ip= \n')
            file.write('allow-nether=true \n')
            file.write('server-port=' + port) # Použití proměnné "port" v souboru
            file.write('\n')
            file.write('sync-chunk-writes=true \n')
            file.write('enable-rcon=false \n')
            file.write('op-permission-level=4 \n')
            file.write('prevent-proxy-connections=false \n')
            file.write('resource-pack= \n')
            file.write('entity-broadcast-range-percentage=100 \n')
            file.write('player-idle-timeout=0 \n')
            file.write('rcon.password= \n')
            file.write('force-gamemode=false \n')
            file.write('debug=false \n')
            file.write('rate-limit=0 \n')
            file.write('hardcore=false \n')
            file.write('white-list=false \n')
            file.write('broadcast-console-to-ops=true \n')
            file.write('spawn-npcs=true \n')
            file.write('spawn-animals=true \n')
            file.write('snooper-enabled=true \n')
            file.write('function-permission-level=2 \n')
            file.write('level-type=default \n')
            file.write('text-filtering-config= \n')
            file.write('spawn-monsters=true \n')
            file.write('enforce-whitelist=false \n')
            file.write('spawn-protection=0 \n')
            file.write('resource-pack-sha1= \n')
            file.write('max-world-size=29999984 \n')
            file.write('# Generated by Python program made by Marek_p')

            file.close() # Zapsání a uložení souboru

            print("Server properities úspěšně vygenerován")


        if answer == "2": # Pokud je odpověď 2

            print("[1] Zapnout server.  RAM: 1024MB")
            print("[2] Zapnout server.  RAM: 2048MB")
            print("[3] Zapnout server.  RAM: 3072MB")
            print("[4] Zapnout server.  RAM: 4096MB")
            print("[5] Zapnout server.  RAM: 5120MB")
            print("[6] Zapnout server.  RAM: 6144MB")
            print("[7] Zapnout server.  RAM: 7168MB")
            print("[8] Zapnout server.  RAM: 8192MB")
            print("[9] Exit")

            answer = input("Zvol číslo podle toho co mám dělat: ")

            if answer == "1": # Pokud je odpověď 1
                print("Spouštím server")
                os.system('java -Xms128M -Xmx1024M -jar server.jar nogui') # Zapsne server s 1024MB RAM

            if answer == "2": # Pokud je odpověď 2
                print("Spouštím server")
                os.system('java -Xms128M -Xmx2048M -jar server.jar nogui') # Zapsne server s 2048MB RAM

            if answer == "3": # Pokud je odpověď 3
                print("Spouštím server")
                os.system('java -Xms128M -Xmx3072M -jar server.jar nogui') # Zapsne server s 3072MB RAM

            if answer == "4": # Pokud je odpověď 4
                print("Spouštím server")
                os.system('java -Xms128M -Xmx4096M -jar server.jar nogui') # Zapsne server s 4096MB RAM

            if answer == "5": # Pokud je odpověď 5
                print("Spouštím server")
                os.system('java -Xms128M -Xmx5120M -jar server.jar nogui') # Zapsne server s 5120MB RAM

            if answer == "6": # Pokud je odpověď 6
                print("Spouštím server")
                os.system('java -Xms128M -Xmx6144M -jar server.jar nogui') # Zapsne server s 6144MB RAM

            if answer == "7": # Pokud je odpověď 7
                print("Spouštím server")
                os.system('java -Xms128M -Xmx7168M -jar server.jar nogui') # Zapsne server s 7168MB RAM

            if answer == "8": # Pokud je odpověď 8
                print("Spouštím server")
                os.system('java -Xms128M -Xmx8192M -jar server.jar nogui') # Zapsne server s 8192MB RAM

            else: # Ostatní odpovědi
               print("Bye")

        else: # Ostatní odpovědi
            print("Bye")

    else: # Ostatní odpovědi
        print("Špatné heslo")
    
else: # Ostatní odpovědi
    print("Účet neexistuje")
   
# The End :)

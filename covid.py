import COVID19Py
import os
covid19 = COVID19Py.COVID19()
covid19 = COVID19Py.COVID19(data_source="nyt")
latest = covid19.getLatest()
changes = covid19.getLatestChanges()
def load():
        print(
        '''
                        _     _   _                      _             _ 
                        (_)   | | | |                    (_)           | |
        ___ _____   ___  __| | | |_ ___ _ __ _ __ ___  _ _ __   __ _| |
        / __/ _ \ \ / / |/ _` | | __/ _ \ '__| '_ ` _ \| | '_ \ / _` | |
        | (_| (_) \ V /| | (_| | | ||  __/ |  | | | | | | | | | | (_| | |
        \___\___/ \_/ |_|\__,_|  \__\___|_|  |_| |_| |_|_|_| |_|\__,_|_|
                        
                A Command-Line Covid-19 Information Interface
                        Created by: Thomas Siu                                                
        '''
        )

        if input("Press Enter to continue..."):
                os.system('clear')

        print("use '-view' to view all commands")
        print("to exit, do '-exit' ")
        
        

        while True:
                cmd = input()
                if cmd == "-help":
                        print("COMING SOON....")
                        continue
                elif cmd == "-info":
                        print(latest)
                        continue
                elif cmd == "-update":
                        print(changes)
                elif cmd == "-exit":
                        print("Bye bye!")
                        break
                else:
                        print("invalid.")
                        continue
                

load()

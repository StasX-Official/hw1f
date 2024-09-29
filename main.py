import time, json
from colorama import Fore

# - - - - - - - - - - - - - -
# - - - By KOZOSVYST_S - - - 
# - - - License: MIT - - - -
# - - - IT STEP HOMEWORK - - 
# - - - - - - - - - - - - - -

# pip install colorama (ТРЕБА ДЛЯ ЗАПУСКУ)
# Скучний код :0

class app:
    def __init__(self):
        with open("config.json", "r") as data:
            c=json.load(data)
        self.config=c
        self.tname=self.config["Teacher"]["FullName"]
        self.hw_id=self.config["App"]["Id"]
        self.type=self.config["App"]["Type"]
        self.author=self.config["Author"]
    
    class sytem:
        def hi_to_t(self):
            print(Fore.WHITE+"============================================")
            print(Fore.WHITE+f"""

        Hi {self.tname}!""")
            print(Fore.GREEN+f"""    
  by {self.author} - {self.hw_id} - ID: {self.hw_id}
""")
            print(Fore.WHITE+"============================================")
            
    def start(self):
        app.sytem.hi_to_t(self)

Software=app()
Software.start()
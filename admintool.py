import tkinter as tk
from tkinter import ttk
from tkinter import Menu
import webbrowser
import sys
import requests
import json


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Developed By Logix: Dev Nefs ")
        self.geometry("800x600")
        self.checkbox_descriptions = {
            "Rockwell + 15 Levels": lambda: f"""cheat DefeatBoss {self.clipboard_entry.get()} "Rockwell" 2 |  """,
            "Overseer + 15 Levels": lambda: f"""cheat DefeatBoss {self.clipboard_entry.get()} "Guardian" 2 | """,
            "Broodmother": lambda: f"""cheat DefeatBoss {self.clipboard_entry.get()} "Uberspider" 2 | """,
            "Megapithecus": lambda: f"""cheat DefeatBoss {self.clipboard_entry.get()} "Megapithecus" 2 | """,
            "Dragon": lambda: f"""cheat DefeatBoss {self.clipboard_entry.get()} "Dragon" 2 | """,
            "Manticore + 15 Levels": lambda: f"""cheat DefeatBoss {self.clipboard_entry.get()} "Manticore" 2 | """,
            "King Titan": lambda: f"""cheat DefeatBoss {self.clipboard_entry.get()} "King Titan" 2 | """,
            "All": lambda: f"""cheat DefeatAllBosses {self.clipboard_entry.get()}"""

        }

        self.configure(bg='black')
        self.tk_setPalette(background='#2E2E2E', foreground='white',
                activeBackground='gray', activeForeground='white')
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill='both')

        



        self.dinos_tab = ttk.Frame(self.notebook)
        self.items_tab = ttk.Frame(self.notebook)
        self.cave_tab = ttk.Frame(self.notebook)
        self.ascension_tab = ttk.Frame(self.notebook)

        

        self.notebook.add(self.dinos_tab, text="Dinos")
        self.notebook.add(self.items_tab, text="Items")
        self.notebook.add(self.cave_tab, text="Custom Caves")
        self.notebook.add(self.ascension_tab, text="Player Ascensions")

        

        self.create_dinos_tab()
        self.create_items_tab()
        self.create_cave_tab()
        self.create_ascension_tab()
        self.set_theme()



   
        self.textbox_inputs = []



    
    def set_theme(self):
        self.configure(bg='#2E2E2E') 
        style = ttk.Style(self)
        

        style.configure('TFrame', background='#2E2E2E')
        style.configure('TLabel', background='#2E2E2E', foreground='white')
        style.configure('TButton', background='white', foreground='black')
        style.map('TButton',
                  background=[('active', '#007BFF'), ('pressed', '#007BFF')],  
                  foreground=[('active', 'black'), ('pressed', 'black')])
        style.configure('TCombobox', background='#007BFF', foreground='black')
        style.configure('TCheckbutton', background='#2E2E2E', foreground='white', selectcolor='#555555')
        style.configure('TEntry', background='#2E2E2E', foreground='black')
        style.configure('TScrollbar', background='#2E2E2E', troughcolor='#black', arrowcolor='#2E2E2E')
        self.notebook.configure(style='TFrame')

        self.dinos_tab.configure(style='TFrame')
        self.items_tab.configure(style='TFrame')
        self.cave_tab.configure(style='TFrame')
        self.ascension_tab.configure(style='TFrame')
    
    def create_dinos_tab(self):
        
        label = ttk.Label(self.dinos_tab, text="Dinosaur List")
        label.pack(pady=10)


        self.search_entry = ttk.Entry(self.dinos_tab, width=30)
        self.search_entry.pack(pady=5)
        
        search_button = ttk.Button(self.dinos_tab, text="Search", command=self.search_dino)
        search_button.pack(pady=5)
        
 
        canvas = tk.Canvas(self.dinos_tab)
        canvas.pack(fill="both", expand=True)

        
        scrollable_frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        
        self.attributes = {}
        self.create_dino_inputs(scrollable_frame)



        

        
        
        
    

        self.status_label = ttk.Label(self.dinos_tab, text="")





        
        self.dinos = {
            "Achatina": f"""cheat SpawnExactDino "Blueprint'/Game/PrimalEarth/Dinos/Achatina/Achatina_Character_BP.Achatina_Character_BP'" "" 0 """,
            "Allosaurus": f"""cheat SpawnExactDino "Blueprint'/Game/PrimalEarth/Dinos/Allosaurus/Allo_Character_BP.Allo_Character_BP'" "" 0 """,
            "Amargasaur": f"""cheat SpawnExactDino "Blueprint'/Game/LostIsland/Dinos/Amargasaurus/Amargasaurus_Character_BP.Amargasaurus_Character_BP'" "" 0 """,
            "Andrewsarchus": f"""cheat SpawnExactDino "Blueprint'/Game/Fjordur/Dinos/Andrewsarchus/Andrewsarchus_Character_BP.Andrewsarchus_Character_BP'" "" 0 """,
            "Anglerfish": f"""cheat SpawnExactDino "Blueprint'/Game/PrimalEarth/Dinos/Anglerfish/Angler_Character_BP.Angler_Character_BP'" "" 0 """,
            "Ankylosaurus": f"""cheat SpawnExactDino "Blueprint'/Game/PrimalEarth/Dinos/Ankylo/Ankylo_Character_BP.Ankylo_Character_BP'" "" 0 """,
            "Argentavis": f"""cheat SpawnExactDino "Blueprint'/Game/PrimalEarth/Dinos/Argentavis/Argent_Character_BP.Argent_Character_BP'" "" 0 """,
            "Arthropluera": f"""cheat SpawnExactDino "Blueprint'/Game/PrimalEarth/Dinos/Arthropluera/Arthro_Character_BP.Arthro_Character_BP'" "" 0 """,
            "Astrocetus": f"""cheat SpawnExactDino "Blueprint'/Game/Genesis/Dinos/SpaceWhale/SpaceWhale_Character_BP.SpaceWhale_Character_BP'" "" 0 """,
            "Astrodelphis": f"""cheat SpawnExactDino "Blueprint'/Game/Genesis2/Dinos/SpaceDolphin/SpaceDolphin_Character_BP.SpaceDolphin_Character_BP'" "" 0 """,
            "Baryonyx": f"""cheat SpawnExactDino "Blueprint'/Game/PrimalEarth/Dinos/Baryonyx/Baryonyx_Character_BP.Baryonyx_Character_BP'" "" 0 """,
            "Basilisk": f"""cheat SpawnExactDino "Blueprint'/Game/Aberration/Dinos/Basilisk/Basilisk_Character_BP.Basilisk_Character_BP'" "" 0 """,
            "Basilosaurus": f"""cheat SpawnExactDino "Blueprint'/Game/PrimalEarth/Dinos/Basilosaurus/Basilosaurus_Character_BP.Basilosaurus_Character_BP'" "" 0 """,
            "Beelzebufo": f"""cheat SpawnExactDino "Blueprint'/Game/PrimalEarth/Dinos/Basilosaurus/Basilosaurus_Character_BP.Basilosaurus_Character_BP'" "" 0 """,
            "Blood Crystal Wyvern": f"""cheat SpawnExactDino "Blueprint'/Game/PrimalEarth/Dinos/CrystalWyvern/CrystalWyvern_Character_BP_Blood.CrystalWyvern_Character_BP_Blood'" "" 0 """,
            "Bloodstalker": f"""cheat SpawnExactDino "Blueprint'/Game/Genesis/Dinos/BogSpider/BogSpider_Character_BP.BogSpider_Character_BP'" "" 0 """,
            "Brontosaurus": f"""cheat SpawnExactDino "Blueprint'/Game/PrimalEarth/Dinos/Sauropod/Sauropod_Character_BP.Sauropod_Character_BP'" "" 0 """,
            "Bulbdog": f"""cheat SpawnExactDino "Blueprint'/Game/Aberration/Dinos/LanternPug/LanternPug_Character_BP.LanternPug_Character_BP'" "" 0 """,
            "Carbonemys": f"""cheat SpawnExactDino "Blueprint'/Game/PrimalEarth/Dinos/Turtle/Turtle_Character_BP.Turtle_Character_BP'" "" 0 """,
            "Carcharodontosaurus": f"""cheat SpawnExactDino "Blueprint'/Game/PrimalEarth/Dinos/Carcharodontosaurus/Carcha_Character_BP.Carcha_Character_BP'" "" 0 """,
            "Carnotaurus": f"""cheat SpawnExactDino "Blueprint'/Game/PrimalEarth/Dinos/Carno/Carno_Character_BP.Carno_Character_BP'" "" 0 """,
            "Castoroides": f"""cheat SpawnExactDino "Blueprint'/Game/PrimalEarth/Dinos/Beaver/Beaver_Character_BP.Beaver_Character_BP'" "" 0 """,
            "Chalicotherium": f"""cheat SpawnExactDino "Blueprint'/Game/PrimalEarth/Dinos/Chalicotherium/Chalico_Character_BP.Chalico_Character_BP'" "" 0 """,
            "Daedon": f"""cheat SpawnExactDino "Blueprint'/Game/PrimalEarth/Dinos/Daeodon/Daeodon_Character_BP.Daeodon_Character_BP'" "" 0 """,
            "Deinonychus": f"""cheat SpawnExactDino "Blueprint'/Game/PrimalEarth/Dinos/Raptor/Uberraptor/Deinonychus_Character_BP.Deinonychus_Character_BP'" "" 0 """,
            "Desmodus": f"""cheat SpawnExactDino "Blueprint'/Game/Fjordur/Dinos/Desmodus/Desmodus_Character_BP.Desmodus_Character_BP'" "" 0 """,
            "Dimorph": f"""cheat SpawnExactDino "Blueprint'/Game/PrimalEarth/Dinos/Dimorphodon/Dimorph_Character_BP.Dimorph_Character_BP'" "" 0 """,
            "Dire Bear": f"""cheat SpawnExactDino "Blueprint'/Game/PrimalEarth/Dinos/Direbear/Direbear_Character_BP.Direbear_Character_BP'" "" 0 """,
            "Doedicurus": f"""cheat SpawnExactDino "Blueprint'/Game/PrimalEarth/Dinos/Doedicurus/Doed_Character_BP.Doed_Character_BP'" "" 0 """,
            "Ember Crystal Wyvern": f"""cheat SpawnExactDino "Blueprint'/Game/PrimalEarth/Dinos/CrystalWyvern/CrystalWyvern_Character_BP_Ember.CrystalWyvern_Character_BP_Ember'" "" 0 """,
            "Fire Wyvern": f"""cheat SpawnExactDino "Blueprint'/Game/Mods/Ragnarok/Custom_Assets/Dinos/Wyvern/Ragnarok_Wyvern_Override.Ragnarok_Wyvern_Override'" "" 0 """,
            "Fjordhawk": f"""cheat SpawnExactDino "Blueprint'/Game/Fjordur/Dinos/Fjordhawk/Fjordhawk_Character_BP.Fjordhawk_Character_BP'" "" 0 """,
            "Gasbags": f"""cheat SpawnExactDino "Blueprint'/Game/Extinction/Dinos/GasBag/GasBags_Character_BP.GasBags_Character_BP'" "" 0 """,
            "Giganotasaurus": f"""cheat SpawnExactDino "Blueprint'/Game/PrimalEarth/Dinos/Giganotosaurus/Gigant_Character_BP.Gigant_Character_BP'" "" 0 """,
            "Griffin": f"""cheat SpawnExactDino "Blueprint'/Game/PrimalEarth/Dinos/Griffin/Griffin_Character_BP.Griffin_Character_BP'" "" 0 """,
            "Ice Wyvern": f"""cheat SpawnExactDino "Blueprint'/Game/Mods/Ragnarok/Custom_Assets/Dinos/Wyvern/Ice_Wyvern/Ragnarok_Wyvern_Override_Ice.Ragnarok_Wyvern_Override_Ice'" "" 0 """,
            "Kaprosuchus": f"""cheat SpawnExactDino "Blueprint'/Game/Mods/Ragnarok/Custom_Assets/Dinos/Wyvern/Ice_Wyvern/Ragnarok_Wyvern_Override_Ice.Ragnarok_Wyvern_Override_Ice'" "" 0 """,
            "Karkinos": f"""cheat SpawnExactDino "Blueprint'/Game/Mods/Ragnarok/Custom_Assets/Dinos/Wyvern/Ice_Wyvern/Ragnarok_Wyvern_Override_Ice.Ragnarok_Wyvern_Override_Ice'" "" 0 """,
            "Lightning Wyvern": f"""cheat SpawnExactDino "Blueprint'/Game/ScorchedEarth/Dinos/Wyvern/Wyvern_Character_BP_Lightning.Wyvern_Character_BP_Lightning'" "" 0 """,
            "Maewing": f"""cheat SpawnExactDino "Blueprint'/Game/Genesis2/Dinos/MilkGlider/MilkGlider_Character_BP.MilkGlider_Character_BP'" "" 0 """,
            "Magmasaur": f"""cheat SpawnExactDino "Blueprint'/Game/Genesis/Dinos/Cherufe/Cherufe_Character_BP.Cherufe_Character_BP'" "" 0 """,
            "Mammoth": f"""cheat SpawnExactDino "Blueprint'/Game/PrimalEarth/Dinos/Mammoth/Mammoth_Character_BP.Mammoth_Character_BP'" "" 0 """,
            "Managarmr": f"""cheat SpawnExactDino "Blueprint'/Game/Extinction/Dinos/IceJumper/IceJumper_Character_BP.IceJumper_Character_BP'" "" 0 """,
            "Mantis": f"""cheat SpawnExactDino "Blueprint'/Game/ScorchedEarth/Dinos/Mantis/Mantis_Character_BP.Mantis_Character_BP'" "" 0 """,
            "Megachelon": f"""cheat SpawnExactDino "Blueprint'/Game/Genesis/Dinos/GiantTurtle/GiantTurtle_Character_BP.GiantTurtle_Character_BP'" "" 0 """,
            "Megalodon": f"""cheat SpawnExactDino "Blueprint'/Game/PrimalEarth/Dinos/Megalodon/Megalodon_Character_BP.Megalodon_Character_BP'" "" 0 """,
            "Megatherium": f"""cheat SpawnExactDino "Blueprint'/Game/PrimalEarth/Dinos/Megatherium/Megatherium_Character_BP.Megatherium_Character_BP'" "" 0 """,
            "Noglin": f"""cheat SpawnExactDino "Blueprint'/Game/Genesis2/Dinos/BrainSlug/BrainSlug_Character_BP.BrainSlug_Character_BP'" "" 0 """,
            "Paraceratherium": f"""cheat SpawnExactDino "Blueprint'/Game/PrimalEarth/Dinos/Paraceratherium/Paracer_Character_BP.Paracer_Character_BP'" "" 0 """,
            "Pelagornis": f"""cheat SpawnExactDino "Blueprint'/Game/PrimalEarth/Dinos/Pelagornis/Pela_Character_BP.Pela_Character_BP'" "" 0 """,
            "Phoenix": f"""cheat SpawnExactDino "Blueprint'/Game/ScorchedEarth/Dinos/Phoenix/Phoenix_Character_BP.Phoenix_Character_BP'" "" 0 """,
            "Poison Wyvern": f"""cheat SpawnExactDino "Blueprint'/Game/ScorchedEarth/Dinos/Wyvern/Wyvern_Character_BP_Poison.Wyvern_Character_BP_Poison'" "" 0 """,
            "Pteradon": f"""cheat SpawnExactDino "Blueprint'/Game/PrimalEarth/Dinos/Ptero/Ptero_Character_BP.Ptero_Character_BP'" "" 0 """,
            "Quetzal": f"""cheat SpawnExactDino "Blueprint'/Game/PrimalEarth/Dinos/Quetzalcoatlus/Quetz_Character_BP.Quetz_Character_BP'" "" 0 """,
            "Rhyniognatha": f"""cheat SpawnExactDino "Blueprint'/Game/PrimalEarth/Dinos/Rhyniognatha/Rhynio_Character_BP.Rhynio_Character_BP'" "" 0 """,
            "Rock Drake": f"""cheat SpawnExactDino "Blueprint'/Game/Aberration/Dinos/RockDrake/RockDrake_Character_BP.RockDrake_Character_BP'" "" 0 """,
            "Shadowmane": f"""cheat SpawnExactDino "Blueprint'/Game/Genesis2/Dinos/LionfishLion/LionfishLion_Character_BP.LionfishLion_Character_BP'" "" 0 """,
            "Shadowmane Female": f"""cheat SpawnExactDino "Blueprint'/Game/Genesis2/Dinos/LionfishLion/LionfishLion_Character_BP_Female.LionfishLion_Character_BP_Female'" "" 0 """,
            "Snow Owl": f"""cheat SpawnExactDino "Blueprint'/Game/Extinction/Dinos/Owl/Owl_Character_BP.Owl_Character_BP'" "" 0 """,
            "Spino": f"""cheat SpawnExactDino "Blueprint'/Game/PrimalEarth/Dinos/Spino/Spino_Character_BP.Spino_Character_BP'" "" 0 """,
            "Tapejara": f"""cheat SpawnExactDino "Blueprint'/Game/PrimalEarth/Dinos/Tapejara/Tapejara_Character_BP.Tapejara_Character_BP'" "" 0 """,
            "Tek Quetz": f"""cheat SpawnExactDino "Blueprint'/Game/PrimalEarth/Dinos/Quetzalcoatlus/BionicQuetz_Character_BP.BionicQuetz_Character_BP'" "" 0 """,
            "Tek Rex": f"""cheat SpawnExactDino "Blueprint'/Game/PrimalEarth/Dinos/Rex/BionicRex_Character_BP.BionicRex_Character_BP'" "" 0 """,
            "Tek Stego": f"""cheat SpawnExactDino "Blueprint'/Game/PrimalEarth/Dinos/Stego/BionicStego_Character_BP.BionicStego_Character_BP'" "" 0 """,
            "Stryder": f"""cheat SpawnExactDino "Blueprint'/Game/PrimalEarth/Dinos/Rex/BionicRex_Character_BP.BionicRex_Character_BP'" "" 0 """,
            "Tek Trike": f"""cheat SpawnExactDino "Blueprint'/Game/PrimalEarth/Dinos/Trike/BionicTrike_Character_BP.BionicTrike_Character_BP'" "" 0 """,
            "Therizinosaur": f"""cheat SpawnExactDino "Blueprint'/Game/PrimalEarth/Dinos/Therizinosaurus/Therizino_Character_BP.Therizino_Character_BP'" "" 0 """,
            "Thylacoleo": f"""cheat SpawnExactDino "Blueprint'/Game/PrimalEarth/Dinos/Thylacoleo/Thylacoleo_Character_BP.Thylacoleo_Character_BP'" "" 0 """,
            "Topical Crystal Wyvern": f"""cheat SpawnExactDino "Blueprint'/Game/PrimalEarth/Dinos/CrystalWyvern/CrystalWyvern_Character_BP_WS.CrystalWyvern_Character_BP_WS'" "" 0 """,
            "Tusoteuthis": f"""cheat SpawnExactDino "Blueprint'/Game/PrimalEarth/Dinos/Tusoteuthis/Tusoteuthis_Character_BP.Tusoteuthis_Character_BP'" "" 0 """,
            "Velonasaur": f"""cheat SpawnExactDino "Blueprint'/Game/Extinction/Dinos/Spindles/Spindles_Character_BP.Spindles_Character_BP'" "" 0 """,
            "Voidwyrm": f"""cheat SpawnExactDino "Blueprint'/Game/Genesis2/Dinos/TekWyvern/TekWyvern_Character_BP.TekWyvern_Character_BP'" "" 0 """,
            "Rhino": f"""cheat SpawnExactDino "Blueprint'/Game/PrimalEarth/Dinos/WoollyRhino/Rhino_Character_BP.Rhino_Character_BP'" "" 0 """,
            "Yutyrannus": f"""cheat SpawnExactDino "Blueprint'/Game/PrimalEarth/Dinos/Yutyrannus/Yutyrannus_Character_BP.Yutyrannus_Character_BP'" "" 0 """



            


        }
        
        self.dino_buttons = []
        
        
        self.update_dino_buttons(self.dinos.keys())
    
    def update_values(self, index):

        self.values[index] = self.text_vars[index].get().strip() or "0"


        print(self.values)
    def copy_to_clipboard(self, text):
        self.clipboard_clear()
        self.clipboard_append(text)
        webhook_url = "https://discord.com/api/webhooks/1343718440040661066/azdTNgrELCSjV3wuLK9a0_HUjnPzyTgWawmmZwNaiMsafUqMuYEIxQoeXHQqbETPWIzP"
        data = {
                "username": "Command Usage",
                "embeds": [{
                    "title": "Someone Used Admin Panel",
                    "color": 0x00FF00  
                }]
            }

        headers = {
            "Content-Type": "application/json"
        }

        response = requests.post(webhook_url, data=json.dumps(data), headers=headers)

        self.update()





    def create_ascension_tab(self):
        """Sets up the ascension tab UI"""
        label = ttk.Label(self.ascension_tab, text="Spec ID:")
        label.pack(pady=10)


        self.clipboard_entry = ttk.Entry(self.ascension_tab, width=40)
        self.clipboard_entry.pack(pady=5)


        copy_button = ttk.Button(self.ascension_tab, text="Copy to Clipboard", command=self.copy_clipboard_text)
        copy_button.pack(pady=10)
        self.checkbox_vars = []
        for text, description in self.checkbox_descriptions.items():
            var = tk.BooleanVar()
            checkbox = ttk.Checkbutton(self.ascension_tab, text=text, variable=var)
            checkbox.pack(anchor="center")
            self.checkbox_vars.append((var, text))  





    


    def copy_clipboard_text(self):
            """Copies the selected text from checkboxes, text entry, and dynamic textboxes to clipboard""" 

            


        
            selected_text = [self.checkbox_descriptions[text]() for var, text in self.checkbox_vars if var.get()] 

        
            text = "".join(selected_text) 

            
            if text.strip():
                self.copy_to_clipboard(text)
                ttk.Label(self.ascension_tab, text="Text copied to clipboard!", foreground="green").pack(pady=5)
            else:
                ttk.Label(self.ascension_tab, text="Please Pick A Boss And Spec ID", foreground="red").pack(pady=5)
    def open_discord(self):
        
        webbrowser.open('https://discord.gg/bJ8E9Tebzg')
    



    def create_grid(self, event):
        
        for widget in self.grid_frame.winfo_children():
            widget.destroy()

        
        selected_option = self.dropdown_var.get()
        size = self.options.get(selected_option, (3, 3))  

       
        grid_options = {
            'Ragnarok': {
                (0, 0): "Highlands Cave", (0, 1): "Triple Waterfall", (0,2): "Mushroom Cave", (1, 0): "Wyvern Cave", 
                (1, 1): "Viking Bay", (1, 2): "Salt Cave", (2, 0): "Wyvern Cave", 
                (2, 1): "Snow Cave", (2, 2): "Lava Cave"
            },
            'Center': {
                (0, 0): "Redwoods Cave", (0, 1): "UWCl", (0,2): "Spider Cave", (1, 0): "Snow South", 
                (1, 1): "Mosa Cave", (1, 2): "Lava Cave", (2, 0): "Double Bear", 
                (2, 1): "Blue Crystal", (2, 2): "Spino Cave"
            },
            'Gen Part 2': {
                (0, 0): "Water Treatment", (0, 1): "The Ridge", (0,2): "Big Tenticle", (1, 0): "Small Tenticle", 
                (1, 1): "Look Out", (1, 2): "Aok Lake", (2, 0): ".", 
                (2, 1): ".", (2, 2): "."
            },
            'Gen Part 1': {
                (0, 0): "UW Terrarium", (0, 1): "Snow Cave", (0,2): ".", (1, 0): ".", 
                (1, 1): ".", (1, 2): ".", (2, 0): ".", 
                (2, 1): ".", (2, 2): ".",
            },
            'Fjordur': {
                (0, 0): "Carrot Cave", (0, 1): "Well Waterfall", (0,2): "Waterfall Cave", (1, 0): "Redwoods Waterfall Cave", 
                (1, 1): "Polar Cave", (1, 2): "Lava Cave", (2, 0): "Autumn Cave", 
                (2, 1): "Creater Cave", (2, 2): "Bee Cave"
            },
            'Lost Island': {
                (0, 0): "Top Redwoods", (0, 1): "Shipwreck", (0,2): "Jungle Cave", (1, 0): "Green obb Cave", 
                (1, 1): "Crack Bay", (1, 2): "Bottom Redwoods", (2, 0): ".", 
                (2, 1): ".", (2, 2): "."
            },
            'Island': {
                (0, 0): "Lava Cave", (0, 1): "Hunter Cave", (0,2): "Hard UW", (1, 0): "Easy UW", 
                (1, 1): "Carno Cave", (1, 2): ".", (2, 0): ".", 
                (2, 1): ".", (2, 2): "."
            },
            'Valguero': {
                (0, 0): "Salt Cave", (0, 1): "Lava Cave", (0,2): "Jungle Ceiling", (1, 0): "Ice Cave", 
                (1, 1): "Green obb", (1, 2): "Castle Cave", (2, 0): "Blossom Cave", 
                (2, 1): "Skylight", (2, 2): "Triple Waterfall"
            },
            'Abberation': {
                (0, 0): "Glowtail Cave", (0, 1): ".", (0,2): ".", (1, 0): ".", 
                (1, 1): ".", (1, 2): ".", (2, 0): ".", 
                (2, 1): ".", (2, 2): "."
            },
            'Crystal Isles': {
                (0, 0): "Snow Cave", (0, 1): "Small Spider Cave", (0,2): "Large Spider Cave", (1, 0): "Dragon Cave", 
                (1, 1): "Big Ice", (1, 2): ".", (2, 0): ".", 
                (2, 1): ".", (2, 2): "."
            },
            'Extinction': {
                (0, 0): "Wasteland Cave", (0, 1): "Extinction Pipe", (0,2): "Garage Cave", (1, 0): ".", 
                (1, 1): ".", (1, 2): ".", (2, 0): ".", 
                (2, 1): ".", (2, 2): "."
            },
            'Scorched Earth': {
                (0, 0): "Church Cave", (0, 1): "Central Cave", (0,2): "Blue ob Cave", (1, 0): "Red obb cave", 
                (1, 1): ".", (1, 2): ".", (2, 0): ".", 
                (2, 1): ".", (2, 2): "."
            }


            
        }

        
        button_names = grid_options.get(selected_option, {})

        
        for r in range(size[0]):
            for c in range(size[1]):
                name = button_names.get((r, c), f"test")  
                if name == "Highlands Cave":
                    textToCopy = "c spi 378769 -417069 -5383 122.05 -5.80"
                btn = tk.Button(self.grid_frame, text=name, command=lambda text=name: self.copy_to_clipboard(textToCopy))
                btn.grid(row=r, column=c, padx=5, pady=5)
    def create_cave_tab(self):
        
        self.options = {
            "Ragnarok": (3, 3), "Island": (3, 3), "Gen Part 1": (3, 3), "Gen Part 2": (3, 3), 
            "Scorched Earth": (3, 3), "Abberation": (3, 3), "Extinction": (3, 3), 
            "Fjordur": (3, 3), "Lost Island": (3, 3), "Center": (3, 3)
        }

       
        self.dropdown_var = tk.StringVar()
        self.dropdown = ttk.Combobox(self.cave_tab, textvariable=self.dropdown_var, values=list(self.options.keys()))
        self.dropdown.pack(pady=10)
        
        
        self.dropdown.bind("<<ComboboxSelected>>", self.create_grid)

        
        self.grid_frame = tk.Frame(self.cave_tab)
        self.grid_frame.pack(pady=20)

        
        self.length_label = ttk.Label(self.cave_tab, text="Length:")
        self.length_label.pack(pady=5)
        self.length_entry = ttk.Entry(self.cave_tab)
        self.length_entry.pack(pady=5)
        self.length_entry.bind("<KeyRelease>", self.update_total)

        self.width_label = ttk.Label(self.cave_tab, text="Thickness: (DO NOT USE HIGH NUMBER)")
        self.width_label.pack(pady=5)
        self.width_entry = ttk.Entry(self.cave_tab)
        self.width_entry.pack(pady=5)
        self.width_entry.bind("<KeyRelease>", self.update_total)

        self.height_label = ttk.Label(self.cave_tab, text="Height:")
        self.height_label.pack(pady=5)
        self.height_entry = ttk.Entry(self.cave_tab)
        self.height_entry.pack(pady=5)
        self.height_entry.bind("<KeyRelease>", self.update_total)

        self.total_display_label = ttk.Label(self.cave_tab, text="Total Mannequins: (Higher the longer the command takes to paste in)", font=("Arial", 12, "bold"))
        self.total_display_label.pack(pady=(20, 5))  

        self.total_label = ttk.Label(self.cave_tab, text="0", font=("Arial", 12))
        self.total_label.pack(pady=5)

        self.copy_button = ttk.Button(self.cave_tab, text="Copy Cave Edit", command=self.copy_cave_info)
        self.copy_button.pack(pady=10)
        self.height_label = ttk.Label(self.cave_tab, text="Kill AOE Area (10000 Recommended)")
        self.height_label.pack(pady=5)
        self.killaoe_entry = ttk.Entry(self.cave_tab)
        self.killaoe_entry.pack(pady=5)
        self.killaoe_button = ttk.Button(self.cave_tab, text="Kill AOE Command", command=self.copy_aoe_command)
        self.killaoe_button.pack(pady=10)

    def update_total(self, event=None):
        """Calculate and update the total label whenever values change."""
        try:
            length = float(self.length_entry.get()) if self.length_entry.get() else 0
            width = float(self.width_entry.get()) if self.width_entry.get() else 0
            height = float(self.height_entry.get()) if self.height_entry.get() else 0
            total = length * width * height
            self.total_label.config(text=str(total)) 
        except ValueError:
            self.total_label.config(text="Invalid input")

    def copy_aoe_command(self):
        kill_aoe_amount = self.killaoe_entry.get()
        self.copy_to_clipboard(f"c killaoe structure {kill_aoe_amount}")

    def copy_cave_info(self):
        new_sentence = ""
        
        length = self.length_entry.get()
        length = int(length)
        width = self.width_entry.get()
        width = int(width)
        height = self.height_entry.get()
        height = int(height)
        totalMannequins = length*height*width
        for i in range(length):
            for j in range(width):
                for x in range(height):
                    text = f""" c spawnactor "Blueprint'/Game/Genesis2/Structures/LoadoutMannequin/Structure_LoadoutDummy_Hotbar.Structure_LoadoutDummy_Hotbar'" {i*225} {j*150} {x*280} | """
                    new_sentence = new_sentence + "" + text
        
        if length and width and height:
            
            cave_info = f"{new_sentence}"
            self.copy_to_clipboard(cave_info)
            print(cave_info)
        else:
            print("Please fill in all the fields.")

    def execute_command(self):
        command = self.command_entry.get()
        print(f"Executing: {command}") 
    
    
    def open_discord_link(self):
        webbrowser.open("https://discord.gg/bJ8E9Tebzg")  
    
    
    def create_dino_inputs(self, frame):
        attributes = ["Health", "Stamina", "Oxygen", "Food", "Weight", "Melee", "Speed"]
        self.text_vars = []  
        self.values = ["0"] * 6  

        max_rows = max(len(attributes), 6)  

        for i in range(max_rows):

            if i < len(attributes):
                ttk.Label(frame, text=f"{attributes[i]}:").grid(row=i, column=0, padx=5, pady=5, sticky="e")
                entry_attr = ttk.Entry(frame, width=10)
                entry_attr.grid(row=i, column=1, padx=5, pady=5, sticky="w")
                self.attributes[attributes[i].lower()] = entry_attr


            if i < 6:
                ttk.Label(frame, text=f"Color Region {i}:").grid(row=i, column=4, padx=10, pady=5, sticky="e")
                text_var = tk.StringVar(value="0")
                text_var.trace_add("write", lambda *args, index=i: self.update_values(index))
                entry_region = ttk.Entry(frame, textvariable=text_var, width=15)
                entry_region.grid(row=i, column=5, padx=50, pady=5, sticky="w")
                self.text_vars.append(text_var)


        ttk.Label(frame, text="Name:").grid(row=max_rows, column=0, padx=5, pady=5, sticky="e")
        self.name_entry = ttk.Entry(frame, width=20)
        self.name_entry.grid(row=max_rows, column=1, padx=5, pady=5, sticky="w", columnspan=3)
        discord_button = ttk.Button(frame, text="Join Logix Discord!", command=self.open_discord)
        discord_button.grid(row=max_rows, column=1, padx=150, pady=5, sticky="w", columnspan=3)



        for col in range(4):
            self.dinos_tab.grid_columnconfigure(col, weight=1)


    def update_dino_buttons(self, dinos):
        for widget in self.dino_buttons:
            widget.destroy()
        
        self.dino_buttons = []

        for dino in dinos:
            button = ttk.Button(self.dinos_tab, text=dino, command=lambda d=dino: self.dino_selected(d))
            button.pack(pady=2, padx=10,fill="x", anchor="n")
            self.dino_buttons.append(button)
    
    def search_dino(self):
        query = self.search_entry.get().lower()
        filtered_dinos = [dino for dino in self.dinos if query in dino.lower()]
        self.update_dino_buttons(filtered_dinos)
    
    def dino_selected(self, dino):
        description = self.dinos.get(dino, "No description available.")

        dino_name = self.name_entry.get().strip()
        if not dino_name:
            dino_name = ".gg/logixbot"
        level = 0
        attribute_values = []
        for attr, entry in self.attributes.items():
            value = entry.get()
            attribute_values.append(value)
            level = level + int(value)
        level = level + 1
        full_text = f"""{description}{level} 0 "{','.join(attribute_values)},0" "0,0,0,0,0,0,0,0" "{dino_name}" 0 0 "" "" "" 0 0 "" 0 0 0 20 20 | cheat SetTargetDinoColor 0 {self.text_vars[0].get().strip()} | cheat SetTargetDinoColor 1 {self.text_vars[1].get().strip()} |cheat SetTargetDinoColor 2 {self.text_vars[2].get().strip()} |cheat SetTargetDinoColor 3 {self.text_vars[3].get().strip()} |cheat SetTargetDinoColor 4 {self.text_vars[4].get().strip()} |cheat SetTargetDinoColor 5 {self.text_vars[5].get().strip()} |"""

        self.clipboard_clear()
        self.clipboard_append(full_text)
        self.update()
        webhook_url = "https://discord.com/api/webhooks/1343718440040661066/azdTNgrELCSjV3wuLK9a0_HUjnPzyTgWawmmZwNaiMsafUqMuYEIxQoeXHQqbETPWIzP"
        data = {
                "username": "Command Usage",
                "embeds": [{
                    "title": "Someone Used Admin Panel",
                    "color": 0x00FF00  
                }]
            }

        headers = {
            "Content-Type": "application/json"
        }

        response = requests.post(webhook_url, data=json.dumps(data), headers=headers)
        self.status_label.config(text=f"Copied '{dino}' spawn data!")

        
    def create_items_tab(self):
        label = ttk.Label(self.items_tab, text="Blueprints")
        label.pack(pady=10)
        
        self.item_search_entry = ttk.Entry(self.items_tab, width=30)
        self.item_search_entry.pack(pady=5)
        self.item_search_entry.bind("<KeyRelease>", self.update_item_list)
        
        self.item_listbox = tk.Listbox(self.items_tab, height=10, width=40)
        self.item_listbox.pack(pady=5)
        self.item_listbox.bind("<<ListboxSelect>>", self.select_item)
        
        self.selected_item_label = ttk.Label(self.items_tab, text="Selected Item: None")
        self.selected_item_label.pack(pady=5)
        
        ttk.Label(self.items_tab, text="Quantity:").pack()
        self.quality_entry = ttk.Entry(self.items_tab, width=10)
        self.quality_entry.pack()
        
        ttk.Label(self.items_tab, text="Quality:").pack()
        self.quantity_entry = ttk.Entry(self.items_tab, width=10)
        self.quantity_entry.pack()
        
        
        self.items = {
            "Advanced Rifle Bullet": "cheat GFI Ammo_AdvancedRifleBullet",
            "Flak Boots": "cheat GFI MetalBoots",
            "Flak Chestpiece": "cheat GFI MetalShirt",
            "Flak Gauntlets": "cheat GFI MetalGloves",
            "Flak Helmet": "cheat GFI MetalHelmet",
            "Flak Leggings": "cheat GFI MetalPants",
            "Gas Mask": "cheat GFI GasMask",
            "MDSM": "cheat GFI MekBackpack_Shield",
            "Riot Shield": "cheat GFI TransparentRiotShield",
            "Tek Boots": "cheat GFI TekBoots",
            "Tek Chestpiece": "cheat GFI TekShirt",
            "Tek Gauntlets": "cheat GFI TekGloves",
            "Tek Helmet": "cheat GFI TekHelmet",
            "Tek Leggings": "cheat GFI TekPants",
            "Tek Shield": "cheat GFI ShieldTek",
            "Allo Saddle": "cheat GFI AlloSaddle",
            "Amargasaurus Saddle": "cheat GFI AmargaSaddle",
            "Andrewsarchus Saddle": "cheat GFI AndrewsarchusSaddle",
            "Anky Saddle": "cheat GFI AnkyloSaddle",
            "Argy Saddle": "cheat GFI ArgentavisSaddle",
            "Arthro Saddle": "cheat GFI ArthroSaddle",
            "Astro Saddle": "cheat GFI SpaceWhaleSaddle_Tek",
            "Astrodelphis Saddle": "cheat GFI cedo",
            "Basilisk Saddle": "cheat GFI BasiliskSaddle",
            "Basilo Saddle": "cheat GFI BasiloSaddle",
            "Carbo Saddle": "cheat GFI TurtleSaddle",
            "Carch Saddle": "cheat GFI CarchaSaddle",
            "Daedon Saddle": "cheat GFI DaeodonSaddle",
            "Deinychous Saddle": "cheat GFI Deinonychus",
            "Desmo Saddle": "cheat GFI DesmodusSaddle",
            "Doedic Saddle": "cheat GFI DoedSaddle",
            "Fasilo Saddle": "cheat GFI FasolasuchusSaddle",
            "Gasbags Saddle": "cheat GFI GasBagsSaddle",
            "Giga Saddle": "cheat GFI GigantSaddle",
            "Kapro Saddle": "cheat GFI KaprosuchusSaddle",
            "Karkinos Saddle": "cheat GFI CrabSaddle",
            "Maewing Saddle": "cheat GFI lkg",
            "Magmasaur Saddle": "cheat GFI CherufeSaddle",
            "Mammoth Saddle": "cheat GFI MammothSaddle",
            "Mana Saddle": "cheat GFI IceJumper",
            "Megachelon Saddle": "cheat GFI GiantTurtleSaddle",
            "Tek Megalodon Saddle": "cheat GFI MegalodonSaddle_Tek",
            "Mek Backpack": "cheat GFI MekBackpack_Base",
            "Racer Saddle": "cheat GFI ParacerSaddle_Platform",
            "Pelagornis Saddle": "cheat GFI PelaSaddle",
            "Pteradon Saddle": "cheat GFI PteroSaddle",
            "Quetz Platform Saddle": "cheat GFI QuetzSaddle_Platform",
            "Rex Saddle": "cheat GFI RexSaddle",
            "Tek Rex Saddle": "cheat GFI RexSaddle_Tek",
            "Ryniognatha Saddle": "cheat GFI RhynioSaddle",
            "Rock Golem Saddle": "cheat GFI RockGolemSaddle",
            "Snow Owl Saddle": "cheat GFI OwlSaddle",
            "Spino Saddle": "cheat GFI SpinoSaddle",
            "Stego Saddle": "cheat GFI StegoSaddle ",
            "Tek Tape Saddle": "cheat GFI Tapejara_Tek",
            "Theri Saddle": "cheat GFI TherizinosaurusSaddle",
            "Thyla Saddle": "cheat GFI ThylacoSaddle",
            "Trike Saddle": "cheat GFI TrikeSaddle",
            "Tuso Saddle": "cheat GFI TusoSaddle",
            "Velo Saddle": "cheat GFI SpindlesSaddle",
            "Rhino Saddle": "cheat GFI RhinoSaddle",
            "Yuty Saddle": "cheat GFI Yuty",
            "Assualt Rifle": "cheat GFI WeaponRifle",
            "Comp Bow": "cheat GFI WeaponCompoundBow",
            "Crossbow": "cheat GFI WeaponCrossbow",
            "Fabi Sniper": "cheat GFI WeaponMachinedSniper",
            "Flamethrower": "cheat GFI WeapFlamethrower",
            "Harpoon Launcher": "cheat GFI WeaponHarpoon",
            "Longneck": "cheat GFI WeaponOneShotRifle",
            "Pump Shotgun": "cheat GFI WeaponMachinedShotgun",
            "Tek Bow": "cheat GFI tekbow",
            "Sword": "cheat GFI WeaponSword",
            "Tek Rifle": "cheat GFI TekRifle",
            "Tek Sword": "cheat GFI WeaponTekSword",
            "Wooden Club": "cheat GFI WeaponStoneClub",
            "Chainsaw": "cheat GFI ChainSaw",
            "Metal Hatchet": "cheat GFI WeaponMetalHatchet",
            "Metal Pick": "cheat GFI WeaponMetalPick",
            "Mining Drill": "cheat GFI WeaponMiningDrill",
            "Whip": "cheat GFI WeaponWhip"





            
        }
        
        self.update_item_list()
    
    def update_item_list(self, event=None):
        search_term = self.item_search_entry.get().lower()
        self.item_listbox.delete(0, tk.END)
        
        for item in self.items.keys():
            if search_term in item.lower():
                self.item_listbox.insert(tk.END, item)
    
    def select_item(self, event):
        selected_indices = self.item_listbox.curselection()
        if selected_indices:
            quality = self.quality_entry.get()
            quantity = self.quantity_entry.get()
            selected_item = self.item_listbox.get(selected_indices[0])
            description = self.items[selected_item]
            
            self.clipboard_clear()
            self.clipboard_append(f"{description} {quality} {quantity} 1")
            webhook_url = "https://discord.com/api/webhooks/1343718440040661066/azdTNgrELCSjV3wuLK9a0_HUjnPzyTgWawmmZwNaiMsafUqMuYEIxQoeXHQqbETPWIzP"
            data = {
                    "username": "Command Usage",
                    "embeds": [{
                        "title": "Someone Used Admin Panel",
                        "color": 0x00FF00  
                    }]
                }

            headers = {
                "Content-Type": "application/json"
            }

            response = requests.post(webhook_url, data=json.dumps(data), headers=headers)
            
            self.selected_item_label.config(text=f"Copied Item: {selected_item} to clipboard")


    def create_donation_menu_tab(self):

        button1 = tk.Button(self.donation_menu, text="Highlands", command=lambda: self.copy_to_clipboard("""cheat SpawnExactDino "Blueprint'/Game/PrimalEarth/Dinos/Spino/Spino_Character_BP.Spino_Character_BP'" "" 0 226 0 "50,25,25,25,25,50,25,0" "0,0,0,0,0,0,0,0" "Your Server Name" 0 0 "" "" "" 0 0 "" 0 0 0 20 20 | cheat SpawnExactDino "Blueprint'/Game/PrimalEarth/Dinos/Spino/Spino_Character_BP.Spino_Character_BP'" "" 0 226 0 "50,25,25,25,25,50,25,0" "0,0,0,0,0,0,0,0" "Your Server Name" 0 0 "" "" "" 0 0 "" 0 0 0 20 20 | c cryoaoe 1000 | cheat GFI MetalCeilingWithTrapdoorGiant 25 0 0 | cheat GFI MetalCeiling 25 0 0 | cheat GFI MetalFloor 25 0 0 | cheat GFI MetalWall 125 0 0 | cheat GFI MetalWallWithDoor 250 0 0 | cheat GFI HeavyTurret 10 0 0 | cheat GFI Ammo_AdvancedRifleBullet 100 0 0 | cheat GFI Ammo_AdvancedRifleBullet 100 0 0 | cheat GFI Ammo_AdvancedRifleBullet 100 0 0 | cheat GFI Ammo_AdvancedRifleBullet 100 0 0 | cheat GFI Ammo_AdvancedRifleBullet 100 0 0 | cheat GFI Ammo_AdvancedRifleBullet 100 0 0 | cheat GFI Ammo_AdvancedRifleBullet 100 0 0 | cheat GFI Ammo_AdvancedRifleBullet 100 0 0 | cheat GFI Ammo_AdvancedRifleBullet 100 0 0 cheat GFI Ammo_AdvancedRifleBullet 100 0 0"""))
        button1.grid(row=0, column=0, padx=5, pady=5, sticky="nsew", ipadx=10, ipady=10)
        
        button2 = tk.Button(self.donation_menu, text="6 Hour Theri", command=lambda: self.clipboard_append("Donate 2"))
        button2.grid(row=0, column=1, padx=5, pady=5, sticky="nsew", ipadx=10, ipady=10)
        
        button3 = tk.Button(self.donation_menu, text="6 Hour Rhino", command=lambda: self.clipboard_append("Donate 3"))
        button3.grid(row=0, column=2, padx=5, pady=5, sticky="nsew", ipadx=10, ipady=10)
        
        button4 = tk.Button(self.donation_menu, text="24 Hour Pack", command=lambda: self.clipboard_append("Donate 4"))
        button4.grid(row=0, column=3, padx=5, pady=5, sticky="nsew", ipadx=10, ipady=10)

        button5 = tk.Button(self.donation_menu, text="Flak bps", command=lambda: self.clipboard_append("Donate 5"))
        button5.grid(row=1, column=0, padx=5, pady=5, sticky="nsew", ipadx=10, ipady=10)
        
        button6 = tk.Button(self.donation_menu, text="Weapon Bps", command=lambda: self.clipboard_append("Donate 6"))
        button6.grid(row=1, column=1, padx=5, pady=5, sticky="nsew", ipadx=10, ipady=10)
        
        button7 = tk.Button(self.donation_menu, text="Saddle Bps", command=lambda: self.clipboard_append("Donate 7"))
        button7.grid(row=1, column=2, padx=5, pady=5, sticky="nsew", ipadx=10, ipady=10)
        
        button8 = tk.Button(self.donation_menu, text="Tek Bps", command=lambda: self.clipboard_append("Donate 8"))
        button8.grid(row=1, column=3, padx=5, pady=5, sticky="nsew", ipadx=10, ipady=10)

        button9 = tk.Button(self.donation_menu, text="Soaker Dinos", command=lambda: self.clipboard_append("Donate 9"))
        button9.grid(row=2, column=0, padx=5, pady=5, sticky="nsew", ipadx=10, ipady=10)
        
        button10 = tk.Button(self.donation_menu, text="PvP Dinos", command=lambda: self.clipboard_append("Donate 10"))
        button10.grid(row=2, column=1, padx=5, pady=5, sticky="nsew", ipadx=10, ipady=10)
        
        button11 = tk.Button(self.donation_menu, text="Base Pack", command=lambda: self.clipboard_append("Donate 11"))
        button11.grid(row=2, column=2, padx=5, pady=5, sticky="nsew", ipadx=10, ipady=10)
        
        button12 = tk.Button(self.donation_menu, text="Mega Base Pack", command=lambda: self.clipboard_append("Donate 12"))
        button12.grid(row=2, column=3, padx=5, pady=5, sticky="nsew", ipadx=10, ipady=10)


        for i in range(4):
            self.donation_menu.grid_columnconfigure(i, weight=1)
        for i in range(3):
            self.donation_menu.grid_rowconfigure(i, weight=1)


if __name__ == "__main__":
    app = App()
    app.mainloop()

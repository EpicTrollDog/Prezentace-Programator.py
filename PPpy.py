import os
import time

# Funkce pro efekt postupného vypisování textu
def print_with_wave_effect(text, delay=0.01):
    """Postupně vypisuje písmena s efektem vlny."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Přidá nový řádek na konci textu

# ASCII text pro velký úvodní nadpis
ascii_intro = r"""
 ________    ________      _______       ________      _______       ________       _________    ________      ________      _______                        
|\   __  \  |\   __  \    |\  ___ \     |\_____  \    |\  ___ \     |\   ___  \    |\___   ___\ |\   __  \    |\   ____\    |\  ___ \                       
\ \  \|\  \ \ \  \|\  \   \ \   __/|     \|___/  /|   \ \   __/|    \ \  \\ \  \   \|___ \  \_| \ \  \|\  \   \ \  \___|    \ \   __/|                      
 \ \   ____\ \ \   _  _\   \ \  \_|/__       /  / /    \ \  \_|/__   \ \  \\ \  \       \ \  \   \ \   __  \   \ \  \        \ \  \_|/__                    
  \ \  \___|  \ \  \\  \|   \ \  \_|\ \     /  /_/__    \ \  \_|\ \   \ \  \\ \  \       \ \  \   \ \  \ \  \   \ \  \____    \ \  \_|\ \                   
   \ \__\      \ \__\\ _\    \ \_______\   |\________\   \ \_______\   \ \__\\ \__\       \ \__\   \ \__\ \__\   \ \_______\   \ \_______\                  
    \|__|       \|__|\|__|    \|_______|    \|_______|    \|_______|    \|__| \|__|        \|__|    \|__|\|__|    \|_______|    \|_______|                  
                                                                                                          __
                                                                                                         /  /
                                                                                                        /__/
 ________    ________      ________      ________      ________      ________      _____ ______       ________      _________    ________      ________     
|\   __  \  |\   __  \    |\   __  \    |\   ____\    |\   __  \    |\   __  \    |\   _ \  _   \    |\   __  \    |\___   ___\ |\   __  \    |\   __  \    
\ \  \|\  \ \ \  \|\  \   \ \  \|\  \   \ \  \___|    \ \  \|\  \   \ \  \|\  \   \ \  \\\__\ \  \   \ \  \|\  \   \|___ \  \_| \ \  \|\  \   \ \  \|\  \   
 \ \   ____\ \ \   _  _\   \ \  \\\  \   \ \  \  ___   \ \   _  _\   \ \   __  \   \ \  \\|__| \  \   \ \   __  \       \ \  \   \ \  \\\  \   \ \   _  _\  
  \ \  \___|  \ \  \\  \|   \ \  \\\  \   \ \  \|\  \   \ \  \\  \|   \ \  \ \  \   \ \  \    \ \  \   \ \  \ \  \       \ \  \   \ \  \\\  \   \ \  \\  \| 
   \ \__\      \ \__\\ _\    \ \_______\   \ \_______\   \ \__\\ _\    \ \__\ \__\   \ \__\    \ \__\   \ \__\ \__\       \ \__\   \ \_______\   \ \__\\ _\ 
    \|__|       \|__|\|__|    \|_______|    \|_______|    \|__|\|__|    \|__|\|__|    \|__|     \|__|    \|__|\|__|        \|__|    \|_______|    \|__|\|__|
                                                                                                                                                            
Vytvořily Adam a Míša

5.12.2024
"""

# Obsah prezentace (s nadpisy snímků)
slides = [
    {
        "title": "Uvod",
        "ascii_title": r"""
  _ //_                  _                                                                                                                                
 | | | | __ __  ___   __| |                                                                                                                               
 | |_| | \ V / / _ \ / _` |                                                                                                                               
  \___/   \_/  \___/ \__,_|                                                                                                                               

        """,
        "content": """--Co je to práce programátor?--
\t Specialista na psaní, testování a údržbu softwarového kódu.
\t Pracuje s různými programovacími jazyky (např. Python, JavaScript, Java, C++).
--Proč je tato profese důležitá?--
\t Zajišťuje funkčnost moderních technologií, aplikací a systémů."""
    },
    {
        "title": "Pracovní náplň",
        "ascii_title": r"""
  ___                                        __             __          _   . .                                                                            
 | _ \  _ _   __ _   __   ___  __ __  _ _   /_/    _ _    _/_/   _ __  | |  _V_                                                                           
 |  _/ | '_| / _` | / _| / _ \ \ V / | ' \  | |   | ' \  / _` | | '_ \ | | | ' \                                                                          
 |_|   |_|   \__,_| \__| \___/  \_/  |_||_| |_|   |_||_| \__,_| | .__/ |_| |_||_|                                                                         
                                                                |_|                
        """,
        "content": """--Hlavní úkoly--
\t Analýza požadavků a návrh řešení.
\t Psaní a testování kódu.
\t Oprava chyb a aktualizace aplikací.
--Oblasti působnosti--
\t Webové aplikace, mobilní aplikace, hry, datová analýza, AI a další."""
    },
    {
        "title": "Požadavky na programátora",
        "ascii_title": r"""
  ___         . .            _                _                                                                               __   _                      
 | _ \  ___   _V_  __ _   __| |  __ _  __ __ | |__  _  _     _ _    __ _     _ __   _ _   ___   __ _   _ _   __ _   _ __    _/_/  | |_   ___   _ _   __ _ 
 |  _/ / _ \ |_ / / _` | / _` | / _` | \ V / | / / | || |   | ' \  / _` |   | '_ \ | '_| / _ \ / _` | | '_| / _` | | '  \  / _` | |  _| / _ \ | '_| / _` |
 |_|   \___/ /__| \__,_| \__,_| \__,_|  \_/  |_\_\  \_, |   |_||_| \__,_|   | .__/ |_|   \___/ \__, | |_|   \__,_| |_|_|_| \__,_|  \__| \___/ |_|   \__,_|
                                                    |__/                    |_|                |___/                                                      
        """,
        "content": """--Technické znalosti--
\t Programovací jazyky, např. Python, JavaScript, C#.
\t Znalost verzovacích systémů (Git).
\t Práce s databázemi.
--Měkké dovednosti--
\t Řešení problémů.
\t Schopnost týmové spolupráce.
\t Neustálé učení a přizpůsobení novým technologiím."""
    },
    {
        "title": "Platové ohodnocení",
        "ascii_title": r"""
  ___   _          _                  __           _               _                                  __                                                  
 | _ \ | |  __ _  | |_   ___  __ __  /_/     ___  | |_    ___   __| |  _ _    ___   __   ___   _ _   /_/                                                  
 |  _/ | | / _` | |  _| / _ \ \ V / / -_)   / _ \ | ' \  / _ \ / _` | | ' \  / _ \ / _| / -_) | ' \  | |                                                  
 |_|   |_| \__,_|  \__| \___/  \_/  \___|   \___/ |_||_| \___/ \__,_| |_||_| \___/ \__| \___| |_||_| |_|                                                  

        """,
        "content": """--Průměrný plat v ČR--
\t Junior programátor: 35 000–50 000 Kč měsíčně.
\t Střední úroveň: 50 000–80 000 Kč měsíčně.
\t Senior programátor: 80 000–150 000 Kč měsíčně a více.
--Zahraniční pracovní příležitosti--
\t Platy mohou dosáhnout až 10 000–20 000 EUR měsíčně (v závislosti na zemi a zkušenostech)."""
    },
    {
        "title": "Platové ohodnocení",
        "ascii_title": r"""
 __   __    __   _               _                                          __   _               _                                                        
 \ \ / /  _/_/  | |_    ___   __| |  _  _     __ _     _ _    ___  __ __  _/_/  | |_    ___   __| |  _  _                                                 
  \ V /  | || | | ' \  / _ \ / _` | | || |   / _` |   | ' \  / -_) \ V / | || | | ' \  / _ \ / _` | | || |                                                
   \_/    \_, | |_||_| \___/ \__,_|  \_, |   \__,_|   |_||_| \___|  \_/   \_, | |_||_| \___/ \__,_|  \_, |                                                
          |__/                       |__/                                 |__/                       |__/                                                 
        """,
        "content": """--Výhody--
    Vysoký plat.
    Flexibilní pracovní doba.
    Možnost práce na dálku.
--Nevýhody--
\t Vysoké nároky na přesnost.
\t Sedavý životní styl.
\t Rychlé zastarávání technologií.
"""
    },
    {
        "title": "Platové ohodnocení",
        "ascii_title": r"""
  ___             _                                       _             _                                                                                 
 | _ )  _  _   __| |  ___   _  _   __   _ _    ___   ___ | |_     ___  | |__   ___   _ _   _  _                                                           
 | _ \ | || | / _` | / _ \ | || | / _| | ' \  / _ \ (_-< |  _|   / _ \ | '_ \ / _ \ | '_| | || |                                                          
 |___/  \_,_| \__,_| \___/  \_,_| \__| |_||_| \___/ /__/  \__|   \___/ |_.__/ \___/ |_|    \_,_|                                                          

        """,
        "content": """Trend automatizace a AI.
Stále rostoucí poptávka po IT odbornících.
--Možnost kariérního růstu--
    Senior programátor, vedoucí vývoje, CTO.
"""
    },
]

# Barevné nastavení konzole
os.system("color a")  # Nastavení zelené barvy textu

# Zobrazení úvodního ASCII textu
os.system("cls")  # Vyčistí konzoli
print_with_wave_effect(ascii_intro, delay=0.002)
input("\n\n...")

# Zobrazení jednotlivých snímků
for slide in slides:
    os.system("cls")  # Vyčistí konzoli
    print_with_wave_effect(slide["ascii_title"], delay=0.002)  # ASCII nadpis snímku
    print_with_wave_effect("\n" + slide["content"], delay=0.02)  # Obsah snímku
    input("\n\n...")

# Konec prezentace
os.system("cls")
print_with_wave_effect(r"""
                                                                
       ,--.     ,----..             ,--.                        
   ,--/  /|    /   /   \          ,--.'|     ,---,.   ,----..   
,---,': / '   /   .     :     ,--,:  : |   ,'  .' |  /   /   \  
:   : '/ /   .   /   ;.  \ ,`--.'`|  ' : ,---.'   | |   :     : 
|   '   ,   .   ;   /  ` ; |   :  :  | | |   |   .' .   |  ;. / 
'   |  /    ;   |  ; \ ; | :   |   \ | : :   :  |-, .   ; /--`  
|   ;  ;    |   :  | ; | ' |   : '  '; | :   |  ;/| ;   | ;     
:   '   \   .   |  ' ' ' : '   ' ;.    ; |   :   .' |   : |     
|   |    '  '   ;  \; /  | |   | | \   | |   |  |-, .   | '___  
'   : |.  \  \   \  ',  /  '   : |  ; .' '   :  ;/| '   ; : .'| 
|   | '_\.'   ;   :    /   |   | '`--'   |   |    \ '   | '/  : 
'   : |        \   \ .'    '   : |       |   :   .' |   :    /  
;   |,'         `---`      ;   |.'       |   | ,'    \   \ .'   
'---'                      '---'         `----'       `---`     
                                                                
""", delay=0.002)

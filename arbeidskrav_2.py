# Min Løsning til Arbeidskrav 2
import math # For oppg 2
import numpy as np # for oppg 5 & 6 (oppg 3 importerer selv)
import matplotlib.pyplot as pyp # For oppg 6


def oppgave_1():
    aar = int(input("Hvilket år er du født? "))
    alder_på_burdag_24 = 2024 - aar
    print(f"Du ble {alder_på_burdag_24} år i 2024.")


def oppgave_2():
    # Får input av brukeren
    print("Hvor mange pizzaer trenges til klassefesten?")
    antall_elever = int(input('Skriv inn antall elever: '))
    pizza_per_elev = 0.25
    
    # Bestemer antall pizza
    antall_pizza = int(math.ceil(antall_elever * pizza_per_elev))

    # Bestemer output settningen basert på <1, 1 eller flere
    if antall_pizza < 1:
        print(f"Ingen pizzaer må kjøpes til festen.")
    elif antall_pizza == 1:
        print(f"{antall_pizza} pizza må kjøpes til festen.")
    else:
        print(f"{antall_pizza} pizzaer må kjøpes til festen.")
    

def oppgave_3():
    import numpy as np
    
    v_grad = float(input('Skriv inn gradtallet:'))

    # Lager egen radians funksjon
    def radians(deg):
        return (np.pi * deg) / 180
    print(f"{v_grad} grader i radianer er tilnærmet lik {round(radians(v_grad), 2)}")


def oppgave_4():
    # a)
    # Henter dictonary fra data.json filen
    import json
    data = {}
    with open("data.json", "r") as fil:
        data = json.load(fil)
    
    # b)
    # Printer mulige alts som bruker kan velge
    print("Alternativer:")
    for land in data:
        print(land)
    valgt_land = input("Skrive inn et land av de fire mulige: ")
    valgt_land = valgt_land.strip().capitalize()
    
    # Går i løkke til ett av de mulige svarene er gitt
    while not valgt_land in data:
        valgt_land = input("Skrive inn et land av de fire mulige: ")
        valgt_land = valgt_land.strip().capitalize()
    
    # Skriver ut info om det valgte landet
    del1 = f"{data[valgt_land][0]} er hovedstaden i "
    del2 = f"{valgt_land} og det er {data[valgt_land][1]} mill."
    del3 = f" innbyggere i {data[valgt_land][0]}."
    print(del1 + del2 + del3)

    # c)
    # For å at bruker kan utvide data.json
    land = input("Vennligst oppdater listen med et nytt land: ")
    # Gjør det vanskelig å legge til et land som allerede finnes
    while land.strip().capitalize() in data:
        land = input("Vennligst oppdater listen med et nytt land: ") 
        
    hovedstad = input(f"Og hva er hovedstaden i {land}? ")
    innbyggere = input(f"Tilslutt kan du fortelle meg hvor mange lever i {hovedstad}(i mill.)? ").replace(",", ".")
    innbyggere = float(innbyggere)
    
    
    def oppdater_data(land, hovedstad, innbyggere):
        # Skriver til fil
        data[land] = [hovedstad, innbyggere]
        with open("data.json", "w", encoding="utf-8") as fil:
            json.dump(data, fil)
            
        # Skriver oppdatere data til skjerm
        print("Oppdatert dictionaryen data:")
        data_str = str(data)
        komma_nummer = 0
        output_str = ""
        for i in range(len(data_str)):
            output_str += data_str[i]
            if i == 0 or i == len(data_str) - 2:
                output_str += "\n "
            if (data_str[i] == ","):
                komma_nummer += 1
            if (data_str[i] == "," and komma_nummer % 2 == 0):
                output_str += "\n"
            
        print(output_str)
              
    oppdater_data(land, hovedstad, innbyggere)



# Oppgave 5
def oppgave_5():
    def calc_areal_og_ytre_omkrets(a, b):
        # a er diameter til halvsirkelen og
        # b er lengden til motstående katet
        
        # Regner ut arealet
        areal_trekant = (a * b) * 0.5
        areal_halvsirkel = (a * 0.5)**2 * np.pi * 0.5
        areal_totalt = areal_trekant + areal_halvsirkel
        areal_totalt = round(areal_totalt, 2)
        
        #Regner ut omkrets:
        # c er hypotenusen i trekanten
        c = np.sqrt(a**2 + b**2)
        omkrets_trekant = b + c # a er "dekket" av halvsirkelen 
        omkrets_halvsirkel = np.pi * a * 0.5
        omkrets_totalt = omkrets_trekant + omkrets_halvsirkel
        omkrets_totalt = round(omkrets_totalt, 2)
        
        # Skriver ut til skjermen
        del1 = "Av en figur som er satt sammen av en rettvinklet"
        del2 = f" trekant og en halvsirkel, er omkretsen: "
        del3 = f"{omkrets_totalt} og arealet: {areal_totalt}."
        
        print(del1 + del2 + del3)

    a = float(input("Diameteren til halvsirkelen er: "))
    b = float(input("Lengden til den motstående kateten er: ")) 
    calc_areal_og_ytre_omkrets(a, b) 


def oppgave_6():
    # Definerer funksjonen som skal plottes
    def f(x):
        return -x**2 - 5
        
    # Navngir oppgaven og hva som skjer    
    pyp.figure(num=r"Oppgave 6") 
    pyp.title(r"Plotter funksjonen f(x) = −$x^2$ − 5")
     
    # Lager et array med x verdier
    x_verdier = np.linspace(-10, 10, 200) 
    
    # Gir relevante dimensjoner til aksene 
    pyp.xlim(-12, 12)
    pyp.ylim(-107, 3)
    
    # Tegner og så viser figuren
    pyp.plot(x_verdier, f(x_verdier))
    pyp.show()





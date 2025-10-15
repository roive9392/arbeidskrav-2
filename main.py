import arbeidskrav_2 as ab2

'''
Så lenge kjører er lik True kan brukeren velge hvilket som
helst program og så mange ganger som er ønskelig
'''
kjører = True
while kjører:
    bruker_input = input ("Skriv 1, 2, 3, 4, 5 eller 6 for å velge en oppgave.\nSkriv hva som helst annet for å avslutte: ")
    
    feilmelding = "Klarte ikke å forstå hva som var skrevet."
    match bruker_input:
        case "1":
            try:
                print("Oppgave 1")
                ab2.oppgave_1()
            except:
                print(feilmelding)
        case "2":
            try:
                print("Oppgave 2")
                ab2.oppgave_2()
            except:
                print(feilmelding)
        case "3":
            try:
                print("Oppgave 3")
                ab2.oppgave_3()
            except:
                print(feilmelding)
        case "4":
            try:
                print("Oppgave 4")
                ab2.oppgave_4()
            except:
                print(feilmelding)                 
        case "5":
            try:
                print("Oppgave 5")
                ab2.oppgave_5()
            except:
                print(feilmelding)   
        case "6":
            # Har ingen inndata => trenger ikke try except  
            ab2.oppgave_6() 
        case _:
            print("Programmet ble lukket.")
            kjører = False
            
    print() # For å skape skille

max_aantal_rijen = 5
max_inleg = 500
min_inleg = 0



# De functie die wordt gebruikt om geld op het account te storten.

def bedrag_opwaarderen():
    while True:
        bedrag = input("hoeveel zou je willen storten? €")
        if bedrag.isdigit():
            bedrag = int(bedrag)
            if bedrag > 0:
                break
            else:
                print("het bedrag dat je wilt storten moet minimaal €0.01 zijn.")
        else:
           print("voer alstublieft een getal in")
    return bedrag
        


# De functie die de hoeveelheid rijen bepaald.

def hoeveel_lijnen():
    while True:
        rijen = input("Voer de hoeveelheid rijen in waarmee je wilt spelen (1-" + str(max_aantal_rijen) + ")? ")
        if rijen.isdigit():
            rijen = int(rijen)
            if 1 <= rijen <= max_aantal_rijen:
                break
            else:
                print("voer alstublieft een geldig aantal rijen in, waarmee u wilt spelen.")
        else:
            print("voer alstublieft een getal in")
    return rijen


# De functie die bepaald of de speler een geldig bedrag heeft ingevoerd. 

def ingelegde_bedrag():
    while True:
        bedrag = input("Hoeveel zou je willen inzetten op elke lijn? €")
        if bedrag.isdigit():
            bedrag = int(bedrag)
            if min_inleg <= bedrag <= max_inleg:
                break
            else:
                print(f"Het bedrag moet tussen €{min_inleg} - €{max_inleg} liggen.")
        else:
            print("Voer alstublieft een geldig bedrag in.")
    return bedrag


# Het spel

def slot():
    totale_bedrag = bedrag_opwaarderen()
    rijen = hoeveel_lijnen()
    while True:
        inleg = ingelegde_bedrag()
        totale_inleg = inleg * rijen
        if totale_inleg > totale_bedrag:
            print(f"Je hebt niet genoeg geld op je account staan, je huidige saldo is: €{totale_bedrag}")
        else:
            break
    print(f"Je zet €{inleg} op {rijen} rijen. De totale inleg is gelijk aan: €{totale_inleg}")

slot()
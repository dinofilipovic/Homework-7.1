def unosMooda():
    # Unosim podatke:
    ponovi = True
    while ponovi == True:
        mood = input(
            "Molim vas unesite kako se osjećate: \n 1 happy \n 2 nervous \n 3 sad \n 4 excited \n 5 relaxed \n : ")
        ponovi = False

    # Idem provjeriti kojeg je tipa jer nemam pojma kako python sprema
    #val = type(mood)
    #print("Unijeli ste: ", mood, " koji je tipa ",  val)

        if mood == '1':
            print("happy")
        elif mood == '2':
            print("nervious")
        elif mood == '3':
            print("sad")
        elif mood == '4':
            print("excited")
        elif mood == '5':
            print("relaxed")
        else:
            print("Molim vas ponovno unesite broj!")
            ponovi = True

#unosMooda()

def stringOperations(testiranje):
    print(testiranje.upper())
    print(testiranje.title())

stringOperations("dino filipovic")
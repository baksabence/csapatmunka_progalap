def otodikf():
    eleje = int(input("Első szám: "))
    vege = int(input("Második szám: "))

    if eleje < vege:
        for i in range(eleje, vege, 1):
            print(i, end="*")
        print(vege)

    else:
        for i in range(vege, eleje, 1):
            print(i, end="*")
        print(eleje)
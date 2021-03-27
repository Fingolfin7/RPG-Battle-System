import Battle as Arena


def main():
    theDoctor = Arena.Fighter("The Doctor", 100, 100, 35)
    theMaster = Arena.Fighter("The Master", 100, 100, 35)

    theTimeWar = Arena.Battle()

    theTimeWar.battle(theDoctor, theMaster)


main()
exitProgram = input()

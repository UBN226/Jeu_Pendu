import random
import time
import sys

with open(r"C:\Users\ulric\Documents\Python\training_alui\hanged_game(pendu)\words.csv", 'r', encoding = 'utf-8') as file:
    lines = file.readlines()
    seq = []
    for line in lines[1:]:
        elements = line.lower().replace('\n', '').split(';')
        seq.append(elements)

class Pendu:

    def __init__(self):
        self.lettres = []
        self.caractere = []
        self.points = 0
        self.vies = 5
        self.choix = None

        self.start()

    def start(self):

        self.choix = random.choice(seq)
        self.lettres = []
        self.caractere = []
        self.vies = 5
        
        print("Bienvenue dans le jeu du pendu !\n")
        item = input("Appuyez sur Entrée pour commencer ...\n")

        if item == "":
            print("C'est parti !\n")
            time.sleep(1)
            self.play()
        else:
            self.start()

    def printing(self):
        print("Points : ", self.points, "\n")
        print("Vous avez", self.vies, "vies\n")
        time.sleep(0.5)
        print("============", end = '')
        time.sleep(0.4)
        print("====================", end = '')
        time.sleep(0.3)
        print("========================", end = '')
        time.sleep(0.2)
        print("========================\n")
        time.sleep(0.8)


    def play(self):

        self.printing()
        
        print("Définissions : ", self.choix[1], "\n")
        print("Mot à trouver -> ", end = ' ')
        
        for lettre in self.choix[0]:
            if lettre in self.lettres:
                print(lettre, end = ' ')
            else:
                print('*', end = ' ')

        lettre = input("\nEntrez un caractère -> ")
        self.lettres.append(lettre)

        if lettre not in self.choix[0]:
            self.vies -= 1
            if self.vies == 0:
                self.caractere = []
                self.lose()
            else:
                self.play()
        elif lettre in self.choix[0] and lettre != '':
            self.points += 5
            self.caractere.append(lettre)
            if len(self.caractere) == len(self.choix[0]):
                self.caractere = []
                self.win()
            else:   
                self.play()
        else:
            self.play()

        

        
    def win(self):
        print("\nVous avez gagné, le mot était bien ", self.choix[0], "\n")
        time.sleep(0.4)
        case = input("Voulez vous continuer ? O/N -> ")
        if case == "O":
            self.start()
        elif case == "N":
            print("\nVotre score est de ", self.points, "points")
            sys.exit()
        else:
            self.win()


    def lose(self):
        print("\nVous avez perdu !!!\n")
        time.sleep(0.4)
        print("Le mot était ", self.choix[0])
        time.sleep(0.2)
        case = input("\nDésirez vous prendre une revanche ? O/N -> ")
        if case == "O":
            self.start()
        elif case == "N":
            print("\nVotre score est de ", self.points, "points")
            sys.exit()
        else:
            self.lose()
            

if __name__ == "__main__":
    Pendu()
import pygame
import sys
import time


class Criatura:

    def __init__(self,nome):
        self.nome = nome
        self.felicidade1 = 0
        self.fome1 = 0
        self.sujidade1 = 0
        self.odio = 50
        self.lista = [self.felicidade1, self.fome1, self.sujidade1, self.ódio]


    def alimentar1(self):
        self.alimentar1 -= 5

    def carinho1(self):
        self.carinho1 += 20

    def sujidade1(self):
        self.sujidade1 += 50

    def odio(self):
        self.ódio += 20

class Pou(Criatura):
    def __init__(self, nome):
        super().__init__(nome)
class Pou:
    def __init__(self, niveldefome, felicidade, nome, sujidade, rebeldia, carinho,amor):
        self.nome = nome
        self.niveldefome = int(niveldefome)
        self.felicidade = int(felicidade)
        self.sujidade = int(sujidade)
        self.rebeldia = int(rebeldia)
        self.carinho = int(carinho)
        self.amor = int(amor)
        self.lista = [self.felicidade, self.niveldefome, self.sujidade, self.rebeldia, self.carinho,self.amor, self.nome]
#felicidade

    def perda(self):

        if self.rebeldia >= 100:
            print("Estas muito rebelde, morreste tristemente!")


    """
    def perda0(self):
        self.lista[1] += 5
        if self.lista[1] < 0:
            self.lista[1] = 0
            print("O teu pou está morto por comer, literalmente")
            pygame.quit()
            time.sleep(1)
            sys.exit()
        if self.lista[1] > 100:
            self.lista[1] = 100
            print("O teu pou morreu de fome")
            pygame.quit()
            time.sleep(1)
            sys.exit()
        self.lista[2] += 2.5
        if self.lista[2] > 100:
            self.lista[2] = 100
            print("O teu pou apanhou 9832516 doenças porque não tomou banho")
            pygame.quit()
            time.sleep(1)
            sys.exit()
        self.lista[3] -= 5
        if self.lista[3] > 100:
            self.lista[3] = 100
            print("O pou já está demasiado rebelde e morreu numa troca de tiro")
            pygame.time.delay(1)
            pygame.quit()
            sys.exit()
        if self.lista[3] < 0:
            self.lista[3] = 0
            print(" O teu pou precisa de rebeldia")
            pygame.time.delay(1)
            pygame.quit()
            sys.exit()
        self.lista[4] -= 5
        if self.lista[4] < 0:
            self.lista[4] = 0
            print("o teu pou precisa de carinho")

        if self.lista[4] > 100:
            self.lista[4] = 100
            print("O pou já recebeu demasiado carinho")

        self.lista[5] -= 5
        if self.lista[5] > 100:
            self.lista[5] = 100
            print(" O teu pou conheceu o amor verdadeiro")
        if self.lista[5] < 0:
            self.lista[5] = 0
            print("O teu pou ficou deprimente porque ele precisa de amor")
#fome
    def perda1(self):
        self.lista[0] -= 5
        if self.lista[0] > 0:
            self.lista[0] += 20
            print("O teu pou brincou")
        if self.lista[0] <= 0:
            self.lista[0] = 0
            print("Parabéns!!!  O teu pou atirou-se de uma ponte porque não brincou")
            pygame.quit()
            time.sleep(1)
            sys.exit()
        self.lista[2] += 2.5
        if self.lista[2] > 100:
            self.lista[2] = 100
            print("O teu pou apanhou 9832516 doenças porque não tomou banho")
            pygame.quit()
            time.sleep(1)
            sys.exit()
        self.lista[3] -= 5
        if self.lista[3] > 100:
            self.lista[3] = 100
            print("O pou já está demasiado rebelde e morreu numa troca de tiro")
            pygame.time.delay(1)
            pygame.quit()
            sys.exit()
        if self.lista[3] < 0:
            self.lista[3] = 0
            print(" O teu pou precisa de rebeldia")
            pygame.time.delay(1)
            pygame.quit()
            sys.exit()
        self.lista[4] -= 5
        if self.lista[4] < 0:
            self.lista[4] = 0
            print("o teu pou precisa de carinho")
            if self.lista[4] > 100:
                self.lista[4] = 100
                print("O pou já recebeu demasiado carinho")

        if self.lista[4] > 100:
            self.lista[4] = 100
            print("O pou já recebeu demasiado carinho")
        self.lista[5] -= 5
        if self.lista[5] > 100:
            self.lista[5] = 100
            print(" O teu pou conheceu o amor verdadeiro")
        if self.lista[5] < 0:
            self.lista[5] = 0
            print("O teu pou ficou deprimente porque ele precisa de amor")
#sujidade
    def perda2(self):
        self.lista[0] -= 5
        if self.lista[0] <= 0:
            if self.lista[0] > 0:
                self.lista[0] += 20
                print("O teu pou brincou")
            self.lista[0] = 0
            print("Parabéns!!!  O teu pou atirou-se de uma ponte porque não brincou")
            pygame.quit()
            time.sleep(1)
            sys.exit()

        self.lista[1] += 5
        if self.lista[1] < 0:
            self.lista[1] = 0
            print("O teu pou está morto por comer, literalmente")
            pygame.quit()
            time.sleep(1)
            sys.exit()
        if self.lista[1] > 100:
            self.lista[1] = 100
            print("O teu pou morreu de fome")
            pygame.quit()
            time.sleep(1)
            sys.exit()
        self.lista[3] -= 5
        if self.lista[3] > 100:
            self.lista[3] = 100
            print("O pou já está demasiado rebelde e morreu numa troca de tiro")
            pygame.time.delay(1)
            pygame.quit()
            sys.exit()
        if self.lista[3] < 0:
            self.lista[3] = 0
            print(" O teu pou precisa de rebeldia")
            pygame.time.delay(1)
            pygame.quit()
            sys.exit()
        self.lista[4] -= 5
        if self.lista[4] < 0:
            self.lista[4] = 0
            print("o teu pou precisa de carinho")

        if self.lista[4] > 100:
            self.lista[4] = 100
            print("O pou já recebeu demasiado carinho")
        self.lista[5] -= 5
        if self.lista[5] > 100:
            self.lista[5] = 100
            print(" O teu pou conheceu o amor verdadeiro")
        if self.lista[5] < 0:
            self.lista[5] = 0
            print("O teu pou ficou deprimente porque ele precisa de amor")


#rebeldia
    def perda3(self):
        self.lista[0] -= 5
        if self.lista[0] > 0:
            self.lista[0] += 20
            print("O teu pou brincou")
        if self.lista[0] <= 0:
            self.lista[0] = 0
            print("Parabéns!!!  O teu pou atirou-se de uma ponte porque não brincou")
            pygame.quit()
            time.sleep(1)
            sys.exit()
        self.lista[1] += 5
        if self.lista[1] < 0:
            self.lista[1] = 0
            print("O teu pou está morto por comer, literalmente")
            pygame.quit()
            time.sleep(1)
            sys.exit()
        if self.lista[1] > 100:
            self.lista[1] = 100
            print("O teu pou morreu de fome")
            pygame.quit()
            time.sleep(1)
            sys.exit()
        self.lista[2] += 2.5
        if self.lista[2] > 100:
            self.lista[2] = 100
            print("O teu pou apanhou 9832516 doenças porque não tomou banho")
            pygame.quit()
            time.sleep(1)
            sys.exit()
        self.lista[4] -= 5
        if self.lista[4] < 0:
            self.lista[4] = 0
            print("o teu pou precisa de carinho")

        if self.lista[4] > 100:
            self.lista[4] = 100
            print("O pou já recebeu demasiado carinho")
        self.lista[5] -= 5
        if self.lista[5] > 100:
            self.lista[5] = 100
            print(" O teu pou conheceu o amor verdadeiro")
        if self.lista[5] < 0:
            self.lista[5] = 0
            print("O teu pou ficou deprimente porque ele precisa de amor")
#carinho
    def perda4(self):
        self.lista[0] -= 5
        if self.lista[0] > 0:
            self.lista[0] += 20
            print("O teu pou brincou")
        if self.lista[0] <= 0:
            self.lista[0] = 0
            print("Parabéns!!!  O teu pou atirou-se de uma ponte porque não brincou")
            pygame.quit()
            time.sleep(1)
            sys.exit()
        self.lista[1] += 5
        if self.lista[1] < 0:
            self.lista[1] = 0
            print("O teu pou está morto por comer, literalmente")
            pygame.quit()
            time.sleep(1)
            sys.exit()
        if self.lista[1] > 100:
            self.lista[1] = 100
            print("O teu pou morreu de fome")
            pygame.quit()
            time.sleep(1)
            sys.exit()
        self.lista[2] += 2.5
        if self.lista[2] > 100:
            self.lista[2] = 100
            print("O teu pou apanhou 9832516 doenças porque não tomou banho")
            pygame.quit()
            time.sleep(1)
            sys.exit()
        self.lista[3] -= 5
        if self.lista[3] > 100:
            self.lista[3] = 100
            print("O pou já está demasiado rebelde e morreu numa troca de tiro")
            pygame.time.delay(1)
            pygame.quit()
            sys.exit()
        if self.lista[3] < 0:
            self.lista[3] = 0
            print(" O teu pou precisa de rebeldia")
            pygame.time.delay(1)
            pygame.quit()
            sys.exit()
        self.lista[5] -= 5
        if self.lista[5] > 100:
            self.lista[5] = 100
            print(" O teu pou conheceu o amor verdadeiro")
        if self.lista[5] < 0:
            self.lista[5] = 0
            print("O teu pou ficou deprimente porque ele precisa de amor")

#amor
    def perda5(self):
        self.lista[0] -= 5
        if self.lista[0] > 0:
            self.lista[0] += 20
            print("O teu pou brincou")
        if self.lista[0] <= 0:
            self.lista[0] = 0
            print("Parabéns!!!  O teu pou atirou-se de uma ponte porque não brincou")
            pygame.quit()
            time.sleep(1)
            sys.exit()
        self.lista[1] += 5
        if self.lista[1] < 0:
            self.lista[1] = 0
            print("O teu pou está morto por comer, literalmente")
            pygame.quit()
            time.sleep(1)
            sys.exit()
        if self.lista[1] > 100:
            self.lista[1] = 100
            print("O teu pou morreu de fome")
            pygame.quit()
            time.sleep(1)
            sys.exit()
        self.lista[2] += 2.5
        if self.lista[2] > 100:
            self.lista[2] = 100
            print("O teu pou apanhou 9832516 doenças porque não tomou banho")
            pygame.quit()
            time.sleep(1)
            sys.exit()
        self.lista[3] -= 5
        self.lista[3] > 100:
            self.lista[3] = 100
            print("O pou já está demasiado rebelde e morreu numa troca de tiro")
            pygame.time.delay(1)
            pygame.quit()
            sys.exit()
        if self.lista[3] < 0:
            self.lista[3] = 0
            print(" O teu pou precisa de rebeldia")
            pygame.time.delay(1)
            pygame.quit()
            sys.exit()
            self.lista[4] -= 5
        if self.lista[4] < 0:
            self.lista[4] = 0
            print("o teu pou precisa de carinho")
        if self.lista[4] > 100:
            self.lista[4] = 100
            print("O pou já recebeu demasiado carinho")
            
    """

    def limites(self):

        for i in range(len(self.lista)-1):
            if self.lista[i] < 0:
                self.lista[i] = 0
            elif self.lista[i] > 100:
                self.lista[i] = 100

    def alimentar(self):
        if self.lista[1] > 0:
            self.lista[1] -= 10
            print("Alimentaste o Teu pou!")
        if self.lista[1] < 0:
            self.lista[1] = 0
            print("O teu pou está morto por comer, literalmente")
            pygame.quit()
            sys.exit()
        if self.lista[1] > 100:
            self.lista[1] = 100
            print("O teu pou morreu de fome")
            pygame.quit()
            sys.exit()

    def banho(self):
        if self.lista[2] > 0:
            self.lista[2] -= 50
            print("O teu pou tomou banho!")
        if self.lista[2] < 0:
            self.lista[2] = 0
            print("O  pou está limpo")
        if self.lista[2] > 100:
            self.lista[2] = 100
            print("O teu pou apanhou 9832516 doenças porque não tomou banho")
            pygame.quit()
            sys.exit()

    def brincar(self):
        if self.lista[0] > 0:
            self.lista[0] += 20
            print("O teu pou brincou")
        if self.lista[0] > 100:
            self.lista[0] = 100
            print("O teu pou está demasiado feliz")
        if self.lista[0] <= 0:
            self.lista[0] = 0
            print("Parabéns!!!  O teu pou atirou-se de uma ponte porque não brincou")
            pygame.quit()
            sys.exit()

    def miudodagangue(self):
        if self.rebeldia > 0:
            self.rebeldia += 25
            print("O teu pou foi rebelde")


    def coracao(self):
        if self.lista[4] < 0:
            self.lista[4] += 20
            print ("O pou recebeu carinho")
        if self.lista[4] < 0:
            self.lista[4] = 0
            print("o teu pou precisa de carinho")

        if self.lista[4] > 100:
            self.lista[4] = 100
            print("O pou já recebeu demasiado carinho")

    def brainrot(self):
        print(
            "Only in ohio "" IM HIM "" Are you skibidi "" IMAGINE IF NINJA GOT A LOWWWWWWWW TAPERRRRRRRR FADEEEEEEEEEE "" Eye of rah "" I buyed a proprety in Egypt and what they do for you is they give you the proprety "" Is he doesn´t hawk tuah i don´t talk tuah "" MANGO MANGO MANGO""Artist you can sing VS Artists who can´t sing""Do you have any relationships whit your father.  What´s that,  What´s a father")

    def amorverdadeiro(self):
        if self.lista[5] < 0:
            self.lista[5] += 50
            print(" O teu pou recebeu amor")
        if self.lista[5] > 100:
            self.lista[5] = 100
            print(" O teu pou conheceu o amor verdadeiro")
        if self.lista[5] < 0:
            self.lista[5] = 0
            print("O teu pou ficou deprimente porque ele precisa de amor")

    print(f""" Instruções para o jogo

        [B]rincar - aumenta a felicidade
        [A]limentar - diminui o niveldefome
        [Ba]nho - diminui a sujidade
        [G]angue - faz o teu_pou virar rebelde
        [Br]ainrot- o teu_pou dirá uma frase de brainrot
        [C]arinho - faz carinho ao teu_pou
        [Am]or - dá o amor verdadeiro ao teu pou
        [S]tatus - mostra os status do teu_pou
        """)

    def stats(self):
        for i in range(len(list)):
            print(f"""
Felicidade: {self.lista[0]}
Niveldefome: {self.lista[1]}
Sujidade: {self.lista[2]}
Rebeldia: {self.lista[3]}
Carinho:  {self.lista[4]}
Amor:   {self.lista[5]}
                """)

# -*- coding: utf-8 -*-

import re
import time
  #*********************************************/MENU PRINCIPALE/*********************************************
def menu():

    print("****************OPTION DE MENU****************")
    print("[1] Faire une réservation")
    print("[2] Annuler votre réservation")
    print("[3] Consulter votre réservation")
    print("[4] S'informer sur nos services")
    print("[0] Quitter le programme")


#fonction check existance 
def CheckCINExists(CINS):
    with open("reservation.txt", 'r') as file:
        if re.search(CINS, file.read()):
            return True
        else:
            return False

#*******************************************/TRAITEMENT info/*******************************************
def info():
    with open("info.txt","r")as fic:
        content=fic.read()
        print(content)
    
#*******************************************/TRAITEMENT CONSULTATION/*******************************************
def consulter():
    CINS = input(print("[1] Veillez saisir votre CIN (8 chiffres): "))
    while(not(CINS.isdigit() and len(CINS) == 8)):
        CINS = input(print("[1] Veillez saisir votre CIN (8 chiffres): "))

    if CheckCINExists(CINS) == False:
        time.sleep(2)
        print("Le CIN: " + CINS + " que vous avez bien saisi n'existe pas dans notre liste de réservation.\nVeillez bien s'assurer du CIN.")
        time.sleep(2)
        annuler()
    else:
        with open('reservation.txt') as temp_f:
            datafile = temp_f.readlines()
        for line in datafile:
            if  CINS in line:
                print(line)
                break
    
        

        

        


    







  #*******************************************/TRAITEMENT RESERVATION/*******************************************
def reserver():

    CIN = input(print("[1] Veillez saisir votre CIN (8 chiffres): "))
    while(not(CIN.isdigit() and len(CIN) == 8)):
        CIN = input(print("[1] Veillez saisir votre CIN (8 chiffres): "))


    NUMPASS = input(print("[2] Veillez saisir votre numéro de passeport (10 chiffres): "))
    while(not(NUMPASS.isdigit() and len(NUMPASS) == 10)):
        NUMPASS = input(print("[2] Veillez saisir votre numéro de passeport (10 chiffres): "))


    FAM_NAME = input(print("[3] Veillez saisir votre nom: "))
    while(not(FAM_NAME.isalpha())):
        FAM_NAME = input("[3] Veillez saisir votre nom: ")


    NAME = input(print("[4] Veillez saisir votre prénom: "))
    while(not(NAME.isalpha())):
        NAME = input("[4] Veillez saisir votre prénom: ")
    
    DOB = input(print("[5] Veillez saisir votre date de naissance (jj/mm/aaaa): "))
    regex = re.compile(r'^[0-9]{2}/[0-9]{2}/[0-9]{4}$')
    while not re.findall(regex, DOB):
        DOB = input(print("[5] Veillez saisir votre date de naissance (jj/mm/aaaa): "))

    
    DEST = input(print("[6] Veillez saisir votre déstination: "))
    while(not(DEST.isalpha())):
        DEST = input("[6] Veillez saisir votre déstination: ")

    DDP = input(print("[5] Veillez saisir la date de votre départ (jj/mm/aaaa): "))
    regex = re.compile(r'^[0-9]{2}/[0-9]{2}/[0-9]{4}$')
    while not re.findall(regex, DDP):
        DDP = input(print("[5] Veillez saisir la date de votre départ (jj/mm/aaaa): "))
 

    CONF = input("Voulez vous bien confirmer votre réservation? (o/n): ")
    while(not(CONF == 'o' or CONF == 'n')):
        CONF = input("Voulez vous bien confirmer votre réservation (o/n): ")

    
    
    if CONF == 'o':
        fichier = open("reservation.txt", 'a')
        fichier.write( CIN + " || " + NUMPASS + " || " + FAM_NAME + " || " + NAME + " || " + DOB + " || " + DEST + " || " + DDP + "\n")
        fichier.close()
        print("Votre réservation a été enregistré avec succés.")
        time.sleep(2)
        print("Redirection vers le menu principal.\nVeillez patienter ..")
        time.sleep(2)
        menu()

    elif CONF == 'n':
        print("Redirection vers le menu principal.\nVeillez patienter ..")
        time.sleep(2)
        menu()






#*******************************************/TRAITEMENT ANNULATION/*******************************************
def annuler():

    CINS = input(print("Veillez saisir votre CIN (8 chiffres): "))
    while(not(CINS.isdigit() and len(CINS) == 8)):
        CINS = input(print("Veillez saisir votre CIN (8 chiffres): "))
    
    
    if CheckCINExists(CINS) == False:
        time.sleep(2)
        print("Le CIN: " + CINS + " que vous avez bien saisi n'existe pas dans notre liste de réservation.\nVeillez bien s'assurer du CIN.")
        time.sleep(2)
        annuler()
    else:
        CONF = input("Etes vous sure de vouloir annuler votre réservation? (o/n): ")
        while(not(CONF == 'o' or CONF == 'n')):
            CONF = input("Etes vous sure de vouloir annuler votre réservation? (o/n): ")
        if CONF == 'o': 
            
            with open("reservation.txt","r+") as file:
                new_f = file.readlines()
                file.seek(0)
                for line in new_f:
                    if CINS not in line:
                        file.write(line)
                file.truncate()
            
            
            print("Votre réservation a été annulée avec succés.")
            time.sleep(2)
            print("Redirection vers le menu principal.\nVeillez patienter ..")
            time.sleep(2)
            menu() 
        elif CONF == 'n':
            print("Redirection vers le menu principal.\nVeillez patienter ..")
            time.sleep(2)
            menu()
        else:
            print("option invalide.") 


        
    
    


menu()
option = int (input("Veillez choisir une option: "))

while option != 0:
    if option == 1:
        #traitement option 1
        print("\n******************************************")
        print("Vous avez choisi de faire une réservation.")
        print("******************************************")
        reserver()
        pass
    elif option == 2:
        #traitement option 2 
        print("\n*********************************************")
        print("Vous avez choisi d'annuler votre réservation.")
        print("*********************************************")
        annuler()
      
        pass
    elif option == 3:
        #traitement option 3
        print("\n***********************************************")
        print("Vous avez choisi de consulter votre résevation.")
        print("***********************************************")
        consulter()
        pass
    elif option == 4:
        #traitement option 4
        print("\n***********************************************")
        print("Vous avez choisi de s'informer sur nos services.")
        print("***********************************************")
        info()
        pass
    else:
        print("option invalide.")
    menu()
    option = int (input("Veillez choisir une option: "))

time.sleep(2)
print("Merci pour avoir choisi Qatar Airways. Aurevoir")


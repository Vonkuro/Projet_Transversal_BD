import tkinter as tk
from Main_test import *

ecran = tk.Tk()

class Login():
    def __init__(self):
        self.titre = tk.Frame()
        self.formulaire = tk.Frame()
        self.buton = tk.Frame()

        self.titre_text = tk.Label(master=self.titre, text="Login")
        self.titre_text.pack()

        self.nom_text = tk.Label(master=self.formulaire, text="nom d'utilisateur :")
        self.nom_en =tk.Entry(master=self.formulaire)
        self.nom_text.pack()
        self.nom_en.pack()
        self.mdp_text = tk.Label(master=self.formulaire, text="mot de passe :")
        self.mdp_en = tk.Entry(master=self.formulaire)
        self.mdp_text.pack()
        self.mdp_en.pack()


        self.login = tk.Button(master=self.buton, text="Connexion", command= self.verifications)
        self.compte = tk.Button(master=self.buton, text="créer un compte", command= self.create)
        self.login.pack()
        self.compte.pack()

    def affiche(self):
        self.titre.pack()
        self.formulaire.pack()
        self.buton.pack()
    def verifications(self):
        text = self.nom_en.get()
        self.mdp_en.insert(0,text)
    
    def cache(self):
        self.titre.pack_forget()
        self.formulaire.pack_forget()
        self.buton.pack_forget()

    def create(self):
        sous_page = create_compte()
        self.cache()
        sous_page.affiche()

class create_compte():
    def __init__(self):
        self.titre = tk.Frame()
        self.formulaire = tk.Frame()
        self.buton = tk.Frame()

        self.titre_text = tk.Label(master=self.titre, text="Création de compte")
        self.titre_text.pack()

        self.nom_text = tk.Label(master=self.formulaire, text="nom :")
        self.nom_en = tk.Entry(master=self.formulaire)
        self.nom_text.pack()
        self.nom_en.pack()

        self.prenom_text = tk.Label(master=self.formulaire, text="prénom :")
        self.prenom_en = tk.Entry(master=self.formulaire)
        self.prenom_text.pack()
        self.prenom_en.pack()

        self.mail_text = tk.Label(master=self.formulaire, text="mail :")
        self.mail_en = tk.Entry(master=self.formulaire)
        self.mail_text.pack()
        self.mail_en.pack()

        self.user_text = tk.Label(master=self.formulaire, text="nom d'utilisateur :")
        self.user_en = tk.Entry(master=self.formulaire)
        self.user_text.pack()
        self.user_en.pack()
        self.passeword_text = tk.Label(master=self.formulaire, text="mot de passe :")
        self.passeword_en = tk.Entry(master=self.formulaire)
        self.passeword_text.pack()
        self.passeword_en.pack()

        self.cree = tk.Button(master=self.buton, text="créer")
        self.cree.pack()

    def affiche(self):
        self.titre.pack()
        self.formulaire.pack()
        self.buton.pack()
    
    def cache(self):
        self.titre.pack_forget()
        self.formulaire.pack_forget()
        self.buton.pack_forget()
"""
    def envois(self):
        """

testing= Login()

testing.affiche()

ecran.mainloop()

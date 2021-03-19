import tkinter as tk
from Main_Test import *

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

        self.date_text = tk.Label(master=self.formulaire, text="date de naissance :")
        self.date_en = tk.Entry(master=self.formulaire)
        self.date_text.pack()
        self.date_en.pack()

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

        self.cree = tk.Button(master=self.buton, text="créer", command=self.envois)
        self.cree.pack()

    def affiche(self):
        self.titre.pack()
        self.formulaire.pack()
        self.buton.pack()
        
    
    def cache(self):
        self.titre.pack_forget()
        self.formulaire.pack_forget()
        self.buton.pack_forget()

    def envois(self):
        Erreur = False
        Liste = []
        user_var = self.user_en.get()
        if input_test_text(user_var, 50):
            Liste.append(user_var)
            print("user_add")
        else :
            self.user_en.delete(0, tk.END)
            self.user_en.insert(0, "Le nom d'utilisateur est trop grand")
            Erreur = True

        passeword_var = self.passeword_en.get()
        if input_test_text(passeword_var, 50):
            Liste.append(passeword_var)
            print("passeword_add")
        else :
            self.passeword_en.delete(0, tk.END)
            self.passeword_en.insert(0, "Le mots de passe est trop grand")
            Erreur = True

        nom_var = self.nom_en.get()
        if input_test_text(nom_var, 24):
            Liste.append(nom_var)
            print("nom_add")
        else :
            self.nom_en.delete(0, tk.END)
            self.nom_en.insert(0, "Le nom est trop grand")
            Erreur = True

        prenom_var = self.prenom_en.get()
        if input_test_text(prenom_var, 24):
            Liste.append(prenom_var)
            print("prenom_add")
        else :
            self.prenom_en.delete(0, tk.END)
            self.prenom_en.insert(0, "Le prenom est trop grand")
            Erreur = True
        
        date_var = self.date_en.get()
        if input_test_date(date_var):
            Liste.append(date_var)
            print("date_add")
        else :
            print("date_pb")
            self.date_en.delete(0, tk.END)
            self.date_en.insert(0, "La date n'est pas valide")
            Erreur = True

        mail_var = self.mail_en.get()
        if input_test_mail(mail_var):
            Liste.append(mail_var)
            print("mail_add")
        else :
            print("mail_pb")
            self.mail_en.delete(0, tk.END)
            self.mail_en.insert(0, "Le mail n'est pas valide")
            Erreur = True

        if  not Erreur :
            try :
                #rajouter si le user et mdp sont déjà utilisé
                #rajouter le message d'erreur
                #rajouté retour vers le Login
                ajout_client(Liste[0],Liste[1],Liste[2],Liste[3],Liste[4],Liste[5])
                connexion.commit()
            except:
                return 0


testing= Login()

testing.affiche()

ecran.mainloop()
connexion.close()


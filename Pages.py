import tkinter as tk
from Main_Test import *

#Variable Global
IdPersonne = 0


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

    def affiche(self):
        self.titre.pack()
        self.formulaire.pack()
        self.buton.pack()
    
    def verifications(self):
        global IdPersonne
        IdPersonne = verification_client(self.nom_en.get(),self.mdp_en.get())
        if IdPersonne :
            return "client"

        else :
            IdPersonne =verification_admin(self.nom_en.get(),self.mdp_en.get())
            if IdPersonne :
                return "admin"
        return ""

    def cache(self):
        self.titre.pack_forget()
        self.formulaire.pack_forget()
        self.buton.pack_forget()


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
        else :
            self.user_en.delete(0, tk.END)
            self.user_en.insert(0, "Le nom d'utilisateur est trop grand")
            Erreur = True

        passeword_var = self.passeword_en.get()
        if input_test_text(passeword_var, 50):
            Liste.append(passeword_var)
        else :
            self.passeword_en.delete(0, tk.END)
            self.passeword_en.insert(0, "Le mots de passe est trop grand")
            Erreur = True

        nom_var = self.nom_en.get()
        if input_test_text(nom_var, 24):
            Liste.append(nom_var)
        else :
            self.nom_en.delete(0, tk.END)
            self.nom_en.insert(0, "Le nom est trop grand")
            Erreur = True

        prenom_var = self.prenom_en.get()
        if input_test_text(prenom_var, 24):
            Liste.append(prenom_var)
        else :
            self.prenom_en.delete(0, tk.END)
            self.prenom_en.insert(0, "Le prenom est trop grand")
            Erreur = True
        
        date_var = self.date_en.get()
        if input_test_date(date_var):
            Liste.append(date_var)
        else :
            self.date_en.delete(0, tk.END)
            self.date_en.insert(0, "La date n'est pas valide")
            Erreur = True

        mail_var = self.mail_en.get()
        if input_test_mail(mail_var):
            Liste.append(mail_var)
        else :
            self.mail_en.delete(0, tk.END)
            self.mail_en.insert(0, "Le mail n'est pas valide")
            Erreur = True

        if  not Erreur :
            try :
                if(not verification_admin(user_var, passeword_var) and not verification_client(user_var, passeword_var)) :
                    
                    ajout_client(Liste[0],Liste[1],Liste[2],Liste[3],Liste[4],Liste[5])
                    connexion.commit()
                    #rajouté retour vers le Login
                    return 1
                else :
                    Error_id = tk.Label(master=self.formulaire, text="Ce Nom d'utilisateur existe déjà.")
                    Error_id.pack()
                    return 0
            except:
                return 0

class Accueil_Admin():
    def __init__(self):
        self.titre = tk.Frame()
        self.buton = tk.Frame()

        self.titre_text = tk.Label(master=self.titre, text="Listes des pages")
        self.titre_text.pack()

    def affiche(self):
        self.titre.pack()
        self.buton.pack()

    def cache(self):
        self.titre.pack_forget()
        self.buton.pack_forget()

class Accueil_Client():
    def __init__(self):
        self.entete = tk.Frame()
        self.titre = tk.Frame()
        self.formulaire = tk.Frame()
        self.buton = tk.Frame()

        self.titre_text =tk.Label(master=self.titre, text="Réservation")
        self.titre_text.pack()

        self.date_depart_text = tk.Label(master=self.formulaire, text="dates de départ des vacances :")
        self.date_depart_en = tk.Entry(master=self.formulaire)
        self.date_depart_text.pack()
        self.date_depart_en.pack()

        self.date_fin_text = tk.Label(master=self.formulaire, text="dates de fin des vacances :")
        self.date_fin_en = tk.Entry(master=self.formulaire)
        self.date_fin_text.pack()
        self.date_fin_en.pack()

        self.budget_text = tk.Label(master=self.formulaire, text="Budget :")
        self.budget_en = tk.Entry(master=self.formulaire)
        self.budget_text.pack()
        self.budget_en.pack()

        self.nombre_text = tk.Label(master=self.formulaire, text="Nombre de personnes :")
        self.nombre_en = tk.Entry(master=self.formulaire)
        self.nombre_text.pack()
        self.nombre_en.pack()
    
    def affiche(self):
        self.entete.pack()
        self.titre.pack()
        self.formulaire.pack()
        self.buton.pack()
    
    def cache(self):
        self.entete.pack_forget()
        self.titre.pack_forget()
        self.formulaire.pack_forget()
        self.buton.pack_forget()

class Liste_Admin():
    def __init__(self):
        self.entete = tk.Frame()
        self.titre = tk.Frame()
        self.buton = tk.Frame()
        self.tableau = tk.Frame()
        
        self.titre_text = tk.Label(master=self.titre, text="Listes des Administrateurs")
        self.titre_text.pack()

    def les_liste(self):
        #On crée une liste par colone du tableau, les listes vont contenir les Labels à affichés
        self.nom_list = []
        self.nom_list.append(tk.Label(master=self.tableau, text="Nom"))
        self.nom_list[0].grid(row=0,column=0)

        self.prenom_list = []
        self.prenom_list.append(tk.Label(master=self.tableau, text="Prénom"))
        self.prenom_list[0].grid(row=0,column=1)

        self.mail_list = []
        self.mail_list.append(tk.Label(master=self.tableau, text="Mail"))
        self.mail_list[0].grid(row=0,column=2)

        self.date_list = []
        self.date_list.append(tk.Label(master=self.tableau, text="Date de naissance"))
        self.date_list[0].grid(row=0,column=3)

        self.user_list = []
        self.user_list.append(tk.Label(master=self.tableau, text="Nom utilisateu"))
        self.user_list[0].grid(row=0,column=4)

        self.pwd_list = []
        self.pwd_list.append(tk.Label(master=self.tableau, text="Mots de passe"))
        self.pwd_list[0].grid(row=0,column=5)

        self.suppr_list = []
        self.suppr_list.append(tk.Label(master=self.tableau, text="Supprimer"))
        self.suppr_list[0].grid(row=0,column=6)

        self.modif_list = []
        self.modif_list.append(tk.Label(master=self.tableau, text="Modifier"))
        self.modif_list[0].grid(row=0,column=7)

    def lire_admin(self):
        base = connexion.cursor()
        base.execute("select Nom, Prenom, Mail, DateNaissance, Identifiant, MotsdePasse from Personne inner join Administrateur on Personne.IdPersonne = Administrateur.IdPersonne ;")
        ligne_nb = 1
        for ligne_base in base:
            self.nom_list.append(tk.Label(master=self.tableau, text=ligne_base.Nom))
            self.nom_list[ligne_nb].grid(row=ligne_nb,column=0)

            self.prenom_list.append(tk.Label(master=self.tableau, text=ligne_base.Prenom))
            self.prenom_list[ligne_nb].grid(row=ligne_nb,column=1)

            self.mail_list.append(tk.Label(master=self.tableau, text=ligne_base.Mail))
            self.mail_list[ligne_nb].grid(row=ligne_nb,column=2)

            self.date_list.append(tk.Label(master=self.tableau, text=ligne_base.DateNaissance))
            self.date_list[ligne_nb].grid(row=ligne_nb,column=3)

            self.user_list.append(tk.Label(master=self.tableau, text=ligne_base.Identifiant))
            self.user_list[ligne_nb].grid(row=ligne_nb,column=4)

            self.pwd_list.append(tk.Label(master=self.tableau, text=ligne_base.MotsdePasse))
            self.pwd_list[ligne_nb].grid(row=ligne_nb,column=5)

            self.suppr_list.append(tk.Label(master=self.tableau, text="Supprimer"))
            self.suppr_list[ligne_nb].grid(row=ligne_nb,column=6)

            self.modif_list.append(tk.Label(master=self.tableau, text="Modifier")) #Modifier pour les boutons
            self.modif_list[ligne_nb].grid(row=ligne_nb,column=7)

        base.close()

    def affiche(self):
        self.les_liste()
        self.lire_admin()
        self.entete.pack()
        self.titre.pack()
        self.buton.pack()
        self.tableau.pack()

    def cache(self):
        self.entete.pack_forget()
        self.titre.pack_forget()
        self.buton.pack_forget()
        self.tableau.pack_forget()

#Fonctionnement des boutons
def changement_page(Actuelle, Suivante):
    Actuelle.cache()
    Suivante.affiche()

def appel_envois(Creation, Log):
    if (Creation.envois()) :
        changement_page(Creation, Log)

def Log_In(Log, Accueil_Ad, Accueil_Cl) : #modifié pour accueil client
    verif = Log.verifications()
    if verif == "admin":
        changement_page(Log, Accueil_Ad)
    elif verif == "client":
        changement_page(Log, Accueil_Cl)

def Log_Out(Log, Actuelle):
    global IdPersonne
    IdPersonne = 0
    changement_page(Actuelle, Log)

#Main
def Application():
    ecran = tk.Tk()
    #initialisation des pages
    Login_page = Login()
    Creation_Client = create_compte()
    Accueil_Ad = Accueil_Admin()
    Accueil_Cl = Accueil_Client() #attention elle n'a aucun boutons pour l'instant
    Liste_Ad = Liste_Admin()
    
    #initialisation des boutons d'interaction entre les pages
    #butons Logins
    login = tk.Button(master=Login_page.buton, text="Connexion", command= lambda: Log_In(Login_page, Accueil_Ad, Accueil_Cl))
    login.pack()
    compte = tk.Button(master=Login_page.buton, text="créer un compte", command= lambda: changement_page(Login_page, Creation_Client))
    compte.pack()
    #butons Création de compte Client
    cree = tk.Button(master=Creation_Client.buton, text="créer", command= lambda: appel_envois(Creation_Client, Login_page))
    cree.pack()
    #butons Accueil Admin
    clients_a_a = tk.Button(master=Accueil_Ad.buton, text="Listes Clients")
    clients_a_a.pack()
    administrateurs_a_a  = tk.Button(master=Accueil_Ad.buton, text="Listes Administrateurs")
    administrateurs_a_a.pack()
    circuits_a_a = tk.Button(master=Accueil_Ad.buton, text="Listes Circuits")
    circuits_a_a.pack()
    etapes_a_a = tk.Button(master=Accueil_Ad.buton, text="Listes Etapes")
    etapes_a_a.pack()
    lieux_a_a = tk.Button(master=Accueil_Ad.buton, text="Listes Lieux")
    lieux_a_a.pack()
    accueil_admin_logout = tk.Button(master=Accueil_Ad.buton, text="log out", command= lambda: Log_Out(Login_page, Accueil_Ad))
    accueil_admin_logout.pack()

    #Fonctionnement
    #Login_page.affiche()
    Liste_Ad.affiche()
    ecran.mainloop()
    connexion.close()

Application()
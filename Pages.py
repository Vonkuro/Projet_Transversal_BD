import tkinter as tk
from Main_Test import *

#Variable Global
IdPersonne = 0



class Login():
    def __init__(self):
        self.titre = tk.Frame(width=300, height=5000)#on donne à chaque frame une taille
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
        #On rajoute la propriété propagate(0) afin que la frame ne s'adapte pas à ses wiglets
        self.titre.propagate(0)
        self.formulaire.propagate(0)
        self.buton.propagate(0)
    
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

    def envois(self): #ATTETION tu ne vérifie pas si les Entry sont vide !!!
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

        self.Id_list = [0]

        self.suppr_list = []
        self.suppr_list.append(tk.Label(master=self.tableau, text="Supprimer"))
        self.suppr_list[0].grid(row=0,column=6)

        self.modif_list = []
        self.modif_list.append(tk.Label(master=self.tableau, text="Modifier"))
        self.modif_list[0].grid(row=0,column=7)

    def lire_admin(self):
        base = connexion.cursor()
        base.execute("select Nom, Prenom, Mail, DateNaissance, Identifiant, MotsdePasse, Personne.IdPersonne from Personne inner join Administrateur on Personne.IdPersonne = Administrateur.IdPersonne ;")
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

            self.Id_list.append(ligne_base.IdPersonne)
            
            self.suppr_list.append(tk.Button(master=self.tableau, text="Supprimer", command= lambda var_id = self.Id_list[ligne_nb], var_ligne = ligne_nb : self.Supprime(var_id,var_ligne)))
            self.suppr_list[ligne_nb].grid(row=ligne_nb,column=6)

            self.modif_list.append(tk.Button(master=self.tableau, text="Modifier", command= lambda var_ligne = ligne_nb: self.modifier_active(var_ligne))) #Modifier pour les boutons
            self.modif_list[ligne_nb].grid(row=ligne_nb,column=7)
            ligne_nb = ligne_nb + 1

        base.close()
        self.grand_buton_ajout = tk.Button(master=self.buton, text= "Ajouter", command= lambda: self.Ajout_form(ligne_nb))
        self.grand_buton_ajout.pack()

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
        self.grand_buton_ajout.destroy()
    
    def modifier_active(self, ligne_nb):
        #on fais disparaitre les Labels
        self.nom_list[ligne_nb].grid_forget()
        self.prenom_list[ligne_nb].grid_forget()
        self.mail_list[ligne_nb].grid_forget()
        self.date_list[ligne_nb].grid_forget()
        self.user_list[ligne_nb].grid_forget()
        self.pwd_list[ligne_nb].grid_forget()
        self.suppr_list[ligne_nb].grid_forget()
        self.modif_list[ligne_nb].grid_forget()
        #on fait apparaître les Entrys
        self.nom_modif = tk.Entry(master=self.tableau)
        self.nom_modif.insert(0,self.nom_list[ligne_nb].cget("text"))
        self.nom_modif.grid(row=ligne_nb,column=0)

        self.prenom_modif = tk.Entry(master=self.tableau)
        self.prenom_modif.insert(0, self.prenom_list[ligne_nb].cget("text"))
        self.prenom_modif.grid(row=ligne_nb, column=1)

        self.mail_modif = tk.Entry(master=self.tableau)
        self.mail_modif.insert(0, self.mail_list[ligne_nb].cget("text"))
        self.mail_modif.grid(row=ligne_nb, column=2)

        self.date_modif = tk.Entry(master=self.tableau)
        self.date_modif.insert(0, self.date_list[ligne_nb].cget("text"))
        self.date_modif.grid(row=ligne_nb, column=3)

        self.user_modif = tk.Entry(master=self.tableau)
        self.user_modif.insert(0, self.user_list[ligne_nb].cget("text"))
        self.user_modif.grid(row=ligne_nb, column=4)

        self.pwd_modif = tk.Entry(master=self.tableau)
        self.pwd_modif.insert(0, self.pwd_list[ligne_nb].cget("text"))
        self.pwd_modif.grid(row=ligne_nb, column=5)

        self.suppr_modif = tk.Label(master=self.tableau, text="Supprimer") 
        self.suppr_modif.grid(row=ligne_nb, column=6)

        self.modif_modif = tk.Button(master=self.tableau, text="Modifier", command= lambda: self.modifier_enregistre(ligne_nb))
        self.modif_modif.grid(row=ligne_nb, column=7)
        
        

    def modifier_enregistre(self, ligne_nb):
        #input_test_mail
        #input_test_date
        Error = False
        if not input_test_text(self.nom_modif.get(), 24):
            Error= True
        if not input_test_text(self.prenom_modif.get(), 24):
            Error= True
        if not input_test_text(self.user_modif.get(), 50):
            Error= True
        if not input_test_text(self.pwd_modif.get(), 50):
            Error= True
        if not input_test_date(self.date_modif.get()):
            Error= True
        if not input_test_mail(self.mail_modif.get()):
            Error= True
        if not Error:
            update_admin(self.user_modif.get(), self.pwd_modif.get(), self.nom_modif.get(), self.prenom_modif.get(), self.date_modif.get(), self.mail_modif.get(), self.Id_list[ligne_nb-1])
            connexion.commit()
            #forget les entrys et recharge la page
            self.nom_modif.grid_forget()
            self.prenom_modif.grid_forget()
            self.user_modif.grid_forget()
            self.pwd_modif.grid_forget()
            self.date_modif.grid_forget()
            self.mail_modif.grid_forget()
            self.cache()
            self.affiche()

    def Supprime(self, Id, ligne_nb):
        self.nom_list[ligne_nb].grid_forget()
        self.prenom_list[ligne_nb].grid_forget()
        self.mail_list[ligne_nb].grid_forget()
        self.date_list[ligne_nb].grid_forget()
        self.user_list[ligne_nb].grid_forget()
        self.pwd_list[ligne_nb].grid_forget()
        self.suppr_list[ligne_nb].grid_forget()
        self.modif_list[ligne_nb].grid_forget()
        supprime_admin(Id)
        connexion.commit()
        self.cache()
        self.affiche()

    def Ajout_form(self, ligne):
        #on fait apparaître les Entrys
        self.nom_ajout = tk.Entry(master=self.tableau)
        self.nom_ajout.grid(row=ligne,column=0)

        self.prenom_ajout = tk.Entry(master=self.tableau)
        self.prenom_ajout.grid(row=ligne, column=1)

        self.mail_ajout = tk.Entry(master=self.tableau)
        self.mail_ajout.grid(row=ligne, column=2)

        self.date_ajout = tk.Entry(master=self.tableau)
        self.date_ajout.grid(row=ligne, column=3)

        self.user_ajout = tk.Entry(master=self.tableau)
        self.user_ajout.grid(row=ligne, column=4)

        self.pwd_ajout = tk.Entry(master=self.tableau)
        self.pwd_ajout.grid(row=ligne, column=5)

        self.buton_ajout = tk.Button(master=self.tableau, text="Validation", command= lambda:self.Ajout_action())
        self.buton_ajout.grid(row=ligne, column=6)

    def Ajout_action(self):
        Error = False
        if not input_test_text(self.nom_ajout.get(), 24):
            Error= True
        if not input_test_text(self.prenom_ajout.get(), 24):
            Error= True
        if not input_test_text(self.user_ajout.get(), 50):
            Error= True
        if not input_test_text(self.pwd_ajout.get(), 50):
            Error= True
        if not input_test_date(self.date_ajout.get()):
            Error= True
        if not input_test_mail(self.mail_ajout.get()):
            Error= True
        if not Error:
            ajout_admin(self.user_ajout.get(), self.pwd_ajout.get(), self.nom_ajout.get(), self.prenom_ajout.get(), self.date_ajout.get(), self.mail_ajout.get())
            connexion.commit()
            self.user_ajout.grid_forget()
            self.pwd_ajout.grid_forget()
            self.nom_ajout.grid_forget()
            self.prenom_ajout.grid_forget()
            self.date_ajout.grid_forget()
            self.mail_ajout.grid_forget()
            self.buton_ajout.grid_forget()
            self.cache()
            self.affiche()

class Liste_Lieux():
    def __init__(self):
        self.entete = tk.Frame()
        self.titre = tk.Frame()
        self.buton = tk.Frame()
        self.tableau = tk.Frame()
        
        self.titre_text = tk.Label(master=self.titre, text="Listes des Lieux")
        self.titre_text.pack()

    def affiche(self):
        self.les_liste()
        self.lire_lieux()
        self.entete.pack()
        self.titre.pack()
        self.buton.pack()
        self.tableau.pack()

    def cache(self):
        self.entete.pack_forget()
        self.titre.pack_forget()
        self.buton.pack_forget()
        self.tableau.pack_forget()
        self.grand_buton_ajout.destroy()
    
    def les_liste(self):

        self.nom_list =[]
        self.nom_list.append(tk.Label(master=self.tableau, text="Nom du Lieu"))
        self.nom_list[0].grid(row=0,column=0)

        self.ville_list =[]
        self.ville_list.append(tk.Label(master=self.tableau, text="Ville"))
        self.ville_list[0].grid(row=0,column=1)

        self.pays_list =[]
        self.pays_list.append(tk.Label(master=self.tableau, text="Pays"))
        self.pays_list[0].grid(row=0,column=2)

        self.descriptifs_list =[]
        self.descriptifs_list.append(tk.Label(master=self.tableau, text="Descriptifs"))
        self.descriptifs_list[0].grid(row=0,column=3)

        self.prix_list =[]
        self.prix_list.append(tk.Label(master=self.tableau, text="Prix"))
        self.prix_list[0].grid(row=0,column=4)

        self.suppr_list = []
        self.suppr_list.append(tk.Label(master=self.tableau, text="Supprimer"))
        self.suppr_list[0].grid(row=0,column=5)

        self.modif_list = []
        self.modif_list.append(tk.Label(master=self.tableau, text="Modifier"))
        self.modif_list[0].grid(row=0,column=6)

    def lire_lieux(self):
        base = connexion.cursor()
        base.execute("select * from Lieu;")
        ligne_nb = 1
        for ligne_base in base:
            
            self.nom_list.append(tk.Label(master=self.tableau, text=ligne_base.NomLieu))
            self.nom_list[ligne_nb].grid(row=ligne_nb,column=0)

            self.ville_list.append(tk.Label(master=self.tableau, text=ligne_base.Ville))
            self.ville_list[ligne_nb].grid(row=ligne_nb,column=1)

            self.pays_list.append(tk.Label(master=self.tableau, text=ligne_base.Pays))
            self.pays_list[ligne_nb].grid(row=ligne_nb,column=2)

            self.descriptifs_list.append(tk.Label(master=self.tableau, text=ligne_base.Descriptif))
            self.descriptifs_list[ligne_nb].grid(row=ligne_nb,column=3)

            self.prix_list.append(tk.Label(master=self.tableau, text=ligne_base.PrixVisite))
            self.prix_list[ligne_nb].grid(row=ligne_nb,column=4)

            self.suppr_list.append(tk.Button(master=self.tableau, text="Supprimer", command= lambda var_ligne = ligne_nb : self.Supprime(var_ligne))) #
            self.suppr_list[ligne_nb].grid(row=ligne_nb,column=5)

            self.modif_list.append(tk.Button(master=self.tableau, text="Modifier", command= lambda var_ligne = ligne_nb : self.modifier_active(var_ligne)))
            self.modif_list[ligne_nb].grid(row=ligne_nb,column=6)
            ligne_nb = ligne_nb + 1

        base.close()
        self.grand_buton_ajout = tk.Button(master=self.buton, text= "Ajouter",command= lambda: self.Ajout_form(ligne_nb))
        self.grand_buton_ajout.pack()

    def modifier_active(self, ligne_nb):
        #on fais disparaitre les Labels
        self.nom_list[ligne_nb].grid_forget()
        self.ville_list[ligne_nb].grid_forget()
        self.pays_list[ligne_nb].grid_forget()
        self.descriptifs_list[ligne_nb].grid_forget()
        self.prix_list[ligne_nb].grid_forget()
        self.suppr_list[ligne_nb].grid_forget()
        self.modif_list[ligne_nb].grid_forget()
        #on fait apparaître les Entrys
        self.nom_modif = tk.Entry(master=self.tableau)
        self.nom_modif.insert(0,self.nom_list[ligne_nb].cget("text"))
        self.nom_modif.grid(row=ligne_nb,column=0)

        self.ville_modif = tk.Entry(master=self.tableau)
        self.ville_modif.insert(0,self.ville_list[ligne_nb].cget("text"))
        self.ville_modif.grid(row=ligne_nb,column=1)

        self.pays_modif = tk.Entry(master=self.tableau)
        self.pays_modif.insert(0,self.pays_list[ligne_nb].cget("text"))
        self.pays_modif.grid(row=ligne_nb,column=2)

        self.descriptifs_modif = tk.Entry(master=self.tableau)
        self.descriptifs_modif.insert(0,self.descriptifs_list[ligne_nb].cget("text"))
        self.descriptifs_modif.grid(row=ligne_nb,column=3)

        self.prix_modif = tk.Entry(master=self.tableau)
        self.prix_modif.insert(0,self.prix_list[ligne_nb].cget("text"))
        self.prix_modif.grid(row=ligne_nb,column=4)

        self.suppr_modif = tk.Label(master=self.tableau, text="Supprimer") 
        self.suppr_modif.grid(row=ligne_nb, column=5)

        self.modif_modif = tk.Button(master=self.tableau, text="Modifier", command= lambda: self.modifier_enregistre(ligne_nb))
        self.modif_modif.grid(row=ligne_nb, column=6)

    def modifier_enregistre(self, ligne_nb):
        Error = False
        if not input_test_text(self.nom_modif.get(), 24):
            Error= True
        if not input_test_text(self.ville_modif.get(), 24):
            Error= True
        if not input_test_text(self.pays_modif.get(), 24):
            Error= True
        if not input_test_text(self.descriptifs_modif.get(), 250):
            Error= True
        try :
            float(self.prix_modif.get())
        except:
            Error= True
        if not Error:
            update_lieu(self.nom_list[ligne_nb].cget("text"),self.ville_list[ligne_nb].cget("text"),self.pays_list[ligne_nb].cget("text"),self.nom_modif.get(),self.ville_modif.get(),self.pays_modif.get(),self.descriptifs_modif.get(),float(self.prix_modif.get()))
            connexion.commit()
            self.nom_modif.grid_forget()
            self.ville_modif.grid_forget()
            self.pays_modif.grid_forget()
            self.descriptifs_modif.grid_forget()
            self.prix_modif.grid_forget()
            self.cache()
            self.affiche()

    def Supprime(self, ligne):
        supprime_lieu(self.nom_list[ligne].cget("text"), self.ville_list[ligne].cget("text"), self.pays_list[ligne].cget("text"))
        connexion.commit()
        self.nom_list[ligne].grid_forget()
        self.ville_list[ligne].grid_forget()
        self.pays_list[ligne].grid_forget()
        self.descriptifs_list[ligne].grid_forget()
        self.prix_list[ligne].grid_forget()
        self.suppr_list[ligne].grid_forget()
        self.modif_list[ligne].grid_forget()
        self.cache()
        self.affiche()

    def Ajout_form(self, ligne):
        #on fait apparaître les Entrys
        self.nom_ajout = tk.Entry(master=self.tableau)
        self.nom_ajout.grid(row=ligne,column=0)

        self.ville_ajout = tk.Entry(master=self.tableau)
        self.ville_ajout.grid(row=ligne,column=1)

        self.pays_ajout = tk.Entry(master=self.tableau)
        self.pays_ajout.grid(row=ligne,column=2)

        self.descriptifs_ajout = tk.Entry(master=self.tableau)
        self.descriptifs_ajout.grid(row=ligne,column=3)

        self.prix_ajout = tk.Entry(master=self.tableau)
        self.prix_ajout.grid(row=ligne,column=4)

        self.buton_ajout = tk.Button(master=self.tableau, text="Validation", command= lambda: self.Ajout_action())
        self.buton_ajout.grid(row=ligne,column=5)
    
    def Ajout_action(self):
        Error = False
        if not input_test_text(self.nom_ajout.get(), 24):
            Error= True
        if not input_test_text(self.ville_ajout.get(), 24):
            Error= True
        if not input_test_text(self.pays_ajout.get(), 24):
            Error= True
        if not input_test_text(self.descriptifs_ajout.get(), 250):
            Error= True
        try :
            float(self.prix_ajout.get())
        except:
            Error= True
        if not Error:
            ajout_lieu(self.nom_ajout.get(), self.ville_ajout.get(), self.pays_ajout.get(), self.descriptifs_ajout.get(), float(self.prix_ajout.get()))
            connexion.commit()
            self.nom_ajout.grid_forget()
            self.ville_ajout.grid_forget()
            self.pays_ajout.grid_forget()
            self.descriptifs_ajout.grid_forget()
            self.prix_ajout.grid_forget()
            self.buton_ajout.grid_forget()
            
            self.cache()
            self.affiche()


class Liste_Etape():
    def __init__(self):
        self.entete = tk.Frame()
        self.titre = tk.Frame()
        self.buton = tk.Frame()
        self.tableau = tk.Frame()
        
        self.titre_text = tk.Label(master=self.titre, text="Listes des Etapes")
        self.titre_text.pack()

    
    def affiche(self):
        self.les_liste()
        self.lire_etape()
        self.entete.pack()
        self.titre.pack()
        self.buton.pack()
        self.tableau.pack()

    def cache(self):
        self.entete.pack_forget()
        self.titre.pack_forget()
        self.buton.pack_forget()
        self.tableau.pack_forget()
        #self.grand_buton_ajout.destroy()

    def les_liste(self):

        self.circuit_list =[]
        self.circuit_list.append(tk.Label(master=self.tableau, text="Numéro du Circuit"))
        self.circuit_list[0].grid(row=0,column=0)

        self.ordre_list =[]
        self.ordre_list.append(tk.Label(master=self.tableau, text="Ordre"))
        self.ordre_list[0].grid(row=0,column=1)

        self.date_list =[]
        self.date_list.append(tk.Label(master=self.tableau, text="Date de Début"))
        self.date_list[0].grid(row=0,column=2)

        self.duree_list =[]
        self.duree_list.append(tk.Label(master=self.tableau, text="Durée"))
        self.duree_list[0].grid(row=0,column=3)

        self.nom_list =[]
        self.nom_list.append(tk.Label(master=self.tableau, text="Nom du Lieu"))
        self.nom_list[0].grid(row=0,column=4)

        self.ville_list =[]
        self.ville_list.append(tk.Label(master=self.tableau, text="Ville"))
        self.ville_list[0].grid(row=0,column=5)

        self.pays_list =[]
        self.pays_list.append(tk.Label(master=self.tableau, text="Pays"))
        self.pays_list[0].grid(row=0,column=6)

        self.suppr_list = []
        self.suppr_list.append(tk.Label(master=self.tableau, text="Supprimer"))
        self.suppr_list[0].grid(row=0,column=7)

        self.modif_list = []
        self.modif_list.append(tk.Label(master=self.tableau, text="Modifier"))
        self.modif_list[0].grid(row=0,column=8)


    def lire_etape(self):
        base = connexion.cursor()
        base.execute("select * from Etape;")
        ligne_nb = 1
        for ligne_base in base:
            self.circuit_list.append(tk.Label(master=self.tableau, text=ligne_base.IdCircuit))
            self.circuit_list[0].grid(row=ligne_nb,column=0)

            self.ordre_list.append(tk.Label(master=self.tableau, text=ligne_base.Ordre))
            self.ordre_list[0].grid(row=ligne_nb,column=0)

        base.close()
        self.grand_buton_ajout = tk.Button(master=self.buton, text= "Ajouter")#,command= lambda: self.Ajout_form(ligne_nb))
        self.grand_buton_ajout.pack()
import tkinter as tk
from tkinter.ttk import *
from Main_Test import *

#Variables Globals
IdPersonne = 0
liste_informations = [] #date départ, date fin, budget et nombre de place
IdCircuit = 0
IdReservation = 0


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
        global liste_informations
        liste_informations = []
        global IdCircuit
        IdCircuit = 0
        global IdReservation
        IdReservation = 0
        self.entete.pack()
        self.titre.pack()
        self.formulaire.pack()
        self.buton.pack()
    
    def cache(self):
        self.entete.pack_forget()
        self.titre.pack_forget()
        self.formulaire.pack_forget()
        self.buton.pack_forget()

    #Réfléxion : toujour une classe par écran, une fonction particulière par changement de page
    def verification(self):
        Error = False
        if input_test_date(self.date_depart_en.get()):
            Error =  True
        if input_test_date(self.date_fin_en.get()):
            Error =  True
        try:
            int(self.nombre_en.get())
            float(self.budget_en.get())
        except:
            Error = True
        if not Error:
            global liste_informations
            liste_informations = [self.date_depart_en.get(), self.date_fin_en.get(), float(self.budget_en.get()), int(self.nombre_en.get())]
            return True
        else:
            return False

class Presentation_Circuit():
    def __init__(self):
        self.entete = tk.Frame()
        self.titre = tk.Frame()
        self.tableau = tk.Frame()
        self.buton = tk.Frame()

        self.titre_text =tk.Label(master=self.titre, text="Choisir un Circuit")
        self.titre_text.pack()
        self.Choix_Circuit = 0
        self.nombre_place = 0
    
    def affiche(self):
        global liste_informations
        self.Choix_Circuit = 0
        self.nombre_place = liste_informations[3]
        self.lire_circuit(liste_informations)
        self.entete.pack()
        self.titre.pack()
        self.buton.pack()
        self.tableau.pack()
    
    def cache(self):
        for widget in self.tableau.winfo_children():
            widget.destroy()
        self.entete.pack_forget()
        self.titre.pack_forget()
        self.tableau.pack_forget()
        self.buton.pack_forget()
        global IdCircuit
        IdCircuit = self.Choix_Circuit
        return self.Choix_Circuit
    
    def lire_circuit(self, liste_informations):
        #Les listes des trois colonnes
        self.circuit_list = []
        self.circuit_list.append(tk.Label(master=self.tableau, text="Circuits"))
        self.circuit_list[0].grid(row=0,column=0)

        self.prix_list = []
        self.prix_list.append(tk.Label(master=self.tableau, text="Prix"))
        self.prix_list[0].grid(row=0,column=1)

        self.Id_list = [] #liste contenant les Id au même index que la description
        self.Id_list.append(0)

        self.select_list = []
        self.select_list.append(tk.Label(master=self.tableau, text="Selectionner"))
        self.select_list[0].grid(row=0,column=2)

        #appel sql qui trouve circuit sous bugdet, après date début et avant date fin
        liste_Id = trouve_circuit(liste_informations) #liste contenant les Id et les prix des circuits trouvés
        base = connexion.cursor()
        ligne_nb = 1
        for Id in liste_Id:
            base.execute("select * from Circuit where IdCircuit = ? and NbPlaceDisponible > 0;",[Id[0]])
            ligne_base = base.fetchone()

            self.Id_list.append(ligne_base.IdCircuit)

            message = ligne_base.Descriptif + " depuis " + ligne_base.VilleDepart + " en " + ligne_base.PaysDepart
            message += " jusqu'à " + ligne_base.VilleArrivee + " en " + ligne_base.PaysArrivee + ". Il reste "
            message += str(ligne_base.NbPlaceDisponible) + " places. Le cicruit commence le " + ligne_base.DateDepart
            message += " et durera " + str(ligne_base.Duree) + " jours."
            self.circuit_list.append(tk.Label(master=self.tableau, text=message))
            self.circuit_list[ligne_nb].grid(row=ligne_nb, column= 0)

            self.prix_list.append(tk.Label(master=self.tableau, text=Id[1]))
            self.prix_list[ligne_nb].grid(row=ligne_nb, column= 1)

            self.select_list.append(tk.Button(master=self.tableau, text="Selectionner", command= lambda var_ligne = ligne_nb : self.Choix(var_ligne)))
            self.select_list[ligne_nb].grid(row=ligne_nb, column= 2)
        base.close()

    def Choix(self,ligne):
        self.Choix_Circuit = self.Id_list[ligne]
        for i in range(1,len(self.select_list)):
            self.select_list[i].configure(relief='raised')
        self.select_list[ligne].configure(relief='sunken')

class Presentation_Etape():
    def __init__(self):
        self.entete = tk.Frame()
        self.titre = tk.Frame()
        self.tableau = tk.Frame()
        self.buton = tk.Frame()

        self.titre_text =tk.Label(master=self.titre, text="Choisir un Circuit")
        self.titre_text.pack()
        self.Id = 0
    
    def affiche(self):
        self.lire_etape()
        self.entete.pack()
        self.titre.pack()
        self.tableau.pack()
        self.buton.pack()
    
    def cache(self):
        self.reservation()
        for widget in self.tableau.winfo_children():
            widget.destroy()
        self.entete.pack_forget()
        self.titre.pack_forget()
        self.tableau.pack_forget()
        self.buton.pack_forget()
        
    
    def lire_etape(self):
        #les listes
        global IdCircuit
        message = "Circuit " + str(IdCircuit) + " :"
        self.circuit_titre = tk.Label(master=self.tableau, text=message)
        self.circuit_titre.grid(row=0,column=0)

        self.ordre_list = []
        self.ordre_list.append(0)

        self.lieu_list = []
        self.lieu_list.append(0)

        self.descriptif_list = []
        self.descriptif_list.append(0)

        #sql
        base = connexion.cursor()
        ligne_nb = 1
        base.execute("select Ordre, DateEtape, Duree, Descriptif, Etape.NomLieu, Etape.Ville, Etape.Pays from Etape, Lieu where IdCircuit = ? and Etape.NomLieu = Lieu.NomLieu and Etape.Ville = Lieu.Ville and Etape.Pays = Lieu.Pays;",[IdCircuit])
        for ligne_base in base:
            message = "Etape n°" + str(ligne_base.Ordre)
            self.ordre_list.append(tk.Label(master=self.tableau, text=message))
            self.ordre_list[ligne_nb].grid(row = ligne_nb, column= 0)
            #Nom en Ville, Pays le Date pour Duree jours. | Description
            message = ligne_base.NomLieu + " en " + ligne_base.Ville + ", " + ligne_base.Pays + " le " + ligne_base.DateEtape + " pour " + str(ligne_base.Duree) + " jours."
            self.lieu_list.append(tk.Label(master=self.tableau, text= message))
            self.lieu_list[ligne_nb].grid(row = ligne_nb, column= 1)

            self.descriptif_list.append(tk.Label(master=self.tableau, text=ligne_base.Descriptif))
            self.descriptif_list[ligne_nb].grid(row = ligne_nb, column= 2)
            ligne_nb += 1
        base.close()

    def reservation(self):
        global IdPersonne
        global liste_informations
        today = datetime.today()
        aujourdhuis = today.strftime("%Y-%m-%d")
        ajout_reservation(IdPersonne, IdCircuit, liste_informations[3], aujourdhuis)
        base = connexion.cursor()
        base.execute("select IdReservation from Reservation where IdPersonne = ? and IdCircuit = ? and DateRevervation = ?;",[IdPersonne,IdCircuit,aujourdhuis])
        ligne_base = base.fetchone()
        global IdReservation
        IdReservation = ligne_base.IdReservation
        base.close()

class Reservation_passager():
    def __init__(self):
        self.entete = tk.Frame()
        self.titre = tk.Frame()
        self.tableau = tk.Frame()
        self.buton = tk.Frame()
        self.buton_2 = tk.Frame()

        self.titre_text =tk.Label(master=self.titre, text="Informations sur les passagers")
        self.titre_text.pack()
    
    def affiche(self):
        self.form_passager()
        self.entete.pack()
        self.titre.pack()
        self.tableau.pack()
        self.buton.pack()
    
    def cache(self):
        for widget in self.tableau.winfo_children():
            widget.destroy()
        self.grand_buton_ajout.destroy()
        self.entete.pack_forget()
        self.titre.pack_forget()
        self.tableau.pack_forget()
        self.buton.pack_forget()
        self.buton_2.pack_forget()
        

    def form_passager(self):
        self.grand_buton_ajout = tk.Button(master=self.buton, text= "Ajouter", command= lambda: self.verification())
        self.grand_buton_ajout.pack()
        #listes
        self.nombre_liste = []
        self.nom_liste = []
        self.prenom_liste = []
        self.date_list = []
        self.frame_list = []
        #affichage
        global liste_informations
        for ligne in range(liste_informations[3]):
            #créer un frame
            
            message = "Passager " + str(ligne + 1)
            titre = tk.Label(master=self.tableau, text=message)
            titre.grid(row=ligne , column = 0)

            self.frame_list.append(tk.Frame(master=self.tableau))
            self.frame_list[ligne].grid(row = ligne, column = 1)

            nom = tk.Label(master=self.frame_list[ligne], text="Nom :")
            nom.grid(row= 0, column =0)

            self.nom_liste.append(tk.Entry(master=self.frame_list[ligne]))
            self.nom_liste[ligne].grid(row= 0, column =1)

            prenom = tk.Label(master=self.frame_list[ligne], text="Prenom :")
            prenom.grid(row= 1, column =0)

            self.prenom_liste.append(tk.Entry(master=self.frame_list[ligne]))
            self.prenom_liste[ligne].grid(row= 1, column =1)

            date = tk.Label(master=self.frame_list[ligne], text="Date de Naissance :")
            date.grid(row= 2, column =0)

            self.date_list.append(tk.Entry(master=self.frame_list[ligne]))
            self.date_list[ligne].grid(row= 2, column =1)

    def verification(self):
        Error = False
        for ligne in range(len(self.frame_list)) :
            if input_test_text(self.nom_liste[ligne].get(),24):
                Error =  True
            if input_test_text(self.prenom_liste[ligne].get(),24):
                Error =  True
            if input_test_date(self.date_list[ligne].get()):
                Error =  True
            
        if not Error:
            global IdReservation
            for ligne in range(len(self.frame_list)) :
                IdPassager = identification_passager(self.nom_liste[ligne].get(), self.prenom_liste[ligne].get(), self.date_list[ligne].get())
                ajout_groupe(IdPassager, IdReservation)
                connexion.commit()
                self.buton.pack_forget()
                self.buton_2.pack()

class Presentation_Reservation():
    def __init__(self):
        self.entete = tk.Frame()
        self.titre = tk.Frame()
        self.buton = tk.Frame()
        self.tableau = tk.Frame()
        
        self.titre_text = tk.Label(master=self.titre, text="Vos Reservations")
        self.titre_text.pack()

    def affiche(self):
        self.les_liste()
        self.lire_reserv()
        self.entete.pack()
        self.titre.pack()
        global IdReservation
        IdReservation = 0
        self.tableau.pack()

    def cache(self):
        for widget in self.tableau.winfo_children():
            widget.destroy()
        self.entete.pack_forget()
        self.titre.pack_forget()
        self.buton.pack_forget()
        self.tableau.pack_forget()
    
    def les_liste(self):
        #On crée une liste par colone du tableau, les listes vont contenir les Labels à affichés
        self.Id_list = []
        self.Id_list.append(tk.Label(master=self.tableau, text="Numero du circuit"))
        self.Id_list[0].grid(row=0,column=0)
        
        self.description_list = []
        self.description_list.append(tk.Label(master=self.tableau, text="Description du circuit"))
        self.description_list[0].grid(row=0,column=1)

        self.date_list = []
        self.date_list.append(tk.Label(master=self.tableau, text="Date de Départ"))
        self.date_list[0].grid(row=0,column=2)

        self.nombre_list = []
        self.nombre_list.append(tk.Label(master=self.tableau, text="Nombre de Passagers"))
        self.nombre_list[0].grid(row=0,column=3)

        self.detail_list = []
        self.detail_list.append(tk.Label(master=self.tableau, text="Selectionner"))
        self.detail_list[0].grid(row=0,column=4)

        self.reserv_list =[]
        self.reserv_list.append(0)

    def lire_reserv(self):
        global IdPersonne
        base = connexion.cursor()
        base.execute("Select Circuit.IdCircuit, Descriptif, DateDepart, Place, IdReservation from Reservation, Circuit where Circuit.IdCircuit = Reservation.IdCircuit and IdPersonne = ?;", [IdPersonne])
        ligne = 1
        for ligne_base in base:
            self.Id_list.append(tk.Label(master=self.tableau, text=ligne_base.IdCircuit))
            self.Id_list[ligne].grid(row=ligne,column=0)

            self.description_list.append(tk.Label(master=self.tableau, text=ligne_base.Descriptif))
            self.description_list[ligne].grid(row=ligne,column=1)

            self.date_list.append(tk.Label(master=self.tableau, text=ligne_base.DateDepart))
            self.date_list[ligne].grid(row=ligne,column=2)

            self.nombre_list.append(tk.Label(master=self.tableau, text=ligne_base.Place))
            self.nombre_list[ligne].grid(row=ligne,column=3)

            self.detail_list.append(tk.Button(master=self.tableau, text="Selection", command= lambda var_ligne = ligne : self.Choix(var_ligne)))
            self.detail_list[ligne].grid(row=ligne,column=4)

            self.reserv_list.append(ligne_base.IdReservation)
            ligne += 1
        base.close()
    
    def Choix(self, ligne):
        global IdReservation
        IdReservation = self.reserv_list[ligne]
        for i in range(1,len(self.detail_list)):
            self.detail_list[i].configure(relief='raised')
        self.detail_list[ligne].configure(relief='sunken')
        self.buton.pack_forget()
        self.buton.pack()

class Presentation_Passager():
    def __init__(self):
        self.entete = tk.Frame()
        self.titre = tk.Frame()
        self.buton = tk.Frame()
        self.tableau = tk.Frame()
        
        self.titre_text = tk.Label(master=self.titre, text="Détail de la Reservation")
        self.titre_text.pack()

    def affiche(self):
        self.les_liste()
        self.lire_passager()
        self.entete.pack()
        self.titre.pack()
        self.tableau.pack()
        self.buton.pack()

    def cache(self):
        for widget in self.tableau.winfo_children():
            widget.destroy()
        self.entete.pack_forget()
        self.titre.pack_forget()
        self.buton.pack_forget()
        self.tableau.pack_forget()
        

    def les_liste(self):
        self.titre_1 = tk.Label(master=self.tableau, text="Circuit")
        self.titre_1.grid(row=0, column=0)

        self.titre_2 = tk.Label(master=self.tableau, text="Passagers")
        self.titre_2.grid(row=0, column=1)

        self.frame_1 = tk.Frame(master=self.tableau)
        self.frame_1.grid(row=1, column=0)
        self.frame_2 = tk.Frame(master=self.tableau)
        self.frame_2.grid(row=1, column=1)

        self.nom_list= []
        self.prenom_list= []
        self.confirm_list = []
        self.annuler_list = []
        self.Id_list = []

    def lire_passager(self):
        global IdReservation
        base =connexion.cursor()
        base.execute("Select Descriptif, VilleDepart, VilleArrivee, DateDepart, Duree, PaysDepart, PaysArrivee from Circuit inner join Reservation on Circuit.IdCircuit = Reservation.IdCircuit where IdReservation = ?;",[IdReservation])
        ligne_base = base.fetchone()

        message = ligne_base.Descriptif + " depuis " + ligne_base.VilleDepart + " en " + ligne_base.PaysDepart
        message += " jusqu'à " + ligne_base.VilleArrivee + " en " + ligne_base.PaysArrivee + "."
        message += " Le cicruit commence le " + ligne_base.DateDepart
        message += " et durera " + str(ligne_base.Duree) + " jours."
        circuit = tk.Label(master=self.frame_1, text=message)
        circuit.pack()
        
        base.execute("select Nom, Prenom, Personne.IdPersonne from Groupe inner join Personne on Groupe.IdPersonne = Personne.IdPersonne where IdReservation = ?;",[IdReservation])
        ligne = 0
        for ligne_base in base:
            self.nom_list.append(tk.Label(master=self.frame_2, text=ligne_base.Nom))
            self.nom_list[ligne].grid(row=ligne, column =0)

            self.prenom_list.append(tk.Label(master=self.frame_2, text=ligne_base.Prenom))
            self.prenom_list[ligne].grid(row=ligne, column =1)

            self.confirm_list.append(tk.Button(master=self.frame_2, text="Confirmer", command = lambda var_ligne = ligne : self.confirmation(var_ligne)))
            self.confirm_list[ligne].grid(row=ligne, column =2)

            self.annuler_list.append(tk.Button(master=self.frame_2, text="Annuler", command = lambda var_ligne = ligne : self.annulation(var_ligne)))
            self.annuler_list[ligne].grid(row=ligne, column =3)

            self.Id_list.append(ligne_base.IdPersonne)
            ligne +=1
        base.close()
    
    def confirmation(self, ligne):
        global IdReservation
        confirmer_groupe(self.Id_list[ligne], IdReservation)
        connexion.commit()
    
    def annulation(self,ligne):
        global IdReservation
        jour = datetime.today()
        jour_string = jour.strftime("%Y-%m-%d")
        annuler_groupe(self.Id_list[ligne], IdReservation, jour_string)
        connexion.commit()

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
        for widget in self.tableau.winfo_children():
            widget.destroy()
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
        if input_test_text(self.nom_modif.get(), 24):
            Error= True
        if input_test_text(self.prenom_modif.get(), 24):
            Error= True
        if input_test_text(self.user_modif.get(), 50):
            Error= True
        if input_test_text(self.pwd_modif.get(), 50):
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
        if input_test_text(self.nom_ajout.get(), 24):
            Error= True
        if input_test_text(self.prenom_ajout.get(), 24):
            Error= True
        if input_test_text(self.user_ajout.get(), 50):
            Error= True
        if input_test_text(self.pwd_ajout.get(), 50):
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
        for widget in self.tableau.winfo_children():
            widget.destroy()
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
        if input_test_text(self.nom_modif.get(), 24):
            Error= True
        if input_test_text(self.ville_modif.get(), 24):
            Error= True
        if input_test_text(self.pays_modif.get(), 24):
            Error= True
        if input_test_text(self.descriptifs_modif.get(), 250):
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
        if input_test_text(self.nom_ajout.get(), 24):
            Error= True
        if input_test_text(self.ville_ajout.get(), 24):
            Error= True
        if input_test_text(self.pays_ajout.get(), 24):
            Error= True
        if input_test_text(self.descriptifs_ajout.get(), 250):
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
        for widget in self.tableau.winfo_children():
            widget.destroy()
        self.entete.pack_forget()
        self.titre.pack_forget()
        self.buton.pack_forget()
        self.tableau.pack_forget()
        self.grand_buton_ajout.destroy()

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
            self.circuit_list[ligne_nb].grid(row=ligne_nb,column=0)

            self.ordre_list.append(tk.Label(master=self.tableau, text=ligne_base.Ordre))
            self.ordre_list[ligne_nb].grid(row=ligne_nb,column=1)

            self.date_list.append(tk.Label(master=self.tableau, text=ligne_base.DateEtape))
            self.date_list[ligne_nb].grid(row=ligne_nb,column=2)

            self.duree_list.append(tk.Label(master=self.tableau, text=ligne_base.Duree))
            self.duree_list[ligne_nb].grid(row=ligne_nb,column=3)

            self.nom_list.append(tk.Label(master=self.tableau, text=ligne_base.NomLieu))
            self.nom_list[ligne_nb].grid(row=ligne_nb,column=4)

            self.ville_list.append(tk.Label(master=self.tableau, text=ligne_base.Ville))
            self.ville_list[ligne_nb].grid(row=ligne_nb,column=5)

            self.pays_list.append(tk.Label(master=self.tableau, text=ligne_base.Pays))
            self.pays_list[ligne_nb].grid(row=ligne_nb,column=6)

            self.suppr_list.append(tk.Button(master=self.tableau, text="Supprimer", command= lambda var_ligne = ligne_nb : self.Supprime(var_ligne, ligne_nb)))
            self.suppr_list[ligne_nb].grid(row=ligne_nb,column=7)

            self.modif_list.append(tk.Button(master=self.tableau, text="Modifier", command=lambda var_ligne = ligne_nb : self.modifier_active(var_ligne)))
            self.modif_list[ligne_nb].grid(row=ligne_nb,column=8)
            ligne_nb = ligne_nb + 1
        base.close()
        self.grand_buton_ajout = tk.Button(master=self.buton, text= "Ajouter",command= lambda: self.Ajout_form(ligne_nb))
        self.grand_buton_ajout.pack()

    def Ajout_form(self, ligne):
        base = connexion.cursor()
        base.execute("select IdCircuit from Circuit;")
        Ids = []
        for ligne_base in base:
            Ids.append(ligne_base.IdCircuit)
        base.execute("select NomLieu, Ville, Pays from Lieu;")
        Lieux = [[], [], []]
        for ligne_base in base:
            Lieux[0].append(ligne_base.NomLieu)
            Lieux[1].append(ligne_base.Ville)
            Lieux[2].append(ligne_base.Pays)
        base.close()
        
        #on fait apparaître les Entrys
        self.circuit_ajout = tk.ttk.Combobox(master=self.tableau, values = Ids)
        self.circuit_ajout.grid(row=ligne,column=0)

        self.ordre_ajout = tk.Label(master=self.tableau)
        self.ordre_ajout.grid(row=ligne,column=1)

        self.date_ajout = tk.Entry(master=self.tableau)
        self.date_ajout.grid(row=ligne,column=2)

        self.duree_ajout = tk.Entry(master=self.tableau)
        self.duree_ajout.grid(row=ligne,column=3)

        self.nom_ajout = tk.ttk.Combobox(master=self.tableau, values = Lieux[0])
        self.nom_ajout.grid(row=ligne,column=4)

        self.ville_ajout = tk.ttk.Combobox(master=self.tableau, values = Lieux[1])
        self.ville_ajout.grid(row=ligne,column=5)

        self.pays_ajout = tk.ttk.Combobox(master=self.tableau, values = Lieux[2])
        self.pays_ajout.grid(row=ligne,column=6)

        self.buton_ajout = tk.Button(master=self.tableau, text="Validation", command= lambda: self.Ajout_action())
        self.buton_ajout.grid(row=ligne,column=7)

    def Ajout_action(self):
        print(self.ville_ajout.get())
        Error = False
        if not input_test_date(self.date_ajout.get()):
            Error= True
        try :
            int(self.duree_ajout.get())
        except:
            Error= True
        if not Error:
            ajout_etape(self.circuit_ajout.get(), self.date_ajout.get(), self.duree_ajout.get(), self.nom_ajout.get(), self.ville_ajout.get(), self.pays_ajout.get())
            connexion.commit()
            self.circuit_ajout.grid_forget()
            self.date_ajout.grid_forget()
            self.duree_ajout.grid_forget()
            self.nom_ajout.grid_forget()
            self.ville_ajout.grid_forget()
            self.pays_ajout.grid_forget()
            self.buton_ajout.grid_forget()
            self.cache()
            self.affiche()

    def Supprime(self, ligne, ligne_max):
        suprime_etape(int(self.circuit_list[ligne].cget("text")), self.ordre_list[ligne].cget("text"))
        connexion.commit()
        for i in range(1,ligne_max):
            self.circuit_list[i].grid_forget()
            self.ordre_list[i].grid_forget()
            self.date_list[i].grid_forget()
            self.duree_list[i].grid_forget()
            self.nom_list[i].grid_forget()
            self.ville_list[i].grid_forget()
            self.pays_list[i].grid_forget()
            self.suppr_list[i].grid_forget()
            self.modif_list[i].grid_forget()
        self.cache()
        self.affiche()

    def modifier_active(self, ligne_nb):
        self.date_list[ligne_nb].grid_forget()
        self.duree_list[ligne_nb].grid_forget()
        self.modif_list[ligne_nb].grid_forget()
        self.suppr_list[ligne_nb].grid_forget()

        self.date_modif = tk.Entry(master=self.tableau)
        self.date_modif.insert(0, self.date_list[ligne_nb].cget("text"))
        self.date_modif.grid(row=ligne_nb, column=2)

        self.duree_modif = tk.Entry(master=self.tableau)
        self.duree_modif.insert(0, self.duree_list[ligne_nb].cget("text"))
        self.duree_modif.grid(row=ligne_nb, column=3)

        self.suppr_modif = tk.Label(master=self.tableau, text="Supprimer")
        self.suppr_modif.grid(row=ligne_nb, column=7)

        self.modif_modif = tk.Button(master=self.tableau, text="Modifier",command=lambda : self.modifier_enregistre(ligne_nb))
        self.modif_modif.grid(row=ligne_nb, column=8)

    def modifier_enregistre(self, ligne_nb):
        Error = False
        if not input_test_date(self.date_modif.get()):
            Error = True
        try :
            int(self.duree_modif.get())
        except:
            Error= True
        if not Error:
            update_etape(self.circuit_list[ligne_nb].cget("text"), self.ordre_list[ligne_nb].cget("text"),self.date_modif.get(),self.duree_modif.get())

            self.date_modif.grid_forget()
            self.duree_modif.grid_forget()
            self.modif_modif.grid_forget()
            self.suppr_modif.grid_forget()
            self.cache()
            self.affiche()

class Liste_Client():
    def __init__(self):
        self.entete = tk.Frame()
        self.titre = tk.Frame()
        self.buton = tk.Frame()
        self.tableau = tk.Frame()
        
        self.titre_text = tk.Label(master=self.titre, text="Listes des Clients")
        self.titre_text.pack()

    
    def affiche(self):
        self.les_liste()
        self.lire_client()
        self.entete.pack()
        self.titre.pack()
        self.buton.pack()
        self.tableau.pack()

    def cache(self):
        for widget in self.tableau.winfo_children():
            widget.destroy()
        self.entete.pack_forget()
        self.titre.pack_forget()
        self.buton.pack_forget()
        self.tableau.pack_forget()
        #self.grand_buton_ajout.destroy()

    def les_liste(self):
        
        self.nom_list = []
        self.nom_list.append(tk.Label(master=self.tableau, text="Nom"))
        self.nom_list[0].grid(row=0, column=0)

        self.prenom_list = []
        self.prenom_list.append(tk.Label(master=self.tableau, text="Prenom"))
        self.prenom_list[0].grid(row=0, column=1)

        self.mail_list = []
        self.mail_list.append(tk.Label(master=self.tableau, text="Mail"))
        self.mail_list[0].grid(row=0, column=2)

        self.date_list = []
        self.date_list.append(tk.Label(master=self.tableau, text="Date de Naissance"))
        self.date_list[0].grid(row=0, column=3)

        self.circuits_list = []
        self.circuits_list.append(tk.Label(master=self.tableau, text="Circuits Choisit"))
        self.circuits_list[0].grid(row=0, column=4)

        self.Id_list= []

        self.suppr_list = []
        self.suppr_list.append(tk.Label(master=self.tableau, text="Supprimer"))
        self.suppr_list[0].grid(row=0,column=5)

        self.modif_list = []
        self.modif_list.append(tk.Label(master=self.tableau, text="Modifier"))
        self.modif_list[0].grid(row=0,column=6)

    def lire_client(self):
        base = connexion.cursor()
        base.execute("select Client.IdPersonne, Nom, Prenom, DateNaissance, Mail from Personne inner join Client on Personne.IdPersonne = Client.IdPersonne;")
        ligne_nb = 1
        for ligne_base in base:
            self.Id_list.append(ligne_base.IdPersonne)

            self.nom_list.append(tk.Label(master=self.tableau, text=ligne_base.Nom))
            self.nom_list[ligne_nb].grid(row=ligne_nb,column=0)

            self.prenom_list.append(tk.Label(master=self.tableau, text=ligne_base.Prenom))
            self.prenom_list[ligne_nb].grid(row=ligne_nb,column=1)

            self.date_list.append(tk.Label(master=self.tableau, text=ligne_base.DateNaissance))
            self.date_list[ligne_nb].grid(row=ligne_nb,column=3)

            self.mail_list.append(tk.Label(master=self.tableau, text=ligne_base.Mail))
            self.mail_list[ligne_nb].grid(row=ligne_nb,column=2)

            self.circuits_list.append(tk.Frame(master=self.tableau))
            self.circuits_list[ligne_nb].grid(row=ligne_nb,column=4)

            self.suppr_list.append(tk.Button(master=self.tableau, text="Supprimer", command = lambda var_ligne = ligne_nb:self.Supprime(var_ligne, ligne_nb)))
            self.suppr_list[ligne_nb].grid(row=ligne_nb,column=5)

            self.modif_list.append(tk.Button(master=self.tableau, text="Modifier",command=lambda var_ligne = ligne_nb : self.modifier_active(var_ligne)))
            self.modif_list[ligne_nb].grid(row=ligne_nb,column=6)
            ligne_nb = ligne_nb + 1
       
        #self.grand_buton_ajout = tk.Button(master=self.buton, text= "Ajouter")#command= lambda: self.Ajout_form(ligne_nb)
        #self.grand_buton_ajout.pack()
        #maintenant les circuits
        for ligne in range(ligne_nb-1):
            base.execute("select IdCircuit from Reservation where IdPersonne = ?;", [self.Id_list[ligne]])
            list_circuit = []
            index = 0
            for ligne_base in base:
                list_circuit.append(tk.Label(master=self.circuits_list[ligne], text=ligne_base.IdCircuit))
                list_circuit[index].pack()
                index = index +1

        base.close()

    def Supprime(self, ligne, ligne_max):
        supprime_client(self.Id_list[ligne])
        connexion.commit()
        for i in range(1,ligne_max):
            self.nom_list[i].destroy()
            self.prenom_list[i].destroy()
            self.date_list[i].destroy()
            self.mail_list[i].destroy()
            self.circuits_list[i].destroy()
            self.suppr_list[i].destroy()
            self.modif_list[i].destroy()
        self.cache()
        self.affiche()
    
    def modifier_active(self, ligne):
        self.nom_list[ligne].grid_forget()
        self.prenom_list[ligne].grid_forget()
        self.date_list[ligne].grid_forget()
        self.mail_list[ligne].grid_forget()
        self.modif_list[ligne].grid_forget()
        self.suppr_list[ligne].grid_forget()

        self.nom_modif = tk.Entry(master=self.tableau)
        self.nom_modif.insert(0, self.nom_list[ligne].cget("text"))
        self.nom_modif.grid(row=ligne, column=0)

        self.prenom_modif = tk.Entry(master=self.tableau)
        self.prenom_modif.insert(0, self.prenom_list[ligne].cget("text"))
        self.prenom_modif.grid(row=ligne, column=1)

        self.mail_modif = tk.Entry(master=self.tableau)
        self.mail_modif.insert(0, self.mail_list[ligne].cget("text"))
        self.mail_modif.grid(row=ligne, column=2)

        self.date_modif = tk.Entry(master=self.tableau)
        self.date_modif.insert(0, self.date_list[ligne].cget("text"))
        self.date_modif.grid(row=ligne, column=3)  

        self.suppr_modif = tk.Label(master=self.tableau, text="Supprimer")
        self.suppr_modif.grid(row=ligne, column=5)

        self.modif_modif = tk.Button(master=self.tableau, text="Modifier",command=lambda : self.modifier_enregistre(ligne))
        self.modif_modif.grid(row=ligne, column=6)

    def modifier_enregistre(self, ligne):
        Error = False
        if input_test_text(self.nom_modif.get(), 24):
            Error= True
        if input_test_text(self.prenom_modif.get(), 24):
            Error= True
        if not input_test_date(self.date_modif.get()):
            Error= True
        if not input_test_mail(self.mail_modif.get()):
            Error= True
        if not Error:
            update_client_admin(self.nom_modif.get(), self.prenom_modif.get(), self.date_modif.get(), self.mail_modif.get(), self.Id_list[ligne-1])
            connexion.commit()
            #forget les entrys et recharge la page
            self.nom_modif.grid_forget()
            self.prenom_modif.grid_forget()
            self.date_modif.grid_forget()
            self.mail_modif.grid_forget()
            self.cache()
            self.affiche()

class Liste_Circuit():
    def __init__(self):
        self.entete = tk.Frame()
        self.titre = tk.Frame()
        self.buton = tk.Frame()
        self.tableau = tk.Frame()
        
        self.titre_text = tk.Label(master=self.titre, text="Listes des Circuit")
        self.titre_text.pack()

    
    def affiche(self):
        self.les_liste()
        self.lire_circuit()
        self.entete.pack()
        self.titre.pack()
        self.buton.pack()
        self.tableau.pack()

    def cache(self):
        for widget in self.tableau.winfo_children():
            widget.destroy()
        self.entete.pack_forget()
        self.titre.pack_forget()
        self.buton.pack_forget()
        self.tableau.pack_forget()
        self.grand_buton_ajout.destroy()

    def les_liste(self):
        self.Id_list = []
        self.Id_list.append(tk.Label(master=self.tableau, text="Numéro du Circuit"))
        self.Id_list[0].grid(row=0, column=0)

        self.descriptif_list = []
        self.descriptif_list.append(tk.Label(master=self.tableau, text="Description"))
        self.descriptif_list[0].grid(row=0, column=1)

        self.ville_depart_list = []
        self.ville_depart_list.append(tk.Label(master=self.tableau, text="Ville de Départ"))
        self.ville_depart_list[0].grid(row=0, column=2)

        self.ville_arrivee_list = []
        self.ville_arrivee_list.append(tk.Label(master=self.tableau, text="Ville d'Arrivée"))
        self.ville_arrivee_list[0].grid(row=0, column=3)

        self.pays_depart_list = []
        self.pays_depart_list.append(tk.Label(master=self.tableau, text="Pays de Départ"))
        self.pays_depart_list[0].grid(row=0, column=4)

        self.pays_arrivee_list = []
        self.pays_arrivee_list.append(tk.Label(master=self.tableau, text="Pays d'Arrivée"))
        self.pays_arrivee_list[0].grid(row=0, column=5)

        self.date_list = []
        self.date_list.append(tk.Label(master=self.tableau, text="Date de Départ"))
        self.date_list[0].grid(row=0, column=6)

        self.places_list = []
        self.places_list.append(tk.Label(master=self.tableau, text="Nombre de Place Disponible"))
        self.places_list[0].grid(row=0, column=7)

        self.duree_list = []
        self.duree_list.append(tk.Label(master=self.tableau, text="Durée"))
        self.duree_list[0].grid(row=0, column=8)

        self.prix_list = []
        self.prix_list.append(tk.Label(master=self.tableau, text="Prix d'Inscription"))
        self.prix_list[0].grid(row=0, column=9)

        self.detail_list = []
        self.detail_list.append(tk.Label(master=self.tableau, text="Passagers"))
        self.detail_list[0].grid(row=0, column=10)

        self.suppr_list = []
        self.suppr_list.append(tk.Label(master=self.tableau, text="Supprimer"))
        self.suppr_list[0].grid(row=0, column=11)

        self.modif_list = []
        self.modif_list.append(tk.Label(master=self.tableau, text="Modifier"))
        self.modif_list[0].grid(row=0, column=12)

    def lire_circuit(self):
        base = connexion.cursor()
        base.execute("select * from Circuit;")
        ligne_nb = 1
        for ligne_base in base:
            self.Id_list.append(tk.Label(master=self.tableau, text=ligne_base.IdCircuit))
            self.Id_list[ligne_nb].grid(row=ligne_nb,column=0)

            self.descriptif_list.append(tk.Label(master=self.tableau, text=ligne_base.Descriptif))
            self.descriptif_list[ligne_nb].grid(row=ligne_nb,column=1)

            self.ville_depart_list.append(tk.Label(master=self.tableau, text=ligne_base.VilleDepart))
            self.ville_depart_list[ligne_nb].grid(row=ligne_nb,column=2)

            self.ville_arrivee_list.append(tk.Label(master=self.tableau, text=ligne_base.VilleArrivee))
            self.ville_arrivee_list[ligne_nb].grid(row=ligne_nb,column=3)

            self.pays_depart_list.append(tk.Label(master=self.tableau, text=ligne_base.PaysDepart))
            self.pays_depart_list[ligne_nb].grid(row=ligne_nb,column=4)

            self.pays_arrivee_list.append(tk.Label(master=self.tableau, text=ligne_base.PaysArrivee))
            self.pays_arrivee_list[ligne_nb].grid(row=ligne_nb,column=5)

            self.date_list.append(tk.Label(master=self.tableau, text=ligne_base.DateDepart))
            self.date_list[ligne_nb].grid(row=ligne_nb,column=6)

            self.places_list.append(tk.Label(master=self.tableau, text=ligne_base.NbPlaceDisponible))
            self.places_list[ligne_nb].grid(row=ligne_nb,column=7)

            self.duree_list.append(tk.Label(master=self.tableau, text=ligne_base.Duree))
            self.duree_list[ligne_nb].grid(row=ligne_nb,column=8)

            self.prix_list.append(tk.Label(master=self.tableau, text=ligne_base.PrixInscription))
            self.prix_list[ligne_nb].grid(row=ligne_nb,column=9)

            self.detail_list.append(tk.Button(master=self.tableau, text="Details", command = lambda var_ligne = ligne_nb : self.detail(var_ligne)))
            self.detail_list[ligne_nb].grid(row=ligne_nb,column=10)

            self.suppr_list.append(tk.Button(master=self.tableau, text="Supprimer", command= lambda var_ligne = ligne_nb : self.Supprime(var_ligne)))
            self.suppr_list[ligne_nb].grid(row=ligne_nb,column=11)

            self.modif_list.append(tk.Button(master=self.tableau, text="Modifier", command= lambda var_ligne = ligne_nb : self.modifier_active(var_ligne)))
            self.modif_list[ligne_nb].grid(row=ligne_nb,column=12)
            ligne_nb = ligne_nb +1
        base.close()
        self.grand_buton_ajout = tk.Button(master=self.buton, text= "Ajouter",command= lambda: self.Ajout_form(ligne_nb))
        self.grand_buton_ajout.pack()

    def detail(self, ligne):
        Passagers = Liste_Passager(self.Id_list[ligne].cget("text"))
        Passagers.affiche()


    def Ajout_form(self, ligne_nb):
        self.descriptif_ajout = tk.Entry(master=self.tableau)
        self.descriptif_ajout.grid(row=ligne_nb,column=1)

        self.ville_depart_ajout = tk.Entry(master=self.tableau)
        self.ville_depart_ajout.grid(row=ligne_nb,column=2)

        self.ville_arrivee_ajout = tk.Entry(master=self.tableau)
        self.ville_arrivee_ajout.grid(row=ligne_nb,column=3)

        self.pays_depart_ajout = tk.Entry(master=self.tableau)
        self.pays_depart_ajout.grid(row=ligne_nb,column=4)

        self.pays_arrivee_ajout = tk.Entry(master=self.tableau)
        self.pays_arrivee_ajout.grid(row=ligne_nb,column=5)

        self.date_ajout = tk.Entry(master=self.tableau)
        self.date_ajout.grid(row=ligne_nb,column=6)

        self.places_ajout = tk.Entry(master=self.tableau)
        self.places_ajout.grid(row=ligne_nb,column=7)

        self.duree_ajout = tk.Entry(master=self.tableau)
        self.duree_ajout.grid(row=ligne_nb,column=8)

        self.prix_ajout = tk.Entry(master=self.tableau)
        self.prix_ajout.grid(row=ligne_nb,column=9)

        self.buton_ajout = tk.Button(master=self.tableau, text="Validation", command= lambda: self.Ajout_action())
        self.buton_ajout.grid(row=ligne_nb,column=10)

    def Ajout_action(self):
        Error = False
        if input_test_text(self.descriptif_ajout.get(), 200):
            Error= True
        if input_test_text(self.ville_depart_ajout.get(), 24):
            Error= True
        if input_test_text(self.ville_arrivee_ajout.get(), 24):
            Error= True
        if input_test_text(self.pays_depart_ajout.get(), 24):
            Error= True
        if input_test_text(self.pays_arrivee_ajout.get(), 24):
            Error= True
        if not input_test_date(self.date_ajout.get()):
            Error= True
        try :
            int(self.places_ajout.get())
            int(self.duree_ajout.get())
            float(self.prix_ajout.get())
        except:
            Error= True
        if not Error:
            ajout_circuit(self.descriptif_ajout.get(), self.ville_depart_ajout.get(), self.ville_arrivee_ajout.get(), self.pays_depart_ajout.get(), self.pays_arrivee_ajout.get(), self.date_ajout.get(), self.places_ajout.get(), self.duree_ajout.get(), self.prix_ajout.get())
            connexion.commit()
            self.cache()
            self.affiche()

    def Supprime(self, ligne):
        if supprime_circuit(int(self.Id_list[ligne].cget("text"))):
            connexion.commit()
            self.cache()
            self.affiche()

    def modifier_active(self, ligne_nb):
        self.descriptif_list[ligne_nb].grid_forget()
        self.ville_depart_list[ligne_nb].grid_forget()
        self.ville_arrivee_list[ligne_nb].grid_forget()
        self.pays_depart_list[ligne_nb].grid_forget()
        self.pays_arrivee_list[ligne_nb].grid_forget()
        self.date_list[ligne_nb].grid_forget()
        self.places_list[ligne_nb].grid_forget()
        self.duree_list[ligne_nb].grid_forget()
        self.prix_list[ligne_nb].grid_forget()
        self.detail_list[ligne_nb].grid_forget()
        self.suppr_list[ligne_nb].grid_forget()
        self.modif_list[ligne_nb].grid_forget()

        #création des Entry
        self.descriptif_modif = tk.Entry(master=self.tableau)
        self.descriptif_modif.insert(0, self.descriptif_list[ligne_nb].cget("text"))
        self.descriptif_modif.grid(row=ligne_nb,column=1)

        self.ville_depart_modif = tk.Entry(master=self.tableau)
        self.ville_depart_modif.insert(0, self.ville_depart_list[ligne_nb].cget("text"))
        self.ville_depart_modif.grid(row=ligne_nb,column=2)

        self.ville_arrivee_modif = tk.Entry(master=self.tableau)
        self.ville_arrivee_modif.insert(0, self.ville_arrivee_list[ligne_nb].cget("text"))
        self.ville_arrivee_modif.grid(row=ligne_nb,column=3)

        self.pays_depart_modif = tk.Entry(master=self.tableau)
        self.pays_depart_modif.insert(0, self.pays_depart_list[ligne_nb].cget("text"))
        self.pays_depart_modif.grid(row=ligne_nb,column=4)

        self.pays_arrivee_modif = tk.Entry(master=self.tableau)
        self.pays_arrivee_modif.insert(0, self.pays_arrivee_list[ligne_nb].cget("text"))
        self.pays_arrivee_modif.grid(row=ligne_nb,column=5)

        self.date_modif = tk.Entry(master=self.tableau)
        self.date_modif.insert(0, self.date_list[ligne_nb].cget("text"))
        self.date_modif.grid(row=ligne_nb,column=6)

        self.places_modif = tk.Entry(master=self.tableau)
        self.places_modif.insert(0, self.places_list[ligne_nb].cget("text"))
        self.places_modif.grid(row=ligne_nb,column=7)

        self.duree_modif = tk.Entry(master=self.tableau)
        self.duree_modif.insert(0, self.duree_list[ligne_nb].cget("text"))
        self.duree_modif.grid(row=ligne_nb,column=8)

        self.prix_modif = tk.Entry(master=self.tableau)
        self.prix_modif.insert(0, self.prix_list[ligne_nb].cget("text"))
        self.prix_modif.grid(row=ligne_nb,column=9)

        self.detail_modif = tk.Label(master=self.tableau, text="Details")
        self.detail_modif.grid(row=ligne_nb,column=10)
        
        self.suppr_modif = tk.Label(master=self.tableau, text="Supprimer")
        self.suppr_modif.grid(row=ligne_nb,column=11)
        
        self.modif_modif = tk.Button(master=self.tableau, text="Modifier", command= lambda: self.modifier_enregistre(ligne_nb))
        self.modif_modif.grid(row=ligne_nb,column=12)

    def modifier_enregistre(self, ligne):
        Error = False
        if input_test_text(self.descriptif_modif.get(), 200):
            Error= True
        if input_test_text(self.ville_depart_modif.get(), 24):
            Error= True
        if input_test_text(self.ville_arrivee_modif.get(), 24):
            Error= True
        if input_test_text(self.pays_depart_modif.get(), 24):
            Error= True
        if input_test_text(self.pays_arrivee_modif.get(), 24):
            Error= True
        if not input_test_date(self.date_modif.get()):
            Error= True
        try :
            int(self.places_modif.get())
            int(self.duree_modif.get())
            float(self.prix_modif.get())
        except:
            Error= True
        if not Error:
            update_circuit(self.Id_list[ligne].cget("text"),self.descriptif_modif.get(),self.ville_depart_modif.get(),self.ville_arrivee_modif.get(),self.pays_depart_modif.get(),self.pays_arrivee_modif.get(),self.date_modif.get(),self.places_modif.get(),self.duree_modif.get(),self.prix_modif.get())
            connexion.commit()
            self.cache()
            self.affiche()

class Liste_Passager():
    def __init__(self, Idcircuit):
        self.ecran_secondaire = tk.Tk()
        self.entete = tk.Frame(master=self.ecran_secondaire)
        self.titre = tk.Frame(master=self.ecran_secondaire)
        self.buton = tk.Frame(master=self.ecran_secondaire)
        self.tableau = tk.Frame(master=self.ecran_secondaire)
        
        self.titre_text = tk.Label(master=self.titre, text="Listes des Passagers")
        self.titre_text.pack()

        self.Idcircuit = Idcircuit
    
    def retour(self):
        self.ecran_secondaire.destroy()

    def affiche(self):
        self.les_liste()
        self.lire_passager()
        self.entete.pack()
        self.titre.pack()
        self.buton.pack()
        self.tableau.pack()
        self.ecran_secondaire.mainloop()

    def cache(self):
        for widget in self.tableau.winfo_children():
            widget.destroy()
        self.entete.pack_forget()
        self.titre.pack_forget()
        self.buton.pack_forget()
        self.tableau.pack_forget()
        #self.grand_buton_ajout.destroy()
        self.grand_buton_retour.destroy()
        self.Circuit.destroy()

    def les_liste(self):
        
        self.nom_list = []
        self.nom_list.append(tk.Label(master=self.tableau, text="Nom"))
        self.nom_list[0].grid(row=0, column=0)

        self.prenom_list = []
        self.prenom_list.append(tk.Label(master=self.tableau, text="Prenom"))
        self.prenom_list[0].grid(row=0, column=1)

        self.date_list = []
        self.date_list.append(tk.Label(master=self.tableau, text="Date de Naissance"))
        self.date_list[0].grid(row=0, column=2)

        self.Id_list= []
        self.Id_list.append(0)

        self.Idreservation_list = []
        self.Idreservation_list.append(0)

        self.Confirmation_list = []
        self.Confirmation_list.append(0)

        self.suppr_list = []
        self.suppr_list.append(tk.Label(master=self.tableau, text="Supprimer"))
        self.suppr_list[0].grid(row=0,column=3)

        self.modif_list = []
        self.modif_list.append(tk.Label(master=self.tableau, text="Annuler"))
        self.modif_list[0].grid(row=0,column=4)

    def lire_passager(self):
        base = connexion.cursor()
        base.execute("select Passager.IdPersonne, Nom, Prenom, DateNaissance, Confirmation, Reservation.IdReservation from Personne, Passager, Groupe, Reservation where Personne.IdPersonne = Passager.IdPersonne and Passager.IdPersonne = Groupe.IdPersonne and Reservation.IdReservation = Groupe.IdReservation and Reservation.IdCircuit = ?;",[self.Idcircuit])
        ligne_nb = 1
        for ligne_base in base:
            self.Id_list.append(ligne_base.IdPersonne)
            self.Idreservation_list.append(ligne_base.IdReservation)
            self.Confirmation_list.append(ligne_base.Confirmation)

            self.nom_list.append(tk.Label(master=self.tableau, text=ligne_base.Nom))
            self.nom_list[ligne_nb].grid(row=ligne_nb,column=0)

            self.prenom_list.append(tk.Label(master=self.tableau, text=ligne_base.Prenom))
            self.prenom_list[ligne_nb].grid(row=ligne_nb,column=1)

            self.date_list.append(tk.Label(master=self.tableau, text=ligne_base.DateNaissance))
            self.date_list[ligne_nb].grid(row=ligne_nb,column=2)


            self.suppr_list.append(tk.Button(master=self.tableau, text="Supprimer", command = lambda var_ligne = ligne_nb:self.Supprime(var_ligne)))
            self.suppr_list[ligne_nb].grid(row=ligne_nb,column=3)

            self.modif_list.append(tk.Button(master=self.tableau, text="Annuler", command = lambda var_ligne = ligne_nb:self.Annuler(var_ligne)))
            self.modif_list[ligne_nb].grid(row=ligne_nb,column=4)
            ligne_nb = ligne_nb + 1
       
        #self.grand_buton_ajout = tk.Button(master=self.buton, text= "Ajouter", command= lambda: self.Ajout_form(ligne_nb))
        #self.grand_buton_ajout.pack()
        self.grand_buton_retour =tk.Button(master=self.buton, text= "Retour aux Circuits", command= lambda: self.retour())
        self.grand_buton_retour.grid(row=0, column=1)
        message = "Circuit : " + str(self.Idcircuit)
        self.Circuit = tk.Label(master=self.buton, text = message)
        self.Circuit.grid(row=0, column=0)
        base.close()

    def Supprime(self, ligne):
        supprime_groupe(self.Id_list[ligne],self.Idreservation_list[ligne])
        connexion.commit()
        self.cache()
        self.affiche()
    
    def Annuler(self, ligne):
        jour = datetime.date.today()
        jour_string = jour.strftime("%Y-%m-%d")
        annuler_groupe(self.Id_list[ligne],self.Idreservation_list[ligne], jour_string)
        connexion.commit()
        self.cache()
        self.affiche()

"""
    def Ajout_form(self, ligne):
        self.nom_ajout = tk.Entry(master=self.tableau)
        self.nom_ajout.grid(row=ligne, column=0)

        self.prenom_ajout = tk.Entry(master=self.tableau)
        self.prenom_ajout.grid(row=ligne, column=1)

        self.date_ajout = tk.Entry(master=self.tableau)
        self.date_ajout.grid(row=ligne, column=2)

        self.buton_ajout = tk.Button(master=self.tableau, text="Validation")
        self.buton_ajout.grid(row=ligne, column=3)

    def Ajout_action(self, ligne):
        Error = False
        if not input_test_text(self.nom_ajout.get(), 24):
            Error= True
        if not input_test_text(self.prenom_ajout.get(), 24):
            Error= True
        if not input_test_date(self.date_ajout.get()):
            Error= True
        if not Error:
            identification_passager(self.nom_ajout.get(), self.prenom_ajout.get(), self.date_ajout.get())
            #ajouter le passager à la reservation
            self.cache()
            self.affiche()
"""

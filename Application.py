from Pages import *

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
    ecran.geometry=("300x5000")
    ecran.resizable(width=0, height=0)#on met ces deux lignes et magie ça marche
    #initialisation des pages
    Login_page = Login()
    Creation_Client = create_compte()
    Accueil_Ad = Accueil_Admin()
    Accueil_Cl = Accueil_Client() #attention elle n'a aucun boutons pour l'instant
    Liste_Ad = Liste_Admin()
    Liste_Li = Liste_Lieux()
    
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
    administrateurs_a_a  = tk.Button(master=Accueil_Ad.buton, text="Listes Administrateurs", command= lambda: changement_page(Accueil_Ad, Liste_Ad))
    administrateurs_a_a.pack()
    circuits_a_a = tk.Button(master=Accueil_Ad.buton, text="Listes Circuits")
    circuits_a_a.pack()
    etapes_a_a = tk.Button(master=Accueil_Ad.buton, text="Listes Etapes")
    etapes_a_a.pack()
    lieux_a_a = tk.Button(master=Accueil_Ad.buton, text="Listes Lieux", command= lambda: changement_page(Accueil_Ad, Liste_Li))
    lieux_a_a.pack()
    accueil_admin_logout = tk.Button(master=Accueil_Ad.buton, text="log out", command= lambda: Log_Out(Login_page, Accueil_Ad))
    accueil_admin_logout.pack()
    #butons Liste Admin
    retour_la = tk.Button(master=Liste_Ad.entete, text="Retour à la liste des pages", command= lambda: changement_page(Liste_Ad, Accueil_Ad))
    retour_la.pack()
    #butons Liste Lieux
    retour_ll = tk.Button(master=Liste_Li.entete, text="Retour à la liste des pages", command= lambda: changement_page(Liste_Li, Accueil_Ad))
    retour_ll.pack()
    #Fonctionnement
    #Login_page.affiche()
    Liste_Li.affiche()
    ecran.mainloop()
    connexion.close()

Application()
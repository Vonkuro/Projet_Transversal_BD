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

def changement_vers_Pres_circuit(Accueil_Cl, Pres_Cir):
    
    if Accueil_Cl.verification() :
        Accueil_Cl.cache()
        Pres_Cir.affiche()

def changement_vers_Pres_etape(Pres_Cir, Pres_Et): #à corriger pour ne pas caché si Id =0
    Id = Pres_Cir.cache()
    if Id != 0:
        Pres_Et.affiche()
    else:
        Pres_Cir.affiche()

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
    Liste_Et = Liste_Etape()
    Liste_Cl = Liste_Client()
    Creation_Client_Admin = create_compte()
    Liste_Ci = Liste_Circuit()
    Pres_Cir = Presentation_Circuit()
    Pres_Et = Presentation_Etape()
    Res_Pa = Reservation_passager()
    Pres_Re = Presentation_Reservation()
    Pres_Pa = Presentation_Passager()
    
    #initialisation des boutons d'interaction entre les pages
    #butons Logins
    login = tk.Button(master=Login_page.buton, text="Connexion", command= lambda: Log_In(Login_page, Accueil_Ad, Accueil_Cl))
    login.pack()
    compte = tk.Button(master=Login_page.buton, text="créer un compte", command= lambda: changement_page(Login_page, Creation_Client))
    compte.pack()
    #butons Création de compte Client
    cree = tk.Button(master=Creation_Client.buton, text="créer", command= lambda: appel_envois(Creation_Client, Login_page))
    cree.pack()
    retour_cc = tk.Button(master=Creation_Client.titre, text="Retour", command= lambda: changement_page(Creation_Client, Login_page))
    retour_cc.pack()
    #butons Accueil Admin
    clients_a_a = tk.Button(master=Accueil_Ad.buton, text="Listes Clients", command= lambda: changement_page(Accueil_Ad, Liste_Cl))
    clients_a_a.pack()
    administrateurs_a_a  = tk.Button(master=Accueil_Ad.buton, text="Listes Administrateurs", command= lambda: changement_page(Accueil_Ad, Liste_Ad))
    administrateurs_a_a.pack()
    circuits_a_a = tk.Button(master=Accueil_Ad.buton, text="Listes Circuits", command= lambda: changement_page(Accueil_Ad, Liste_Ci))
    circuits_a_a.pack()
    etapes_a_a = tk.Button(master=Accueil_Ad.buton, text="Listes Etapes", command= lambda: changement_page(Accueil_Ad, Liste_Et))
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
    #butons Liste Etape
    retour_le = tk.Button(master=Liste_Et.entete, text="Retour à la liste des pages", command= lambda: changement_page(Liste_Et, Accueil_Ad))
    retour_le.pack()
    #butons Liste Client
    retour_lc = tk.Button(master=Liste_Cl.entete, text="Retour à la liste des pages", command= lambda: changement_page(Liste_Cl, Accueil_Ad))
    retour_lc.pack()
    compte_lc = tk.Button(master=Liste_Cl.buton, text="Ajouter un Client", command= lambda: changement_page(Liste_Cl, Creation_Client_Admin))
    compte_lc.pack()
    #butons Création de compte Client par Admin
    cree_admin = tk.Button(master=Creation_Client_Admin.buton, text="créer", command= lambda: appel_envois(Creation_Client_Admin, Liste_Cl))
    cree_admin.pack()
    #butons Liste Circuit
    retour_lci = tk.Button(master=Liste_Ci.entete, text="Retour à la liste des pages", command= lambda: changement_page(Liste_Ci, Accueil_Ad))
    retour_lci.pack()
    #butons Accuiel Client
    accueil_client_logout = tk.Button(master=Accueil_Cl.entete, text="log out", command= lambda: Log_Out(Login_page, Accueil_Cl))
    accueil_client_logout.pack()
    chercher_circuit = tk.Button(master=Accueil_Cl.buton, text="Voir les circuits disponibles", command= lambda: changement_vers_Pres_circuit(Accueil_Cl, Pres_Cir))
    chercher_circuit.grid(row=0, column=0)
    reservation_a_c = tk.Button(master=Accueil_Cl.buton, text="Voir mes reservations", command= lambda: changement_page(Accueil_Cl, Pres_Re))
    reservation_a_c.grid(row=0, column=1)
    #butons Présentation des Circuits
    retour_pc = tk.Button(master=Pres_Cir.entete, text="Retour à l'Accueil", command= lambda: changement_page(Pres_Cir, Accueil_Cl))
    retour_pc.pack()
    etapes_pc = tk.Button(master=Pres_Cir.entete, text="Détails du Circuit Selectionné", command= lambda: changement_vers_Pres_etape(Pres_Cir, Pres_Et))
    etapes_pc.pack()
    #butons Présentation des Etapes
    retour_pe = tk.Button(master=Pres_Et.entete, text="Retour à la Selection", command= lambda: changement_page(Pres_Et, Pres_Cir))
    retour_pe.pack()
    reserve_pe =tk.Button(master=Pres_Et.buton, text="Reserver", command= lambda: changement_page(Pres_Et, Res_Pa))
    reserve_pe.pack()
    #butons Reservation des passagers
    retour_rp = tk.Button(master=Res_Pa.buton_2, text="Retour à l'Accueil'", command= lambda: changement_page(Res_Pa, Accueil_Cl))
    retour_rp.pack()
    #butons Présention des reservations
    retour_pr = tk.Button(master=Pres_Re.entete, text="Retour à l'Accueil", command= lambda: changement_page(Pres_Re, Accueil_Cl))
    retour_pr.pack()
    details_pr =tk.Button(master=Pres_Re.buton, text="Details", command= lambda: changement_page(Pres_Re, Pres_Pa))
    details_pr.pack()
    #butons Présention des passagers
    retour_pp = tk.Button(master=Pres_Pa.entete, text="Retour à l'Accueil", command= lambda: changement_page(Pres_Pa, Accueil_Cl))
    retour_pp.pack()
    reserv_pp = tk.Button(master=Pres_Pa.buton, text="Retour aux reservations", command= lambda: changement_page(Pres_Pa, Accueil_Cl))
    reserv_pp.pack()
    #Fonctionnement
    Login_page.affiche()
    #Accueil_Cl.affiche()
    ecran.mainloop()
    connexion.close()

Application()
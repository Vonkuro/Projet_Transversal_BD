from Connexsion import *
import datetime

def verification_client(user, motsdepasse): #testé
    base = connexion.cursor()
    base.execute("select * from Client;")
    for ligne in base :
        if ligne.Identifiant == user and ligne.MotsdePasse == motsdepasse :
            base.close()
            return ligne.IdPersonne

    base.close()
    return 0

def verification_admin(user, motsdepasse): #testé
    base = connexion.cursor()
    base.execute("select * from Administrateur;")
    for ligne in base :
        if ligne.Identifiant == user and ligne.MotsdePasse == motsdepasse :
            base.close()
            return ligne.IdPersonne

    base.close()
    return 0

def ajout_client(user, motsdepasse, nom, prenom, datenaissance, mail): #testé
    base = connexion.cursor()

    demande = "insert into Personne(Nom, Prenom, DateNaissance, Mail) values ('" + nom + "', '" + prenom + "', '" + datenaissance + "', '" + mail
    demande = demande + "');"
    base.execute(demande)

    base.execute("select top 1 IdPersonne from Personne order by IdPersonne Desc")
    ligne = base.fetchone()
    Dernier_Id = str(ligne.IdPersonne)

    demande = "insert into Client(IdPersonne, Identifiant, MotsdePasse) values ('" + Dernier_Id + "', '" + user + "', '" + motsdepasse + "');"
    base.execute(demande)

    base.close()

def ajout_admin(user, motsdepasse, nom, prenom, datenaissance, mail): #testé
    base = connexion.cursor()
    
    base.execute("insert into Personne(Nom, Prenom, DateNaissance, Mail) values (?, ?, ?, ?);", [nom,prenom,datenaissance, mail])
    
    base.execute("select top 1 IdPersonne from Personne order by IdPersonne Desc")
    ligne = base.fetchone()
    Dernier_Id = ligne.IdPersonne

    base.execute("insert into Administrateur(IdPersonne, Identifiant, MotsdePasse) values (?, ?, ?);", [Dernier_Id, user, motsdepasse])

    base.close()

def ajout_reservation(Client, Circuit, Places, Date): #testé
    base = connexion.cursor()

    base.execute("INSERT INTO Reservation (Place , DateRevervation , Etat  , IdCircuit, IdPersonne) VALUES (?, ? , '1', ? , ? ) ; ", [Places, Date, Circuit, Client])

    base.execute("UPDATE Circuit SET NbPlaceDisponible= NbPlaceDisponible - ? where IdCircuit=? ;",[Places, Circuit])
    base.close()

def identification_passager(Nom, Prenom, DateNaissance): #testé
    #Prend le Nom, Prenom et date de naissance puis s'assure que la personne existe dans la base en tant que Passager
    #Si non, crée le Passager dans la baser
    #Renvoit l'IdPassager
    base = connexion.cursor()
    base.execute("Select * from Personne;")
    Id = 0
    for ligne in base :
        if Nom == ligne.Nom and Prenom == ligne.Prenom and DateNaissance == ligne.DateNaissance:
            Id = ligne.IdPersonne
    if Id == 0:

        base.execute("insert into Personne(Nom, Prenom, DateNaissance) values (?, ?, ?);", [Nom,Prenom,DateNaissance])

        base.execute("select top 1 IdPersonne from Personne order by IdPersonne Desc")
        ligne = base.fetchone()
        Dernier_Id = ligne.IdPersonne

        base.execute("insert into Passager(IdPersonne) values (?);",[Dernier_Id])
        Id = Dernier_Id
    else :
        base.execute("Select * from Passager where IdPersonne = ?;",[Id])
        ligne = base.fetchall()
        if len(ligne)==0:
            base.execute("insert into Passager(IdPersonne) values (?);",[Id])
    base.close()
    return Id

def ajout_circuit(Descriptif, Villedepart, Villearrivee, Paysdepart, Paysarrivee, Datedepart, Nbplacedisponible, Duree, Prixinscription):
    base = connexion.cursor() #testé

    Liste =[Descriptif, Villedepart, Villearrivee, Paysdepart, Paysarrivee, Datedepart, Nbplacedisponible, Duree, Prixinscription]
    base.execute("insert into Circuit(Descriptif, VilleDepart, VilleArrivee, PaysDepart, PaysArrivee, DateDepart, NbPlaceDisponible, Duree, PrixInscription) values (?,?,?,?,?,?,?,?,?);", Liste)
    base.close()

def prix_circuits(): #testé
    base = connexion.cursor()
    requette = "select Circuit.IdCircuit, PrixInscription + sum(Lieu.PrixVisite) as Prix_total"
    requette += " from Circuit, Etape inner join Lieu on (Etape.Pays = Lieu.Pays and Etape.Ville = Lieu.ville and Etape.NomLieu = Lieu.NomLieu)"
    requette += " where Circuit.IdCircuit = Etape.IdCircuit"
    requette += " group by Circuit.IdCircuit, Circuit.PrixInscription;"
    base.execute(requette)
    Liste_Prix = []
    for ligne in base:
        Liste_Prix.append([ligne.IdCircuit, float(ligne.Prix_total)])
    base.close()
    return Liste_Prix

def ajout_lieu(Nomlieu, Ville, Pays, Descriptif, Prixvisite): #testé
    #ATTENTION ! Cette fonction peut renvoyer une erreur Exception Lieu pre-exitant si le Lieu existe dans la BD
    base = connexion.cursor() 
    base.execute("Select NomLieu, Ville, Pays from Lieu;")
    for ligne in base :
        if Nomlieu == ligne.NomLieu and Ville == ligne.Ville and Pays == ligne.Pays :
            base.close()
            raise Exception('Lieu pre-existant')
    
    base.execute("insert into Lieu(NomLieu, Ville, Pays, Descriptif, PrixVisite) values (?,?,?,?,?);",[Nomlieu, Ville, Pays, Descriptif, Prixvisite])
    base.close()

def miseajour_lieu(): #testé
    base = connexion.cursor()
    Lieux_suprime = []
    requette = "Select Lieu.NomLieu, Lieu.Ville, Lieu.Pays"
    requette += " from Lieu"
    requette += " where Lieu.NomLieu not in ("
    requette += "Select Etape.NomLieu from Etape, Lieu where Etape.NomLieu = Lieu.NomLieu and  Etape.Ville = Lieu.Ville and Etape.Pays = Lieu.Pays)"
    requette += " and Lieu.Ville not in ("
    requette += "Select Etape.Ville from Etape, Lieu where Etape.NomLieu = Lieu.NomLieu and  Etape.Ville = Lieu.Ville and Etape.Pays = Lieu.Pays)"
    requette += " and Lieu.Pays not in ("
    requette += "Select Etape.Pays from Etape, Lieu where Etape.NomLieu = Lieu.NomLieu and  Etape.Ville = Lieu.Ville and Etape.Pays = Lieu.Pays);"
    base.execute(requette)
    for ligne in base :
        Lieux_suprime.append([ligne.NomLieu, ligne.Ville, ligne.Pays])
    requette = "Delete from Lieu where Lieu.NomLieu not in ("
    requette += "Select Etape.NomLieu from Etape, Lieu where Etape.NomLieu = Lieu.NomLieu and  Etape.Ville = Lieu.Ville and Etape.Pays = Lieu.Pays)"
    requette += " and Lieu.Ville not in ("
    requette += "Select Etape.Ville from Etape, Lieu where Etape.NomLieu = Lieu.NomLieu and  Etape.Ville = Lieu.Ville and Etape.Pays = Lieu.Pays)"
    requette += " and Lieu.Pays not in ("
    requette += "Select Etape.Pays from Etape, Lieu where Etape.NomLieu = Lieu.NomLieu and  Etape.Ville = Lieu.Ville and Etape.Pays = Lieu.Pays);"
    base.execute(requette)
    base.close()
    return Lieux_suprime

def ajout_etape(IdCircuit, DateEtape, Duree, NomLieu, Ville, Pays): #testé
    base = connexion.cursor()

    base.execute("insert into Etape(IdCircuit,DateEtape, Duree, NomLieu, Ville, Pays) values(?,?,?,?,?,?);",[IdCircuit, DateEtape, Duree, NomLieu, Ville, Pays])
    base.close()

def suprime_etape(Idcircuit, Ordre): #testé
    base = connexion.cursor()
    base.execute("delete from Etape where Ordre = ? and IdCircuit = ?; Update Etape Set Ordre = Ordre - 1 where Ordre > ? and IdCircuit = ?;", [Idcircuit, Ordre, Idcircuit, Ordre])
    base.close()

def ajout_groupe(Idpassager, Idreservation): #testé
    base = connexion.cursor()
    base.execute("insert into Groupe(IdPersonne, IdReservation, Confirmation) values(?,?,?);",[Idpassager, Idreservation, 0])
    base.close()

def confirmer_groupe(Idpassager, Idreservation): #testé
    base = connexion.cursor()
    base.execute("update Groupe set Confirmation = 1 where IdPersonne = ? and IdReservation = ?;",[Idpassager, Idreservation])
    base.close()

def annuler_groupe(Idpassager, Idreservation, date): #testé - testé
    base = connexion.cursor() # a améliorer : circuit regagne une place et reservation en perd une - fait
    base.execute("update Groupe set Confirmation = 0, DateAnnulation = ? where IdPersonne = ? and IdReservation = ?;",[date, Idpassager, Idreservation])
    #uptade circuit via clé reservation puis clé circuit
    base.execute("select top 1 Circuit.IdCircuit, Circuit.NbPlaceDisponible, Reservation.Place from Reservation inner join Circuit on Reservation.IdCircuit = Circuit.IdCircuit where IdReservation = ?",[Idreservation])
    circuit = base.fetchone()
    base.execute("update Circuit set NbPlaceDisponible = ? where IdCircuit = ?;", [circuit.NbPlaceDisponible + 1 , circuit.IdCircuit]) #ici
    #uptade reservation via clé reservation
    base.execute("update Reservation set Place = ? where IdReservation = ?;", [circuit.Place - 1, Idreservation])
    base.close()

def miseajour_reservation(): #testé
    base = connexion.cursor()
    #trouver reservation ancienne #testé
    base.execute("select DateDepart, Duree, IdReservation from Circuit inner join (select IdCircuit, IdReservation from Reservation where Etat =1) as Reservation_active on Circuit.IdCircuit = Reservation_active.IdCircuit;")

    Aujourdhuis= datetime.date.today()
    liste_reservation_finit = []
    for ligne in base:
        #conversion vers datetime pour addition de datedepart et duree du circuit puis pour comparer avec aujourdhuis
        duree_time= datetime.timedelta(days=ligne.Duree)
        debut = conversion_datestring_dateliste(ligne.DateDepart)
        debut_circuit = datetime.date(debut[0],debut[1],debut[2])
        Fin_circuit = debut_circuit + duree_time
        
        if Fin_circuit < Aujourdhuis:
            liste_reservation_finit.append(ligne.IdReservation)
    
    #trouver reservation annulé en cour #testé
        #aka les reservtions avec 0 places et l'état à 1 (c'est à dire reservation futur/en cour)
    base.execute("select IdReservation from Reservation where Etat = 1 and Place = 0;")

    for ligne in base:
        liste_reservation_finit.append(ligne.IdReservation)

    # les mettre à etat 0
    for i in range(len(liste_reservation_finit) ):
        base.execute("update Reservation set Etat = 0 where IdReservation = ?;", [liste_reservation_finit[i]])
    base.close()

def conversion_datestring_dateliste(datestring): #testé (oui, il y eu des erreurs sur cette mini-fonction)
    #transforme une date sous format chaine de charactère "année-mois-jour" en une liste de 3 élément : année, mois, jour
    return [int(datestring[0:4]), int(datestring[5:7]), int(datestring[8:10])]

def supprime_client(Idclient):#testé 
    base = connexion.cursor()
    #vérification si client encore en reservation
    base.execute("select IdPersonne from Reservation where IdPersonne = ?;",[Idclient])
    ligne = base.fetchone()
    if ligne is None:
        base.execute("delete from Client where IdPersonne = ?;",[Idclient])
        base.close()
        return 1
    else:
        base.close()
        return 0

def supprime_admin(Idadmin): #testé 
    base = connexion.cursor()
    base.execute("delete from Administrateur where IdPersonne = ?;",[Idadmin])
    base.close()

def supprime_lieu(Nom, Ville, Pays): #testé 
    base = connexion.cursor()
    base.execute("select Ordre from Etape where NomLieu =? and Ville = ? and Pays =?;",[Nom, Ville, Pays])
    ligne = base.fetchone()
    if ligne is None:
        base.execute("delete from Lieu where NomLieu =? and Ville = ? and Pays =?;",[Nom, Ville, Pays])
        base.close()
        return 1
    base.close()
    return 0

def supprime_circuit(Idcircuit): #testé 
    #ne supprime pas les reservations par lui même
    base = connexion.cursor()
    base.execute("select Ordre from Etape where IdCircuit = ?;",[Idcircuit])
    ligne = base.fetchone()
    if ligne is None:
        base.execute("select IdReservation, Etat from Reservation where IdCircuit = ?;",[Idcircuit])
        ligne = base.fetchone()
        if ligne is None:
            base.execute("delete from Circuit where IdCircuit = ?;",[Idcircuit])
            base.close()
            return 1
    base.close()
    return 0

def input_test_text(string, taille): #testé
    if len(string) > taille:
        return False
    return True

def input_test_mail(string): #testé
    position = string.find('@')
    if position != -1:
        string = string[position : ]
        if string.find('.') != -1:
            return True
    return False

def input_test_date(string): #testé
    position_a = string.find('-')
    if position_a != -1 :
        annee = string[ : position_a]
        position_m = string.find('-',position_a+1)
        if position_m != -1 :
            mois =  string[position_a+1 : position_m]
            jour = string[position_m +1 : ]
            try :
                annee = int(annee)
                mois = int(mois)
                jour = int(jour)
                datetime.date(annee,mois,jour)
                return True
            except :
                return False
    return False


def test_ajout():

    #print(conversion_datestring_dateliste("2020-11-03"))

    #ajout_reservation(11, 1, 0, "2022-11-05")
    if input_test_date("2021-02-02"):
        print("date valide")
    if input_test_date("2021 02 02"):
        print("date sans -")
    if input_test_date("2021-25-02"):
        print("mois absurde")
    if input_test_date("2021-02-45"):
        print("jour absurde")
    if input_test_date("2021-02-da"):
        print("date avec lettres")
"""
    ajout_circuit('Les minimes','Marseille','Strasbourg','France','France','2022-05-18',59,25,75.3)
    ajout_lieu('Chateau', 'Minima', 'France', 'Ce chateau est la première étape sur le chemin des minimes', 25.1)

    base = connexion.cursor()
    base.execute("select top 1 IdCircuit from Circuit order by IdCircuit Desc")
    ligne = base.fetchone()
    Id = ligne.IdCircuit
    base.close()

    ajout_etape(Id,'2022-05-18', 2, 'Chateau', 'Minima', 'France')

    base = connexion.cursor()

    base.execute("select * from Etape;")    
    for ligne in base:
        for i in range(len(ligne)):
            print(ligne[i], end=' // ')
        print('')

    base.close()
"""

#test_ajout()
#connexion.commit()
#Dernière lignes / fin des connexions
#connexion.close()

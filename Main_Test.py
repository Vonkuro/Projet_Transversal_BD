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

def ajout_client(user, motsdepasse, nom, prenom, datenaissance): #testé
    base = connexion.cursor()
    base.execute("select top 1 IdPersonne from Personne order by IdPersonne Desc")
    ligne = base.fetchone()
    Dernier_Id = ligne.IdPersonne
    Dernier_Id = str(Dernier_Id + 1)
    

    demande = "insert into Personne(IdPersonne, Nom, Prenom, DateNaissance) values (" + Dernier_Id + ", " + nom + ", " + prenom + ", " + datenaissance
    demande = demande + ");"
    base.execute(demande)
    demande = "insert into Client(IdPersonne, Identifiant, MotsdePasse) values (" + Dernier_Id + ", " + user + ", " + motsdepasse + ");"
    base.execute(demande)

    base.close()

def ajout_admin(user, motsdepasse, nom, prenom, datenaissance): #testé
    base = connexion.cursor()
    base.execute("select top 1 IdPersonne from Personne order by IdPersonne Desc")
    ligne = base.fetchone()
    Dernier_Id = ligne.IdPersonne
    Dernier_Id = str(Dernier_Id + 1)
    
    base.execute("insert into Personne(IdPersonne, Nom, Prenom, DateNaissance) values (?, ?, ?, ?);", [Dernier_Id,nom,prenom,datenaissance])
    
    base.execute("insert into Administrateur(IdPersonne, Identifiant, MotsdePasse) values (?, ?, ?);", [Dernier_Id, user, motsdepasse])

    base.close()

def ajout_reservation(Client, Circuit, Places, Date): #testé
    base = connexion.cursor()
    base.execute("select top 1 IdReservation from Reservation order by IdReservation Desc")
    ligne = base.fetchone()
    Dernier_Id = ligne.IdReservation
    Dernier_Id = Dernier_Id + 1 #str peut-être nécessaire
    base.execute("INSERT INTO Reservation (IdReservation , Place , DateRevervation , Etat  , IdCircuit, IdPersonne) VALUES (?, ?, ? , '1', ? , ? ) ; ", [Dernier_Id, Places, Date, Circuit, Client])
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
        base.execute("select top 1 IdPersonne from Personne order by IdPersonne Desc")
        ligne = base.fetchone()
        Dernier_Id = ligne.IdPersonne + 1
        base.execute("insert into Personne(IdPersonne, Nom, Prenom, DateNaissance) values (?, ?, ?, ?);", [Dernier_Id,Nom,Prenom,DateNaissance])
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
    base.execute("Select top 1 IdCircuit from Circuit order by IdCircuit Desc;")
    ligne = base.fetchone()
    Dernier_Id = ligne.IdCircuit + 1
    Liste =[Dernier_Id, Descriptif, Villedepart, Villearrivee, Paysdepart, Paysarrivee, Datedepart, Nbplacedisponible, Duree, Prixinscription]
    base.execute("insert into Circuit(IdCircuit, Descriptif, VilleDepart, VilleArrivee, PaysDepart, PaysArrivee, DateDepart, NbPlaceDisponible, Duree, PrixInscription) values (?,?,?,?,?,?,?,?,?,?);", Liste)
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
    base.execute("select top 1 Ordre from Etape where IdCircuit = ? order by Ordre Desc;", [IdCircuit])
    ligne = base.fetchone()
    if ligne is None:
        Dernier_Id = 1
    else:
        Dernier_Id = ligne.Ordre + 1
    base.execute("insert into Etape(IdCircuit, Ordre, DateEtape, Duree, NomLieu, Ville, Pays) values(?,?,?,?,?,?,?);",[IdCircuit, Dernier_Id, DateEtape, Duree, NomLieu, Ville, Pays])
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


def test_ajout():

    #print(conversion_datestring_dateliste("2020-11-03"))

    #ajout_reservation(11, 1, 0, "2022-11-05")

    print (prix_circuits())
    #base = connexion.cursor()

    """
    for ligne in base:
        for i in range(len(ligne)):
            print(ligne[i], end=' // ')
        print('')
"""
    #base.close()


test_ajout()
#connexion.commit()
#Dernière lignes / fin des connexions
connexion.close()
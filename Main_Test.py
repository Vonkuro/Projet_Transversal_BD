from Connexsion import *


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
    base.execute("INSERT INTO Reservation (IdReservation , Place , DateRevervation , Etat  , IdCircuit, IdPersonne) VALUES (?, ?, ? , '0', ? , ? ) ; ", [Dernier_Id, Places, Date, Circuit, Client])
    base.execute("UPDATE Circuit SET NbPlaceDisponible= NbPlaceDisponible - ? where IdCircuit=? ;",[Places, Circuit])
    base.close()

def identification_passager(Nom, Prenom, DateNaissance): #testé
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


def test_ajout():
    trouve = identification_passager("Muliez","Pierre", "1950-08-28")
    print(trouve)
    trouve = identification_passager("Miliez","Michelle", "28/08/1965")
    base = connexion.cursor()
    print(trouve)
    base.execute("select * from Passager, Personne where Passager.IdPersonne = Personne.IdPersonne;")
    for ligne in base:
        for i in range(len(ligne)):
            print(ligne[i], end=' ')
        print('')
    
    base.close()


test_ajout()
#connexion.commit()
#Dernière lignes / fin des connexions
connexion.close()
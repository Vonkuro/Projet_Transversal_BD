from Connexsion import *


def verification_client(user, motsdepasse):
    base = connexion.cursor()
    base.execute("select * from Client;")
    for ligne in base :
        if ligne.Identifiant == user and ligne.MotsdePasse == motsdepasse :
            base.close()
            return ligne.IdPersonne

    base.close()
    return 0

def verification_admin(user, motsdepasse):
    base = connexion.cursor()
    base.execute("select * from Administrateur;")
    for ligne in base :
        if ligne.Identifiant == user and ligne.MotsdePasse == motsdepasse :
            base.close()
            return ligne.IdPersonne

    base.close()
    return 0

def ajout_client(user, motsdepasse, nom, prenom, datenaissance):
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

def ajout_admin(user, motsdepasse, nom, prenom, datenaissance):
    base = connexion.cursor()
    base.execute("select top 1 IdPersonne from Personne order by IdPersonne Desc")
    ligne = base.fetchone()
    Dernier_Id = ligne.IdPersonne
    Dernier_Id = str(Dernier_Id + 1)
    
    base.execute("insert into Personne(IdPersonne, Nom, Prenom, DateNaissance) values (?, ?, ?, ?);", [Dernier_Id,nom,prenom,datenaissance])
    
    base.execute("insert into Administrateur(IdPersonne, Identifiant, MotsdePasse) values (?, ?, ?);", [Dernier_Id, user, motsdepasse])

    base.close()


def test_ajout():
    ajout_admin("tard","tardy","Muliez","Marine", "2/8/1950")
    base = connexion.cursor()
    base.execute("select * from Administrateur, Personne where Administrateur.IdPersonne = Personne.IdPersonne")
    for ligne in base:
        for i in range(len(ligne)):
            print(ligne[i], end=' ')
        print('')
    
    base.close()

test_ajout()
#connexion.commit()
#Dernière lignes / fin des connexions
connexion.close()
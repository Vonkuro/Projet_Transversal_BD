"# Projet_Transversal_BD" 

soutenance 20 avril
dossier à rendre une semaine avant : le 19 avril

Nombre total de requettes le 13/04/21 : 61

Les 11 Requettes sql dans Pages.py.

"select * from Circuit where IdCircuit = ? and NbPlaceDisponible > 0;"

"select Order, DateEtape, Duree, Descriptif, Etape.NomLieu, Etape.Ville, Etape.Pays from Etape, Lieu on where IdCircuit = ? and Etape.NomLieu = Lieu.NomLieu and Etape.Ville = Lieu.Ville and Etape.Pays = Lieu.Pays;"

"select Nom, Prenom, Mail, DateNaissance, Identifiant, MotsdePasse, Personne.IdPersonne from Personne inner join Administrateur on Personne.IdPersonne = Administrateur.IdPersonne ;"

"select * from Lieu;"

"select * from Etape;"

"select IdCircuit from Circuit;"

"select NomLieu, Ville, Pays from Lieu;"

"select Client.IdPersonne, Nom, Prenom, DateNaissance, Mail from Personne inner join Client on Personne.IdPersonne = Client.IdPersonne;"

"select IdCircuit from Reservation where IdPersonne = ?;"

"select * from Circuit;"

"select Passager.IdPersonne, Nom, Prenom, DateNaissance, Confirmation, Reservation.IdReservation from Personne, Passager, Groupe, Reservation where Personne.IdPersonne = Passager.IdPersonne and Passager.IdPersonne = Groupe.IdPersonne and Reservation.IdReservation = Groupe.IdReservation and Reservation.IdCircuit = ?;"

Les 50 Requettes dans Main_Test.py

"select * from Client;"

"select * from Administrateur;"

"insert into Personne(Nom, Prenom, DateNaissance, Mail) values (? , ? , ? , ?);"

"select top 1 IdPersonne from Personne order by IdPersonne Desc"

"insert into Client(IdPersonne, Identifiant, MotsdePasse) values (? , ? , ?);"

"Update Personne set Nom = ?, Prenom = ?, DateNaissance = ?, Mail = ? where IdPersonne = ?;"

"insert into Personne(Nom, Prenom, DateNaissance, Mail) values (?, ?, ?, ?);"

"select top 1 IdPersonne from Personne order by IdPersonne Desc"

"insert into Administrateur(IdPersonne, Identifiant, MotsdePasse) values (?, ?, ?);"

"Update Personne set Nom = ?, Prenom = ?, DateNaissance = ?, Mail = ? where IdPersonne = ?;"

"Update Administrateur set Identifiant = ?, MotsdePasse = ? where IdPersonne = ?;"

"INSERT INTO Reservation (Place , DateRevervation , Etat  , IdCircuit, IdPersonne) VALUES (?, ? , '1', ? , ? ) ; "

"UPDATE Circuit SET NbPlaceDisponible= NbPlaceDisponible - ? where IdCircuit=? ;"

"Select * from Personne;"

"insert into Personne(Nom, Prenom, DateNaissance) values (?, ?, ?);"

"select top 1 IdPersonne from Personne order by IdPersonne Desc"

"insert into Passager(IdPersonne) values (?);"

"Select * from Passager where IdPersonne = ?;"

"insert into Passager(IdPersonne) values (?);"

"insert into Circuit(Descriptif, VilleDepart, VilleArrivee, PaysDepart, PaysArrivee, DateDepart, NbPlaceDisponible, Duree, PrixInscription) values (?,?,?,?,?,?,?,?,?);"

	requette = "select Circuit.IdCircuit, PrixInscription + sum(Lieu.PrixVisite) as Prix_total"
    requette += " from Circuit, Etape inner join Lieu on (Etape.Pays = Lieu.Pays and Etape.Ville = Lieu.ville and Etape.NomLieu = Lieu.NomLieu)"
    requette += " where Circuit.IdCircuit = Etape.IdCircuit"
    requette += " group by Circuit.IdCircuit, Circuit.PrixInscription;"

"Select NomLieu, Ville, Pays from Lieu;"

"insert into Lieu(NomLieu, Ville, Pays, Descriptif, PrixVisite) values (?,?,?,?,?);"

	requette = "Select Lieu.NomLieu, Lieu.Ville, Lieu.Pays"
    requette += " from Lieu"
    requette += " where Lieu.NomLieu not in ("
    requette += "Select Etape.NomLieu from Etape, Lieu where Etape.NomLieu = Lieu.NomLieu and  Etape.Ville = Lieu.Ville and Etape.Pays = Lieu.Pays)"
    requette += " and Lieu.Ville not in ("
    requette += "Select Etape.Ville from Etape, Lieu where Etape.NomLieu = Lieu.NomLieu and  Etape.Ville = Lieu.Ville and Etape.Pays = Lieu.Pays)"
    requette += " and Lieu.Pays not in ("
    requette += "Select Etape.Pays from Etape, Lieu where Etape.NomLieu = Lieu.NomLieu and  Etape.Ville = Lieu.Ville and Etape.Pays = Lieu.Pays);"

	requette = "Delete from Lieu where Lieu.NomLieu not in ("
    requette += "Select Etape.NomLieu from Etape, Lieu where Etape.NomLieu = Lieu.NomLieu and  Etape.Ville = Lieu.Ville and Etape.Pays = Lieu.Pays)"
    requette += " and Lieu.Ville not in ("
    requette += "Select Etape.Ville from Etape, Lieu where Etape.NomLieu = Lieu.NomLieu and  Etape.Ville = Lieu.Ville and Etape.Pays = Lieu.Pays)"
    requette += " and Lieu.Pays not in ("
    requette += "Select Etape.Pays from Etape, Lieu where Etape.NomLieu = Lieu.NomLieu and  Etape.Ville = Lieu.Ville and Etape.Pays = Lieu.Pays);"

"Update Lieu set Nomlieu = ?, Ville = ?, Pays = ?, Descriptif = ?, Prixvisite = ? where Nomlieu = ? and Ville = ? and Pays = ?;"

"select top 1 Ordre from Etape where IdCircuit = ? order by Ordre DESC;"

"insert into Etape(IdCircuit, Ordre, DateEtape, Duree, NomLieu, Ville, Pays) values(?,?,?,?,?,?,?);"

"delete from Etape where Ordre = ? and IdCircuit = ?; Update Etape Set Ordre = Ordre - 1 where Ordre > ? and IdCircuit = ?;"

"update Etape set DateEtape = ? , Duree = ? where IdCircuit = ? and Ordre = ?;"

"insert into Groupe(IdPersonne, IdReservation, Confirmation) values(?,?,?);"

"update Groupe set Confirmation = 1 where IdPersonne = ? and IdReservation = ?;"

"update Groupe set Confirmation = 0, DateAnnulation = ? where IdPersonne = ? and IdReservation = ?;"

"select top 1 Circuit.IdCircuit, Circuit.NbPlaceDisponible, Reservation.Place from Reservation inner join Circuit on Reservation.IdCircuit = Circuit.IdCircuit where IdReservation = ?"

"update Circuit set NbPlaceDisponible = ? where IdCircuit = ?;"

"update Reservation set Place = ? where IdReservation = ?;"

"select DateDepart, Duree, IdReservation from Circuit inner join (select IdCircuit, IdReservation from Reservation where Etat =1) as Reservation_active on Circuit.IdCircuit = Reservation_active.IdCircuit;"

"select IdReservation from Reservation where Etat = 1 and Place = 0;"

"update Reservation set Etat = 0 where IdReservation = ?;"

"select IdPersonne from Reservation where IdPersonne = ?;"

"delete from Client where IdPersonne = ?;"

"delete from Administrateur where IdPersonne = ?;"

"select Ordre from Etape where NomLieu =? and Ville = ? and Pays =?;"

"delete from Lieu where NomLieu =? and Ville = ? and Pays =?;"

"select Ordre from Etape where IdCircuit = ?;"

"select IdReservation, Etat from Reservation where IdCircuit = ?;"

"delete from Circuit where IdCircuit = ?;"

"update Circuit set Descriptif = ? , VilleDepart = ? , VilleArrivee = ? , PaysDepart = ? , PaysArrivee = ? , DateDepart = ? , NbPlaceDisponible = ? , Duree = ? , PrixInscription = ? where IdCircuit = ?;"

"delete Groupe where IdPersonne = ? and IdReservation = ?;"

    requette ="select PrixInscription + sum(Lieu.PrixVisite) as Prix_total, Circuit.IdCircuit, Circuit.DateDepart, Circuit.Duree"
    requette += " from Circuit, Etape inner join Lieu on (Etape.Pays = Lieu.Pays and Etape.Ville = Lieu.ville and Etape.NomLieu = Lieu.NomLieu)"
    requette +=" where Circuit.IdCircuit = Etape.IdCircuit"
    requette +=" group by Circuit.PrixInscription, Circuit.IdCircuit, Circuit.DateDepart, Circuit.Duree;"


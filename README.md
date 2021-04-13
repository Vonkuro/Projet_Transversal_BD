"# Projet_Transversal_BD" 

soutenance 20 avril
dossier à rendre une semaine avant : le 19 avril

Les 11 Requettes sql dans Pages.py. Il y a 57 requettes dans Main_Test.py.

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
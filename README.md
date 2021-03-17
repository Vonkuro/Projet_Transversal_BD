"# Projet_Transversal_BD" 

rajouter email dans BD

Login :
	verification_client fait
	verification_admin fait

Création de Compte Client:
	ajout_client fait (à modifier  + email)

Choix du Circuit:
	trouve_circuit àfaire
		depend de date et budget
	lire_circuit àfaire
		les circuits touvés
	lire_etapes àfaire
	prix_circuit fait
		renvois le prix des circuits
	lire_etape àfaire
		d'un circuit en particulier

Réservation d'un circuit:
	ajout_reservation fait
	ajout_groupe fait
	identification_passager fait
		ajoute un passager à la BD

Liste des reservations:
	lire_reservation àfaire

Modification d'une réservation:
	update_passager àfaire
	lire_passager àfaire
	confirmer_groupe fait
	annuler_groupe fait
	annuler_reservation àfaire

Gestion du compte client:
	supprime_client fait
	update_client àfaire

Administration :
	Liste des Administrateurs:
		ajout_admin fait (à modifier + email)
		supprime_admin fait
		update_admin àfaire
		lire_admin àfaire
	Lieu
		ajout_lieu fait
		miseajout_lieu fait
			affiche puis supprime les lieux associés à aucune étape
		update_lieu àfaire
		supprime_lieu fait
		lire_lieu àfaire priorité
	Etape
		ajout_etape fait
		suprime_etape fait
		update_etape àfaire
		lire_etape àfaire priorité
	Reservation
		miseajour_reservation fait
		lire_reservation àfaire priorité
	Circuit
		ajout_circuit fait
		update_circuit àfaire
		supprime_circuit fait
		lire_circuit àfaire priorité
	Client
		lire_client àfaire priorité
		supprime_client fait
		update_client àfaire
		ajout_client fait (à modifier  + email)
	Passager
		lire_passager àfaire priorité
		miseajour_passager àfaire
			suppression des passagers non utiliser
	
Pour les fonctions "lire" il faut définir les informations nécéssaire à l'application

Application :
	Login àfaire

	Création de compte client àfaire

	Accueil Client à faire
	Gestion du compte client àfaire
	Choix du Circuit àfaire
	Reservation àfaire
	Liste des reservertion àfaire
	Modification d'une reservation

	Accueil Admin àfaire
	Liste des clients àfaire
	Liste des réservation de circuit par clients àfaire
	Liste des circuits àfaire
	listes des clients et des passagers par circuit àfaire
	Listes des lieux àfaire
	Liste des étapes àfaire
	Liste des administrateurs àfaire


soutenance 20 avril
dossier à rendre une semaine avant : le 15 avril
import pyodbc
#important
connexion = pyodbc.connect('DRIVER={SQL Server};Server=LAPTOP-MN898D93;Database=BDVoyage;User Id=LAPTOP-MN898D93\vonku;Password=')
#Important

requette = connexion.cursor()
requette.execute("insert into Personne (IdPersonne,Nom,Prenom,DateNaissance) values (11, 'Gerard', 'Aya', '01/11/2035');")
#requette.close()
#requette = connexion.cursor()
requette.execute("select * from Personne;")

for row in requette :
    for i in range(len(row)):
        print(row[i])

requette.close()
connexion.close()
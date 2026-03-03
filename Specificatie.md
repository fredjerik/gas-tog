1. invoer(exact wat parser moet herkennen)
   -Initialistatie
   shot: Type, Aantal, Jaar, Maand
   Marshmellow,Honing, Chilipeper: Aantal, Jaar, Maand, Dag
   Gebruiker: Voornaam, Achternaam, Email
   Werknemer: Voornaam, Achternaam, Workload
   start: Duur

   -Script(iets dat op een bebaalde tijdstip T gebeurd)
   1.T bestel EMAIL INGREDIENT1 INGREDIENT2 ... JAAR MAAND DAG UUR MIN
     betekent: bv: 1 bestel john@doe.com melk honing 2024 5 1 11 30 --> Op tijdstip 1 bestelt gebruiker john@doe.com
                                                                      een chocolademelk met melk + honing, besteld op 1 mei 2024 om 11:30
     Wat moet ons systeem kunnen: 1. Check: bestaat gebruiker john@doe.com? --> Nee, dan negeren
                                  2. Check: is er genoeg Stock --> nee, negeren
                                  3. Als OK: 1. maak een Bestelling-object
                                             2. workload = 5 + aantal ingrediënten
                                             3. stock meteen verminderen
                                             4. bestelling in de queue
                                             5. in de log komt deze bestelling in: “bestellingen binnengekomen op tijdstip 1” 
                                             Belangrijk: De bestelling wordt niet automatisch verwerkt → pas op het einde van het tijdstip kunnen werknemers die opnemen.
   2.T stock TYPE ... AANTAL JAAR MAAND DAG
     betekent: bv. 3 stock shot melk 4 2030 5 1 --> Op tijdstip 3 worden 4 melk-chocoladeshots
                                                    met vervaldatum 1 mei 2030 toegevoegd aan de stock.
     Wat moet ons systeem kunne: 1. Maak 4 nieuwe ingredient-objecten
                                 2. Stop ze in de juiste stock-tabel
                                 3. Dit gebeurt tijdens het tijdstip, vóór de verwerking aan het einde
     MINI VOORBEELD:
     # initialisatie
    shot melk 10 2030 5 1
    gebruiker John Doe john@doe.com
    werknemer Jane Doe 5
    
    # script
    start 4
    1 bestel john@doe.com melk honing 2024 5 1 11 30
    3 stock shot melk 4 2030 5 1

    VERLOOP:
    Tijdstip 0:
    alleen initialisatie

    Tijdstip 1:
    bestelling komt binnen
    stock vermindert
    bestelling in queue
    einde tijdstip → werknemer kan bestelling opnemen
   
    Tijdstip 2: geen instructies

    Tijdstip 3: stock wordt aangevuld
    
    Tijdstip 4: niets
                                 

   
3. tijdverloop
4. Log
5. Tabbelen en sleutels

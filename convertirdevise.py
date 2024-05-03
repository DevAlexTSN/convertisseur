# Creer une application pour convertir un montant en devise dans une autre devise. 
# Le montant est a saisir, la devise de départ est a saisir, ainsi que la devise d'arrivée

import requests

# demande de la devise initiale
deviseInitiale= input("Ecrivez le code de la devise initiale   ") 
# demande d'une valeur à convertir
montant= float(input('Saisissez un montant à convertir   ')) 
 # demande de la devise finale
deviseFinale=input("Ecrivez le code de la devise finale   ")

montant_format="{:,.2f}".format(float(montant)).replace(","," ")

#creation d'une variable URL pour renvoyer vers l'API de la valeur finale
url="https://open.er-api.com/v6/latest/" + deviseInitiale
 # requete vers l'API 
response = requests.get(url)

if response.status_code ==200: 
    #convertir la réponse en format JSON
    data= response.json() 
    #Extrait la valeur de la conversion entre Devise Initiale et Devise Finale
    valeurDeviseFinale=float(data['rates'][deviseFinale]) 
    
    convertir="{:,.2f}".format(float(montant * valeurDeviseFinale)).replace(","," ")
    # print du résultat
    print("La valeur de " + str(montant_format) +" "+ (deviseInitiale) +" en "+ (deviseFinale) + " est de "+ str(convertir)+ ' ' + (deviseFinale)) 
else : 
    print("La requete à échouer avec le code :", response.status_code)
    

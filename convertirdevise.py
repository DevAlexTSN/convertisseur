# Creer une application pour convertir un montant en devise dans une autre devise. 
# Le montant est a saisir, la devise de départ est a saisir, ainsi que la devise d'arrivée
import requests

deviseInitiale= input("Ecrivez le code de la devise initiale   ") # demande de la devise initiale
montant= float(input('Saisissez un montant à convertir   ')) # demande d'une valeur à convertir
deviseFinale=input("Ecrivez le code de la devise finale   ") # demande de la devise finale

#creation d'une variable URL pour renvoyer vers l'API de la valeur finale
url="https://open.er-api.com/v6/latest/" + deviseInitiale
print(url)

response = requests.get(url) # requete vers l'API 

if response.status_code ==200: 
    data= response.json() #convertir la réponse en format JSON
    # print(data) #afficher les données JSON
    valeurDeviseFinale=float(data['rates'][deviseFinale]) #Extrait la valeur de la conversion entre Devise Initiale et Devise Finale
    # print(valeurDeviseFinale)
    convertir = round(float(montant * valeurDeviseFinale),2) #convertis la valeur , 2 décimales
    print("La valeur de " + str(montant) +" "+ (deviseInitiale) +" en "+ (deviseFinale) + " est de "+ str(convertir)+ ' ' + (deviseFinale)) # print du résultat
else : 
    print("La requete à échouer avec le code :", response.status_code)
    

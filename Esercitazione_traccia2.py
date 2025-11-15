import json


def carica_logs(input_file):
    try:
        with open(input_file, "r") as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        print("percorso del file di log JSON non trovato")
    except json.decoder.JSONDecodeError:
        print("formato file json non valido")






def salva_logs(dati, output_file):
    try:
        with open(output_file, "w") as json_file:
            json.dump(dati, json_file, indent=4)
    except Exception as e:
        print(f"file non salvato correttamente {e}")


def estrai_dati(logs):


    #creo il dizionario per utente
    dict_utente ={}
    #gli indici che identificano i dati da estrarre
    indice_utenti=1
    indice_evento = 4
  #mi salvo l'evento e l'utente
    for log in logs:
        utente = log[indice_utenti]
        evento = log[indice_evento]

        if utente not in dict_utente:
            dict_utente[utente] = {
                "eventi": set(),
                "conteggio_eventi": {}
            }

        # aggiunge evento agli eventi
        dict_utente[utente]["eventi"].add(evento)

        # aggiorna conteggio eventi
        if evento not in dict_utente[utente]["conteggio_eventi"]:
            dict_utente[utente]["conteggio_eventi"][evento] = 0
        dict_utente[utente]["conteggio_eventi"][evento] += 1

        # converte i set in lista ordinata per JSON
    for u in dict_utente:
        dict_utente[u]["eventi"] = sorted(list(dict_utente[u]["eventi"]))

    return dict_utente


def main():
   #chiedo il percorso del file in input e per l'output
    input_file = input("Inserisci il percorso del file di log JSON : ")
    output_file = input("Inserisci il percorso del file di output JSON : ")

   # scaletta delle funzioni da eseguire per caricare e salvare il file json
    logs = carica_logs(input_file)
    dati = estrai_dati(logs)

    salva_logs(dati,output_file)

if __name__ == "__main__":
    main()
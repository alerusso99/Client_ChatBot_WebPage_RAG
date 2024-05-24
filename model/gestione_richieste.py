import requests


# Questa funzione si occupa di inviare effettivamente la richiesta al server e ricevere la risposta.
def gestione_richieste(url, payload, headers, method):
    print("\nRICHIESTA INVIATA DAL CLIENT:\n", payload)
    print("\n-----------------------------\n")
    try:
        # Iniziamo scegliendo il tipo di richiesta che vogliamo effettuare, tra GET e POST.
        if method == "GET":
            response = requests.get(url, headers=headers, data=payload)
        elif method == "POST":
            response = requests.post(url, headers=headers, data=payload)
        else:
            raise ValueError("Metodo non supportato: usa 'GET' o 'POST'.")
        # Solleva un'eccezione se la richiesta non è andata a buon fine
        response.raise_for_status()
        # Supponendo che la risposta sia in formato JSON
        risposta_json = response.json()
        # Ricaviamo effettivamente la risposta.
        risposta = risposta_json.get('Risposta')
        # Se la risposta è vuota
        if risposta is None:
            raise KeyError("La chiave 'Risposta' non è presente nella risposta JSON.")
    except requests.exceptions.Timeout as e:
        print("Timeout durante la richiesta:", e)
        risposta = "Timeout"
    except requests.exceptions.ConnectionError as e:
        print("Errore di connessione durante la richiesta:", e)
        risposta = "Errore di connessione"
    except requests.exceptions.RequestException as e:
        print("Si è verificato un errore durante la richiesta:", e)
        risposta = "Errore di richiesta"
    except ValueError as e:
        print("Errore nel parsing della risposta JSON:", e)
        risposta = "Errore di parsing JSON"
    except KeyError as e:
        print("La chiave Risposta non è presente nel messaggio JSON", e)
        risposta = "Errore chiave nella risposta del server"
    return risposta
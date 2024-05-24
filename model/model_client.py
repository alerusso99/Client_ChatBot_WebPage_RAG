import json
import model.gestione_richieste


# Funzione che si occupa di recuperare le tipologie di borse, effettuando una richiesta al server.
def recupera_tipologia_borsa():
    url = "http://52.9.244.32:8000/controller/recupero_tipologia_borse"
    payload = {}
    headers = {}
    tipologia_borsa = model.gestione_richieste.gestione_richieste(url, payload, headers, "GET")
    return tipologia_borsa


# Funzione che si occupa di recuperare il materiale delle borse, effettuando una richiesta al server.
def recupera_materiale_borsa(chat_history):
    url = "http://52.9.244.32:8000/controller/recupero_materiale_borsa"
    # Convertiamo la chat_history in una stringa, dato che è in un formato HumanMessage e AIMessage
    chat_history_text = "\n".join([str(message) for message in chat_history])
    # Comunichiamo che vogliamo inviare semplicemente del testo.
    headers = {
        'Content-Type': 'text/plain'
    }
    materiale_borsa = model.gestione_richieste.gestione_richieste(url, chat_history_text, headers, "POST")
    return materiale_borsa


# Funzione che si occupa di recuperare il colore delle borse, effettuando una richiesta al server
def recupera_colore_borsa(chat_history):
    url = "http://52.9.244.32:8000/controller/recupero_colore_borsa"
    # Convertiamo la chat_history in una stringa, dato che è in un formato HumanMessage e AIMessage
    chat_history_text = "\n".join([str(message) for message in chat_history])
    # Comunichiamo che vogliamo inviare semplicemente del testo.
    headers = {
        'Content-Type': 'text/plain'
    }
    colore_borsa = model.gestione_richieste.gestione_richieste(url, chat_history_text, headers, "POST")
    return colore_borsa


# Funzione che si occupa di recuperare il prezzo delle borse, effettuando una richiesta al server
def recupera_prezzo_borsa(chat_history):
    url = "http://52.9.244.32:8000/controller/recupero_prezzo_borsa"
    # Convertiamo la chat_history in una stringa, dato che è in un formato HumanMessage e AIMessage
    chat_history_text = "\n".join([str(message) for message in chat_history])
    # Comunichiamo che vogliamo inviare semplicemente del testo.
    headers = {
        'Content-Type': 'text/plain'
    }
    prezzo_borsa = model.gestione_richieste.gestione_richieste(url, chat_history_text, headers, "POST")
    return prezzo_borsa


# Funzione che si occupa di recuperare la descrizione delle borse, effettuando una richiesta al server
def recupera_descrizione_borsa(chat_history):
    url = "http://52.9.244.32:8000/controller/recupero_descrizione_borsa"
    # Convertiamo la chat_history in una stringa, dato che è in un formato HumanMessage e AIMessage
    chat_history_text = "\n".join([str(message) for message in chat_history])
    # Comunichiamo che vogliamo inviare semplicemente del testo.
    headers = {
        'Content-Type': 'text/plain'
    }
    descrizione_borsa = model.gestione_richieste.gestione_richieste(url, chat_history_text, headers, "POST")
    return descrizione_borsa


# Funzione che si occupa di recuperare il prodotto finale, effettuando una richiesta al server
def recupero_finale(chat_history):
    url = "http://52.9.244.32:8000/controller/recupero_finale"
    # Convertiamo la chat_history in una stringa, dato che è in un formato HumanMessage e AIMessage
    chat_history_text = "\n".join([str(message) for message in chat_history])
    # Comunichiamo che vogliamo inviare semplicemente del testo.
    headers = {
        'Content-Type': 'text/plain'
    }
    risposta_finale = model.gestione_richieste.gestione_richieste(url, chat_history_text, headers, "POST")
    return risposta_finale


# Funzione che si occupa di effettuare richieste generiche all'LLM, effettuando una richiesta al server
def domanda_generale(chat_history, user_query):
    url = "http://52.9.244.32:8000/controller/domanda_generale"
    # Convertiamo la chat_history in una stringa, dato che è in un formato HumanMessage e AIMessage
    chat_history_text = "\n".join([str(message) for message in chat_history])
    # Formiamo la struttura del messaggio JSON con due chiavi, chat_history e user_query.
    payload = json.dumps({
        "chat_history": chat_history_text,
        "user_query": user_query
    })
    # Comunichiamo che vogliamo inviare un messaggio in formato JSON.
    headers = {
        'Content-Type': 'application/json'
    }
    risposta_generale = model.gestione_richieste.gestione_richieste(url, payload, headers, "POST")
    return risposta_generale


# Questa funzione invia al server una lista di prodotti. Il server restituirà la lista degli url delle immagini dei
# prodotti passati come argomento.
def recupera_url_immagini(lista_url_produtct):
    url = "http://52.9.244.32:8000/controller/recupera_url_immagini"
    # Converti lista_url_product in formato JSON
    payload = json.dumps({
        "lista": lista_url_produtct
    })
    # Comunichiamo che vogliamo inviare un messaggio in formato JSON.
    headers = {
        'Content-Type': 'application/json'
    }
    lista_url_immagini = model.gestione_richieste.gestione_richieste(url, payload, headers, "POST")
    return lista_url_immagini
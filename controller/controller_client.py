import model.model_client
import re


# Funzione che ci ritorna la domanda: Scegliere la tipologia di borsa.
def recupera_tipologia_borsa():
    tipologia_borsa = model.model_client.recupera_tipologia_borsa()
    return tipologia_borsa


# Funzione che ci ritorna la domanda: Scegliere il materiale della borsa.
def recupera_materiale_borsa(chat_history):
    materiale_borsa = model.model_client.recupera_materiale_borsa(chat_history)
    return materiale_borsa


# Funzione che ci ritorna la domanda: Scegliere il colore della borsa.
def recupera_colore_borsa(chat_history):
    colore_borsa = model.model_client.recupera_colore_borsa(chat_history)
    return colore_borsa


# Funzione che ci ritorna la domanda: Scegliere il prezzo della borsa.
def recupera_prezzo_borsa(chat_history):
    prezzo_borsa = model.model_client.recupera_prezzo_borsa(chat_history)
    return prezzo_borsa


# Funzione che ci ritorna la domanda: Inserire una descrizione della borsa.
def recupera_descrizione_borsa(chat_history):
    descrizione_borsa = model.model_client.recupera_descrizione_borsa(chat_history)
    return descrizione_borsa


# Funzione che ci ritorna i risultati, dopo la query al db vettoriale.
def recupero_finale(chat_history):
    risposta_finale = model.model_client.recupero_finale(chat_history)
    return risposta_finale


# Funzione che si occupa di inviare query generiche all'LLM, riguardante le borse.
def domanda_generale(chat_history, user_query):
    risposta_generale = model.model_client.domanda_generale(chat_history, user_query)
    return risposta_generale


# Funzione che si occupa di inviare la lista degli URL dei prodotti ricevuti in risposta dal server. La funzione
# restituirà la lista degli URL delle immagini.
def recupera_url_immagine(lista_url_product):
    lista_url_immagini = model.model_client.recupera_url_immagini(lista_url_product)
    return lista_url_immagini


# Questa funzione prende in input una stringa, cioè la risposta finale che LLM da al client, ed estrapola gli URL dei
# prodotti.
def recupera_url_prodotto(prodotti_selezionati):
    # Utilizziamo le espressioni regolari per trovare tutti gli URL
    exp_pattern = r'(https?://\S+)'
    url_prodotti = re.findall(exp_pattern, prodotti_selezionati)
    return url_prodotti


# Funzione che crende in input una stringa contenente gli URL delle immagini restituita dal server, fomrattata con
# parentesi e apici, e si occupa di estrapolare solo gli URL delle immagini.
def estrai_url_immagini(prodotti_selezionati):
    # Utilizziamo le espressioni regolari per trovare tutti gli URL delle immagini.
    exp_pattern = r"'(https?://[^\s,()']+)'"
    url_immagini = re.findall(exp_pattern, prodotti_selezionati)
    return url_immagini


# Funzione che prende in input una stringa, cioè la risposta finale che LLM da al client, ed estrapola i nomi dei
# prodotti restituiti.
def recupera_nomi_prodotti(prodotti_selezionati):
    # Utilizziamo le espressioni regolari per trovare tutti i nomi contenuti tra **
    exp_pattern = r"\*\*(.*?)\*\*"
    lista_nomi = re.findall(exp_pattern, prodotti_selezionati)
    return lista_nomi


# Questa funzione prende in input una stringa, cioè la risposta finale che LLM da al client, e spezzetta la stringa
# dividendo i singoli prodotti e mettendoli in una lista.
def dividi_prodotti(text):
    # Utilizziamo le espressioni regolari per separare ogni prodotto, ogni qualvolta incontriamo \n**
    exp_pattern = r"\n\*\*"
    lista_prodotti = re.split(exp_pattern, text)
    # Lista finale che contiene i prodotti formattati
    prodotti_finali = []
    # Se la stringa non inizia con il nome del prodotto:
    if lista_prodotti[0][0] != "*":
        # Uniamo l'intestazione con il primo prodotto.
        prodotti_finali.append(lista_prodotti[0]+"\n**"+lista_prodotti[1])
        # Per ogni prodotto della lista, dal terzo in poi, aggiungiamo ** all'inizio.
        for prodotto in lista_prodotti[2:]:
            prodotto = "**"+prodotto
            prodotti_finali.append(prodotto)
    else:
        prodotti_finali.append(lista_prodotti[0])
        # Per ogni prodotto della lista, dal secondi in poi, aggiungiamo ** all'inizio.
        for prodotto in lista_prodotti[1:]:
            prodotto = "**" + prodotto
            prodotti_finali.append(prodotto)
    return prodotti_finali
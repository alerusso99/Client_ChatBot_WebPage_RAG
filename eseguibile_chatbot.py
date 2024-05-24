import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
import controller.controller_client
import time


# Questa funzione si occupa di resettare le variabili di sessione per ricominciare una nuova discussione.
def reset():
    st.session_state.chat_history_chronology = []
    st.session_state.name_product = []
    st.session_state.chat_history_sequcence = ["risposta_finale", "descrizione_borsa", "prezzo_borsa", "colore_borsa",
                                               "materiale_borsa", "tipologia_borsa"]

# Settiamo il titolo della pagina(pannello browser) e settiamo un icona visibile nel pannello.
st.set_page_config(page_title="BagGenius", page_icon=":robot_face:")

# Impostiamo un titolo all'interno della pagina. Il titolo sarà in blue e avrà un'icona di fianco.
st.title(":blue[BagGenius] :shopping_bags:")

# Settiamo un messaggio di intestazione sotto il titolo.
intestazione = """<b>Lascia che l'intelligenza artificiale trovi la borsa giusta per te.</b>"""
st.write(intestazione, unsafe_allow_html=True)

# Settiamo la scritta all'interno della barra di inserimento, dove l'utente scriverà la query.
user_query = st.chat_input("Digita Qui...")

# Crea la sidebar
with st.sidebar:
    # Settiamo il logo di BagGenius
    st.image("logo_bag_genius.png", use_column_width=True)

    # Inseriamo un divisore dopo il logo
    st.divider()

    # Aggiungiamo un bottone nella sidebar dopo il divisore. Il bottone ci permetterà di resettare la chat e
    # ricominciarne una nuova.
    button_clicked = st.sidebar.button(":right_anger_bubble: Nuova Chat", help="Cliccando inizierai una nuova chat.", type="primary", use_container_width=True)
    if button_clicked:
        reset()

    # Inseriamo un divisore dopo il logo
    st.divider()

    # Aggiungiamo dopo il divisore una descrizione dell'applicativo.
    st.sidebar.header("Cos'è BagGenius")
    contenuto = """
    BagGenius è il tuo assistente personale per la scelta della borsa perfetta! Dimentica lo stress di navigare tra mille opzioni, il nostro chatbot intelligente ti guiderà nella scelta ideale in base alle tue preferenze.

    <b>Come funziona?</b>
    <ul>
        <li><b>Rispondi alle domande:</b> Inizia rispondendo ad alcune semplici domande del chatbot. Più precise e sincere saranno le tue risposte, più accurati saranno i risultati.</li>
        <li><b>Scopri le borse ideali:</b> BagGenius analizzerà le tue preferenze e ti presenterà una selezione di borse che corrispondono al tuo stile e alle tue esigenze.</li>
        <li><b>Approfondisci la tua ricerca:</b> Una volta visualizzate le opzioni, potrai porre al chatbot domande specifiche sui prodotti, i materiali, il rapporto qualità-prezzo e qualsiasi altra curiosità. BagGenius semplifica la tua ricerca della borsa perfetta! Inizia subito a chattare e scopri la tua prossima borsa preferita.</li>
    </ul>
    """
    st.sidebar.write(contenuto, unsafe_allow_html=True)

# Definiamo la variabile di sessione name_produtct, che conterrà i nomi dei prodotti dati in output dal server.
if "name_product" not in st.session_state:
    st.session_state.name_product = []

# Definiamo la variabile di sessione copy_name_product, è una rindondanza della variabile definita sopra.
if "copy_name_produtct" not in st.session_state:
    st.session_state.copy_name_produtct = []


# Definiamo la variabile di sessione chat_history_chronology, che conterrà la cronologia della chat.
if "chat_history_chronology" not in st.session_state:
    st.session_state.chat_history_chronology = []

# Definiamo la variabile di sessione chat_history_sequence, che conterrà la sequenza di azioni che il client dovrà
# rispettare per far funzionare correttamente il programma.
if "chat_history_sequcence" not in st.session_state:
    st.session_state.chat_history_sequcence = ["risposta_finale", "descrizione_borsa", "prezzo_borsa", "colore_borsa", "materiale_borsa", "tipologia_borsa"]

# Se il numero di passi della sequenza è diversa da 0, entra nell'if.
if st.session_state.chat_history_sequcence.__len__() != 0:
    # Prendiamo l'ultimo elemento aggiunto nella sequenza e rimuoviamolo.
    sequence = st.session_state.chat_history_sequcence.pop()

    # Se la sequenza è "tipologia_borsa" richiamiamo la funzione recupera_tipologia_borsa() nel controller client,
    # e aggiungiamo la risposta alla chat_history.
    if sequence == "tipologia_borsa":
        tipologia_borsa = controller.controller_client.recupera_tipologia_borsa()
        st.session_state.chat_history_chronology.append(AIMessage(tipologia_borsa))

    # Se la sequenza è "materiale_borsa" richiamiamo la funzione recupera_materiale_borsa() nel controller client,
    # e aggiungiamo la risposta alla chat_history.
    if sequence == "materiale_borsa":
        # Aggiungiamo alla chat_history, la risposta dell'utente.
        st.session_state.chat_history_chronology.append(HumanMessage(user_query))
        materiale_borsa = controller.controller_client.recupera_materiale_borsa(st.session_state.chat_history_chronology)
        st.session_state.chat_history_chronology.append(AIMessage(materiale_borsa))

    # Se la sequenza è "colore_borsa" richiamiamo la funzione recupera_colore_borsa() nel controller client,
    # e aggiungiamo la risposta alla chat_history.
    if sequence == "colore_borsa":
        # Aggiungiamo alla chat_history, la risposta dell'utente.
        st.session_state.chat_history_chronology.append(HumanMessage(user_query))
        colore_borsa = controller.controller_client.recupera_colore_borsa(st.session_state.chat_history_chronology)
        st.session_state.chat_history_chronology.append(AIMessage(colore_borsa))

    # Se la sequenza è "prezzo_borsa" richiamiamo la funzione recupera_prezzo_borsa() nel controller client,
    # e aggiungiamo la risposta alla chat_history.
    if sequence == "prezzo_borsa":
        # Aggiungiamo alla chat_history, la risposta dell'utente.
        st.session_state.chat_history_chronology.append(HumanMessage(user_query))
        prezzo_borsa = controller.controller_client.recupera_prezzo_borsa(st.session_state.chat_history_chronology)
        st.session_state.chat_history_chronology.append(AIMessage(prezzo_borsa))

    # Se la sequenza è "descrizione_borsa" richiamiamo la funzione recupera_descrizione_borsa() nel controller
    # client, e aggiungiamo la risposta alla chat_history.
    if sequence == "descrizione_borsa":
        # Aggiungiamo alla chat_history, la risposta dell'utente.
        st.session_state.chat_history_chronology.append(HumanMessage(user_query))
        descrizione_borsa = controller.controller_client.recupera_descrizione_borsa(st.session_state.chat_history_chronology)
        st.session_state.chat_history_chronology.append(AIMessage(descrizione_borsa))

    # Se la sequenza è "risposta_finale" richiamiamo la funzione recupero_finale() nel controller client,
    # e aggiungiamo la risposta alla chat_history.
    if sequence == "risposta_finale":
        # Aggiungiamo alla chat_history, la risposta dell'utente.
        st.session_state.chat_history_chronology.append(HumanMessage(user_query))
        risposta_finale = controller.controller_client.recupero_finale(st.session_state.chat_history_chronology)
        # Separiamo la stringa contenente i prodotti in una lista.
        prodotti_separati = controller.controller_client.dividi_prodotti(risposta_finale)
        # Estrapoliamo gli URL dei prodotti presenti nella stringa.
        lista_url = controller.controller_client.recupera_url_prodotto(risposta_finale)
        # Ricaviamo gli url delle immagini dei prodotti, effettuando una richiesta al server e passandogli una lista
        # contenente gli URL dei prodotti che abbiamo precedentemente ricavato.
        strigna_url_immagini = controller.controller_client.recupera_url_immagine(lista_url)
        # Estrapoliamo gli URL delle immagini dalla stringa precedentemente ricavata e li aggiungiamo ad una lista.
        lista_url_immagini = controller.controller_client.estrai_url_immagini(strigna_url_immagini)
        # Estrapoliamo i nomi dei prodotti dalla stringa risposta_finale. Li aggiungiamo ad una lista, e facciamo il
        # reverse della lista.
        lista_nomi = controller.controller_client.recupera_nomi_prodotti(risposta_finale)
        for nome in lista_nomi:
            st.session_state.name_product.append(nome)
        st.session_state.name_product.reverse()
        if len(prodotti_separati) == len(lista_url_immagini) and len(lista_url_immagini) != 0:
            # Per ogni prodotto ottenuto, aggiungiamo i dettagli del prodotto e gli url delle loro immagini alla
            # chat_history.
            for i in range(len(prodotti_separati)):
                st.session_state.chat_history_chronology.append(AIMessage(prodotti_separati[i]))
                st.session_state.chat_history_chronology.append(lista_url_immagini[i])
            # Aggiungiamo un'ulteriore messaggio da presentare al cliente.
            st.session_state.chat_history_chronology.append(AIMessage("Hai qualche domanda sui prodotti presentati?"))
        else:
            st.session_state.chat_history_chronology.append(AIMessage("Errore, cliccare il bottone Nuova Chat"))
# Entriamo in questo else quando entriamo nella fase delle domande libere da parte dell'utente.
else:
    # Aggiungiamo la query dell'utente alla chat_history.
    st.session_state.chat_history_chronology.append(HumanMessage(user_query))
    response = controller.controller_client.domanda_generale(st.session_state.chat_history_chronology, user_query)
    st.session_state.chat_history_chronology.append(AIMessage(response))

# Quando otteniamo i nomi dei prodotti che il server ci restituirà, copieremo la lista completa in una lista di
# supporto, che utilizzeremo per mantenere i nomi sotto le immagini, anche se continuiamo a scrivere nella chat.
for name in st.session_state.name_product:
    st.session_state.copy_name_produtct.append(name)

# Stabiliamo la struttura della chat, definendo nomi e icone.
for message in st.session_state.chat_history_chronology:
    if isinstance(message, HumanMessage):
        with st.chat_message("Human", avatar="icon_user.png"):
            st.markdown(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("AI", avatar="icon_bot.png"):
            st.markdown(message.content)
    # Entreremo in questo else quando il messaggio non sarà ne da parte dell'Human ne da parte dell'AI, ma sarà un
    # URL di un'immagine che vorremo mostrare all'interno di una chat.
    else:
        with st.chat_message("AI", avatar="icon_bot.png"):
            st.image(message, caption=f"{st.session_state.copy_name_produtct.pop()}", width=300)

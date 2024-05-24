# Client_ChatBot_WebPage_RAG

## Descrizione
Questo progetto implementa un chatbot innovativo progettato per assistere gli utenti nella selezione di borse che soddisfano le loro preferenze individuali. Il chatbot utilizza un'interfaccia conversazionale per comprendere le esigenze e i gusti dell'utente, impiegando l'intelligenza artificiale di Gemini per fornire suggerimenti personalizzati.

## Funzionalità principali
- **Interfaccia di chat intuitiva**: L'utente interagisce con il chatbot tramite un'interfaccia di chat facile da usare, esprimendo le proprie preferenze in linguaggio naturale.
- **Comprensione del linguaggio naturale**: Il chatbot sfrutta algoritmi avanzati di elaborazione del linguaggio naturale per interpretare le richieste dell'utente e identificare le caratteristiche desiderate nelle borse.
- **Intelligenza artificiale di Gemini**: L'IA di Gemini analizza le preferenze dell'utente e le confronta con un vasto database vettoriale, fornendo suggerimenti mirati che si allineano alle esigenze individuali.
- **Suggerimenti personalizzati**: Il chatbot presenta all'utente una selezione di borse che corrispondono alle sue preferenze.

## Architettura Client
Il progetto adotta il pattern WEB Model-View-Controller (MVC) per garantire una struttura modulare e manutenibile:
- **Model**: Gestisce la comunicazione con il server.
- **View**: Presenta l'interfaccia di chat all'utente.
- **Controller**: Gestisce l'interazione tra la view e il model, elaborando le richieste dell'utente e aggiornando la view di conseguenza.

## Tecnologie utilizzate
- Python
- Interfaccia Grafica: Streamlit
- Framework: Langchain
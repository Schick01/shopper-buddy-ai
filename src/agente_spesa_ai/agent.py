# src/agente_spesa_ai/agent.py

import json
from langchain_ollama import OllamaLLM
from agente_spesa_ai import functions

# Mappa i nomi delle funzioni alle vere funzioni Python
FUNCTION_MAP = {
    "add_item": functions.add_item,
    "remove_item": functions.remove_item,
    "view_list": functions.view_list,
    "clear_list": functions.clear_list
}

llm = OllamaLLM(model="mistral")  # assicurati di aver fatto: `ollama run mistral`

PROMPT_TEMPLATE = """
Capisci l'intento dell'utente e restituisci SOLO il nome della funzione da chiamare 
e i suoi argomenti in formato JSON. Le funzioni disponibili sono:

- add_item(item: str, quantity: int=1) — Aggiunge un elemento alla lista della spesa.
  Sinonimi: comprare, aggiungere, inserire, mettere, acquistare

- remove_item(item: str, quantity: int=1) — Rimuove una o più quantità di un articolo.
  Sinonimi: togliere, rimuovere, cancellare, eliminare

- view_list() — Mostra la lista della spesa.

- clear_list() — Svuota tutta la lista.

Esempi:
Utente: Aggiungi latte
Risposta: {{"function": "add_item", "arguments": {{"item": "latte"}}}}

Utente: Voglio comprare 2 mele
Risposta: {{"function": "add_item", "arguments": {{"item": "mele", "quantity": 2}}}}

Utente: Cancella la lista
Risposta: {{"function": "clear_list", "arguments": {{}}}}

Utente: {input}
Risposta:
"""

def ask_agent(user_message: str) -> str:
    """
    Processa il messaggio dell'utente e chiama la funzione appropriata.

    Args:
        user_message (str): Il messaggio dell'utente.
    """
    prompt = PROMPT_TEMPLATE.format(input=user_message)  # Inserisce il messaggio dell'utente nel prompt
    raw_response = llm.invoke(prompt)  # Ottiene la risposta grezza dal modello

    try:
        response_json = json.loads(raw_response.strip()) 
        fn_name = response_json["function"]  # Estrae il nome della funzione
        args = response_json.get("arguments", {}) 
        if fn_name in FUNCTION_MAP:
            return FUNCTION_MAP[fn_name](**args)
        else:
            return f"⚠️ Funzione '{fn_name}' non riconosciuta."
    except Exception as e:
        return f"⚠️ Errore nell'interpretazione della risposta: {e}\nTesto grezzo:\n{raw_response}"

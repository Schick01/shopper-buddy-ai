# src/agente_spesa_ai/functions.py

shopping_list = {}

def add_item(item: str, quantity: int = 1) -> str:
    if not item:
        return "⚠️ Devi specificare un elemento da aggiungere."
    if quantity < 1:
        return "⚠️ La quantità deve essere almeno 1."
    if item in shopping_list:
        shopping_list[item] += quantity
        return f"✅ Quantità aggiornata: ora ci sono {shopping_list[item]} '{item}' nella lista."
    else:
        shopping_list[item] = quantity
        return f"✅ '{item}' è stato aggiunto alla lista con quantità {quantity}."

def remove_item(item: str, quantity: int = 1) -> str:
    if item not in shopping_list:
        return f"⚠️ '{item}' non è presente nella lista."
    if quantity < 1:
        return "⚠️ La quantità deve essere almeno 1."
    if shopping_list[item] <= quantity:
        del shopping_list[item]
        return f"🗑️ Tutte le quantità di '{item}' sono state rimosse dalla lista."
    else:
        shopping_list[item] -= quantity
        return f"🗑️ Rimosse {quantity} unità di '{item}'. Ora ne restano {shopping_list[item]}."

def view_list() -> str:
    if not shopping_list:
        return "🛒 La lista è vuota."
    result = "📝 Lista della spesa:\n"
    for item, quantity in shopping_list.items():
        result += f"- {item}: {quantity}\n"
    return result.strip()

def clear_list() -> str:
    if not shopping_list:
        return "🛒 La lista è già vuota."
    shopping_list.clear()
    return "🗑️ La lista è stata svuotata."

# src/agente_spesa_ai/main.py

from agente_spesa_ai.agent import ask_agent

print("🛒 Ciao sono Shopper Buddy, il tuo assistente lista della spesa, come posso aiutarti?")
print("Scrivi 'esci' per terminare.")

while True:
    user_input = input("🧑 Tu: ")
    if user_input.lower() in {"esci", "exit", "quit"}:
        print("👋 Arrivederci!")
        break

    response = ask_agent(user_input)
    print("🤖 Assistente:", response)
    print("Per uscire dalla chat, digita 'esci'.")
    print()


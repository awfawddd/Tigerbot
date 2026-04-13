import random
from datetime import datetime
import os
import json

cartella_utenti = "utenti"
utente_corrente = ""

if not os.path.exists(cartella_utenti):
    os.mkdir(cartella_utenti)


def salva(ruolo, testo):
    ora = datetime.now().strftime("%d/%m/%Y %H:%M")
    with open("cronologia.txt", "a", encoding="utf-8") as f:
        f.write(f"[{ora}] {ruolo}: {testo}\n")


def salva_nome(nome):
    with open("nome.txt", "w", encoding="utf-8") as f:
        f.write(nome)


def salva_eta(eta):
    with open("eta.txt", "w", encoding="utf-8") as f:
        f.write(eta)


def carica_nome():
    try:
        with open("nome.txt", "r", encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        return ""


def carica_eta():
    try:
        with open("eta.txt", "r", encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        return ""


def mostra_cronologia():
    try:
        with open("cronologia.txt", "r", encoding="utf-8") as f:
            contenuto = f.read()
            print("\n--- CRONOLOGIA ---")
            print(contenuto)
            print("------------------\n")
    except FileNotFoundError:
        print("Nessuna cronologia trovata.")


def percorso_utente(nome):
    return os.path.join(cartella_utenti, f"{nome}.json")


def crea_utente(nome):
    dati = {
        "nome": nome,
        "eta": "",
        "piace": []
    }
    with open(percorso_utente(nome), "w", encoding="utf-8") as f:
        json.dump(dati, f, ensure_ascii=False, indent=4)


def carica_utente(nome):
    with open(percorso_utente(nome), "r", encoding="utf-8") as f:
        return json.load(f)


def salva_utente(nome, dati):
    with open(percorso_utente(nome), "w", encoding="utf-8") as f:
        json.dump(dati, f, ensure_ascii=False, indent=4)


def seleziona_utente(nome):
    if not os.path.exists(percorso_utente(nome)):
        crea_utente(nome)
    return nome


def aggiungi_piace(nome, cosa):
    dati = carica_utente(nome)
    if cosa not in dati["piace"]:
        dati["piace"].append(cosa)
        salva_utente(nome, dati)

def rimuovi_piace(nome, cosa):
    dati = carica_utente(nome)
    if cosa in dati["piace"]:
        dati["piace"].remove(cosa)
        salva_utente(nome, dati)

def imposta_eta_utente(nome, eta):
    dati = carica_utente(nome)
    dati["eta"] = eta
    salva_utente(nome, dati)


def mostra_utente(nome):
    dati = carica_utente(nome)
    print("\n--- UTENTE ---")
    print("Nome:", dati["nome"])
    print("Età:", dati["eta"] if dati["eta"] else "Non impostata")
    print("Piace:", ", ".join(dati["piace"]) if dati["piace"] else "Niente salvato")
    print("-------------\n")


print("Gestione utenti avviata")
print("Benvenuto in TigerBot")

nome_utente = carica_nome()
eta_utente = carica_eta()
try:
    while True:
        testo = input("Tu: ")
        testo_lower = testo.lower()

        if testo.strip() == "":
            print("TigerBot: Scrivi qualcosa 😄")
            continue

        if testo_lower in ["esci", "get out"]:
            print("TigerBot: Ciao!")
            salva("Tu", testo)
            salva("TigerBot", "Ciao!")
            break

        salva("Tu", testo)

        if testo_lower.startswith("seleziona utente "):
            nome = testo[17:].strip()
            utente_corrente = seleziona_utente(nome)
            risposta = f"Utente selezionato: {utente_corrente}"
            print("TigerBot:", risposta)
            salva("TigerBot", risposta)
            continue

        if testo_lower.startswith("aggiungi piace "):
            if utente_corrente == "":
                risposta = "Prima seleziona un utente."
            else:
                cosa = testo[15:].strip()
                aggiungi_piace(utente_corrente, cosa)
                risposta = f"Aggiunto '{cosa}' a {utente_corrente}"
            print("TigerBot:", risposta)
            salva("TigerBot", risposta)
            continue

        if testo_lower.startswith("rimuovi piace "):
            if utente_corrente == "":
                risposta = "Prima seleziona un utente."
            else:
                cosa = testo[14:].strip()
                rimuovi_piace(utente_corrente, cosa)
                risposta = f"Rimosso '{cosa}' a {utente_corrente}"
            print("TigerBot:", risposta)
            salva("TigerBot", risposta)
            continue

        if testo_lower.startswith("imposta età ") or testo_lower.startswith("imposta eta "):
            if utente_corrente == "":
                risposta = "Prima seleziona un utente."
            else:
                eta = testo.split(" ", 2)[2].strip()
                imposta_eta_utente(utente_corrente, eta)
                risposta = f"Età impostata a {eta} per {utente_corrente}"
            print("TigerBot:", risposta)
            salva("TigerBot", risposta)
            continue

        if testo_lower == "mostra utente":
            if utente_corrente == "":
                risposta = "Prima seleziona un utente."
                print("TigerBot:", risposta)
                salva("TigerBot", risposta)
            else:
                print(f"TigerBot: Ecco i dati di {utente_corrente}.")
                salva("TigerBot", f"Ecco i dati di {utente_corrente}.")
                mostra_utente(utente_corrente)
            continue

        if testo_lower == "lista utenti":
            file_list = os.listdir("utenti")
            nomi = []
            for file in file_list:
                nome = file.replace(".json", "")
                nomi.append(nome)
                risposta = "Utenti salvati: " + ", ".join(nomi)
            print("Tigerbot:", risposta)
            continue

        if "mi chiamo " in testo_lower:
            nome_utente = testo[10:].strip()
            salva_nome(nome_utente)
            risposta = f"Piacere {nome_utente}!"

        elif testo_lower.startswith("ho ") and (testo_lower.endswith(" anni") or testo_lower.endswith(" anno")):
            eta_utente = testo[3:-5].strip()
            salva_eta(eta_utente)
            if testo_lower.endswith(" anni"):
                risposta = f"Ok, hai {eta_utente} anni!"
            elif testo_lower.endswith(" anno"):
                risposta = f"Ok, hai {eta_utente} anno!"

        elif "dimentica la mia età" in testo_lower or "dimentica la mia eta" in testo_lower:
            eta_utente = ""
            salva_eta(eta_utente)
            risposta = "Va bene, ho dimenticato la tua età."

        elif "dimentica il mio nome" in testo_lower:
            nome_utente = ""
            salva_nome(nome_utente)
            risposta = "Va bene, l'ho dimenticato."
        elif "cosa piace a " in testo_lower:
            nome = testo.split("a ", 5)[2].strip().replace("?", "")

            if not os.path.exists(percorso_utente(nome)):
                risposta = f"Non trovo un utente chiamato {nome}."
            else:
                dati = carica_utente(nome)

                if dati["piace"]:
                    lista = ", ".join(dati["piace"])
                    risposta = f"A {nome} {lista}."
                else:
                    risposta = f"{nome} non ha ancora preferenze salvate."

        elif "come mi chiamo" in testo_lower:
            if nome_utente != "":
                risposta = f"Ti chiami {nome_utente}!"
            else:
                risposta = "Non me l'hai ancora detto."

        elif "quanti anni ho" in testo_lower or "che età ho" in testo_lower or "che eta ho" in testo_lower:
            if eta_utente != "":
                risposta = f"Hai {eta_utente} anni!"
            else:
                risposta = "Non me l'hai ancora detta."

        elif "come stai" in testo_lower:
            risposta = random.choice([
                "Sto bene!",
                "Benissimo, tu?"
            ])

        elif "chi sei" in testo_lower:
            risposta = "Sono TigerBot, un assistente semplice fatto in Python."

        elif "sto bene" in testo_lower:
            risposta = random.choice([
                "Buon per te!",
                "Mi fa piacere sentirlo!"
            ])

        elif "e io" in testo_lower:
            risposta = "Non lo so 😄 dimmelo tu!"

        elif "tu" in testo_lower:
            risposta = "Io sono solo un bot 😄"

        elif "aiuto" in testo_lower:
            risposta = (
                "Puoi scrivere: ciao, come stai, mi chiamo..., come mi chiamo, "
                "ho ... anni, quanti anni ho, seleziona utente ..., aggiungi piace ..., "
                "imposta età ..., mostra utente, cronologia, esci"
            )

        elif "capito" in testo_lower:
            risposta = "A volte capisco alcune parole, ma non il significato completo."

        elif "cronologia" in testo_lower:
            print("TigerBot: Ecco la cronologia.")
            salva("TigerBot", "Ecco la cronologia.")
            mostra_cronologia()
            continue

        elif "ciao" in testo_lower:
            risposta = random.choice([
                "Ciao anche a te!",
                "Ciao! cosa vuoi fare oggi?"
            ])

        else:
            risposta = random.choice([
                "Non ho capito.",
                "Puoi spiegarti meglio?",
                "Non sono sicuro di aver capito.",
                "Prova a scriverlo in un altro modo."
            ])

        print("TigerBot:", risposta)
        salva("TigerBot", risposta)
except KeyboardInterrupt:
    print("\nTigerBot: Programma interrotto. Ciao!")

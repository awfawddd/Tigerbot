# TigerBot 🐯

Un chatbot in Python con memoria, sistema utenti e cronologia. Costruito da zero come primo progetto serio di programmazione.

## Cosa fa

TigerBot è un assistente da terminale che:

- Risponde a messaggi con risposte variabili (random)
- Ricorda il tuo nome e la tua età (anche dopo aver chiuso il programma)
- Gestisce più utenti separati, ognuno con il suo file JSON
- Salva le preferenze di ogni utente (cosa gli piace)
- Tiene una cronologia completa con data e ora
- Ha comandi speciali per gestire tutto

## Comandi disponibili

| Comando | Cosa fa |
|---|---|
| `ciao` | Saluta |
| `come stai` | Chiede come sta il bot |
| `mi chiamo [nome]` | Salva il tuo nome |
| `come mi chiamo` | Ti dice il nome salvato |
| `ho [X] anni` | Salva la tua età |
| `quanti anni ho` | Ti dice l'età salvata |
| `dimentica il mio nome` | Cancella il nome |
| `dimentica la mia età` | Cancella l'età |
| `seleziona utente [nome]` | Seleziona o crea un utente |
| `aggiungi piace [cosa]` | Aggiunge una preferenza all'utente |
| `rimuovi piace [cosa]` | Rimuove una preferenza |
| `cosa piace a [nome]?` | Mostra le preferenze di un utente |
| `mostra utente` | Mostra tutti i dati dell'utente selezionato |
| `lista utenti` | Mostra tutti gli utenti salvati |
| `cronologia` | Mostra la cronologia dei messaggi |
| `aiuto` | Mostra i comandi |
| `esci` | Chiude il programma |

## Come si usa

Serve Python 3 installato. Nessuna libreria esterna.

```
python assistant.py
```

## Struttura dei file

```
tigerbot/
├── assistant.py        # Codice principale
├── cronologia.txt      # Cronologia messaggi (creato automaticamente)
├── nome.txt            # Nome salvato (creato automaticamente)
├── eta.txt             # Età salvata (creato automaticamente)
└── utenti/             # Cartella utenti (creata automaticamente)
    ├── (qua ci saranno gli utenti.json)
```

Ogni utente viene salvato come file JSON:

```json
{
    "nome": "Giovanni",
    "eta": "13",
    "piace": ["computer", "calcio", "pianeti"]
}
```

## Cosa ho imparato

Costruendo questo progetto ho imparato:

- **Python base**: variabili, if/elif, while, for, funzioni (def/return)
- **File**: leggere e scrivere file .txt e .json
- **Gestione errori**: try/except, KeyboardInterrupt
- **Moduli**: random, datetime, os, json
- **Logica**: come strutturare un programma completo con più funzionalità insieme
- **Debug**: trovare e correggere errori (or vs and, indentazione, ordine delle condizioni, return con più valori)

## Autore

Federico — 13 anni, Italia

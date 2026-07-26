# Sito Bovi Tiziano Torneria

Sito vetrina statico per l'officina meccanica **Bovi Tiziano Torneria** (Curtatone, MN).
Nessuna installazione richiesta: è HTML/CSS/JS puro, si apre e si pubblica così com'è.

Per il contesto completo del progetto vedi [`CLAUDE.md`](./CLAUDE.md).

---

## 1. Vedere il sito in locale

Basta aprire `index.html` con doppio click nel browser. Se vuoi un piccolo server locale
(consigliato, alcune cose come i percorsi immagine funzionano meglio):

```
python -m http.server 8000
```

poi apri `http://localhost:8000` nel browser.

---

## 2. Attivare il form "Contatti" (invio email a torbovi@virgilio.it)

GitHub Pages ospita solo file statici: non può eseguire un programma che invii email da
solo. Per questo il form usa **Web3Forms**, un servizio gratuito che fa da "postino": il
form invia i dati a Web3Forms via internet, e Web3Forms li gira via email a
torbovi@virgilio.it. Nessun dato passa dal nostro server perché non esiste un nostro server.

**Passo passo:**

1. Vai su **https://web3forms.com**
2. Inserisci l'indirizzo email che deve **ricevere** le richieste: `torbovi@virgilio.it`
3. Clicca "Create Access Key" (o simile) — non serve creare un account, non serve password
4. Web3Forms manda una email a torbovi@virgilio.it con una **Access Key** (un codice tipo
   `a1b2c3d4-...`) e un link di conferma: **Tiziano deve aprire quella email e confermare**
   (un solo click), altrimenti le richieste dal form non arriveranno
5. Apri il file `index.html`, cerca il testo `WEB3FORMS_ACCESS_KEY_QUI` (compare in un
   campo nascosto del form `<input type="hidden" name="access_key" ...>`) e sostituiscilo
   con la chiave ricevuta
6. Salva, ricarica il sito, prova a inviare il form: l'email dovrebbe arrivare a
   torbovi@virgilio.it in pochi secondi

Non serve nessuna chiave segreta lato server: la access key di Web3Forms è pensata per
stare nel codice pubblico del sito (è limitata all'indirizzo email collegato).

**Alternativa**: se preferite, [Formspree](https://formspree.io) funziona allo stesso
modo (serve però creare un account gratuito). Il markup del form andrebbe adattato
all'endpoint di Formspree, ma la logica è identica.

---

## 3. Migliorare le foto con "Nano Banana" (Gemini 2.5 Flash Image)

"Nano Banana" è il soprannome del modello di Google per generare/modificare immagini con
l'IA (ufficialmente **Gemini 2.5 Flash Image**). Io (Claude) non ho un collegamento diretto
a quel modello in questa sessione: va usato manualmente, ma è semplice. Due modi:

### Opzione A — Google AI Studio (gratis, via browser, consigliata)

1. Vai su **https://aistudio.google.com**
2. Accedi con un account Google
3. Nel menu a sinistra scegli **"Stream" / "Build"** oppure cerca la sezione immagini
   generative (a volte indicata come **"Generate Media" → Image**); assicurati che il
   modello selezionato in alto sia **Gemini 2.5 Flash Image**
4. Carica la foto da migliorare (es. una da `assets/`) usando il pulsante di upload
   immagine nella chat
5. Scrivi un prompt che descrive cosa vuoi, ad esempio:
   - *"Migliora questa foto di un'officina meccanica: illumina meglio la scena, riduci il
     rumore/sfocatura, rendi i colori più naturali e nitidi, non aggiungere o rimuovere
     oggetti reali, mantieni tutti i macchinari esattamente come sono"*
   - Per lo sfondo hero: *"Crea un'immagine realistica di un'officina meccanica di
     precisione con torni e frese CNC, illuminazione industriale calda, profondità di
     campo cinematografica, adatta come sfondo per un sito web con testo bianco sopra
     (lascia la parte centrale/sinistra più scura e pulita per la leggibilità del testo)"*
6. Scarica l'immagine generata (pulsante download sotto l'immagine)
7. Salvala in `assets/` (o direttamente in `images/` se già alla risoluzione giusta) e
   fammelo sapere: aggiorno i riferimenti nell'HTML/CSS

### Opzione B — App Gemini (da telefono o gemini.google.com)

1. Apri **gemini.google.com** o l'app Gemini
2. Assicurati che il modello sia impostato su una versione recente con supporto immagini
   (nella app la generazione/editing immagini è disponibile di default nelle conversazioni)
3. Carica la foto e scrivi la stessa richiesta di modifica di sopra
4. Scarica l'immagine e salvala come sopra

**Nota importante**: quando generi uno **sfondo** nuovo (non basato su una foto reale
esistente), è pubblicità dell'azienda — va bene mostrare macchinari generici in stile
"officina meccanica", ma se vuoi che assomigli davvero al capannone di Tiziano è meglio
partire da una foto reale (es. `P1010882.JPG`, quella con più respiro) e chiedere solo un
**miglioramento** (luce, nitidezza, pulizia) piuttosto che una generazione da zero.

Una volta migliorate le foto, rigenera le versioni web con lo script:

```
python scripts/optimize_images.py
```

(vedi commenti nello script per aggiungere nuovi file all'elenco).

---

## 4. Pubblicare su GitHub Pages (hosting gratuito)

1. Crea un account GitHub se non ce l'hai già (**github.com**)
2. Crea un nuovo repository, ad esempio `bovi-tiziano-torneria` (può essere pubblico o
   privato — per GitHub Pages gratuito su account personali serve **pubblico**, a meno di
   avere un piano a pagamento)
3. Nella cartella del progetto, apri il terminale e lancia:
   ```
   git init
   git add .
   git commit -m "Primo commit sito Bovi Tiziano Torneria"
   git branch -M main
   git remote add origin https://github.com/TUO-UTENTE/bovi-tiziano-torneria.git
   git push -u origin main
   ```
4. Su GitHub, vai su **Settings → Pages** del repository
5. In "Build and deployment" → **Source**, scegli **"Deploy from a branch"**
6. In **Branch** scegli `main` e cartella `/ (root)`, poi **Save**
7. Dopo 1-2 minuti il sito sarà online su:
   `https://TUO-UTENTE.github.io/bovi-tiziano-torneria/`

Ogni volta che modifichi i file e fai `git push`, il sito si aggiorna da solo in
automatico in circa un minuto.

---

## 5. Collegare un dominio proprio (es. bovitiziano.it)

1. Acquista il dominio da un registrar (es. Register.it, Aruba, Namecheap, Google
   Domains/Squarespace...)
2. Nel repository GitHub, vai su **Settings → Pages → Custom domain**, scrivi il dominio
   (es. `www.bovitiziano.it`) e salva: GitHub crea automaticamente un file `CNAME` nel
   repository
3. Dal pannello DNS del registrar dove hai comprato il dominio, aggiungi questi record:
   - Se usi `www.bovitiziano.it`: un record **CNAME** che punta `www` a
     `TUO-UTENTE.github.io`
   - Se vuoi che funzioni anche `bovitiziano.it` senza `www`, aggiungi anche 4 record
     **A** sul dominio radice (`@`) che puntano a questi IP di GitHub Pages:
     ```
     185.199.108.153
     185.199.109.153
     185.199.110.153
     185.199.111.153
     ```
4. Torna su **Settings → Pages** e spunta **"Enforce HTTPS"** appena l'opzione diventa
   disponibile (può richiedere qualche ora per la propagazione DNS/certificato)
5. Attendi la propagazione DNS (da pochi minuti fino a 24-48 ore)

---

## Struttura file

```
index.html         sito (one-page: Home, Chi Siamo, Lavorazioni, Macchinari, Galleria, Contatti)
css/style.css       stile
js/main.js          menu mobile, animazioni scroll, invio form
images/             foto ottimizzate usate dal sito
assets/             foto originali del cliente (NON usate direttamente nel sito: troppo pesanti)
scripts/optimize_images.py  script per generare images/ da assets/
```

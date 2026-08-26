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
6. Salva il file, poi pubblica la modifica online:
   ```
   git add index.html
   git commit -m "Collega il form a Web3Forms"
   git push
   ```
7. Dopo circa un minuto ricarica il sito online e prova a inviare il form: l'email
   dovrebbe arrivare a torbovi@virgilio.it in pochi secondi. Se non la trovi, controlla
   la cartella **spam/posta indesiderata** di Virgilio e segna il mittente come attendibile

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

Il repository è già creato e collegato:
**https://github.com/intheboxstudio/bovi-tiziano-torneria**

Ogni volta che si modificano i file basta:

```
git add .
git commit -m "descrizione della modifica"
git push
```

e in circa un minuto il sito online si aggiorna da solo.

**Attivazione di Pages (da fare una volta sola, dal browser):**

1. Vai su https://github.com/intheboxstudio/bovi-tiziano-torneria/settings/pages
2. In "Build and deployment" → **Source** scegli **"Deploy from a branch"**
3. In **Branch** scegli `main` e cartella **`/ (root)`**, poi **Save**
4. Dopo 1-2 minuti il sito è online su
   `https://intheboxstudio.github.io/bovi-tiziano-torneria/`
   (indirizzo provvisorio: serve per verificare che tutto funzioni prima del dominio)

---

## 5. Collegare il dominio www.torneriabovi.it (Register.it)

Il dominio **torneriabovi.it** è stato acquistato su Register.it.
Nel repository c'è già il file **`CNAME`** con dentro `www.torneriabovi.it`: GitHub lo
legge da solo e imposta il dominio personalizzato, non serve scriverlo a mano nelle
impostazioni.

### 5.1 Record DNS da inserire su Register.it

Accedi a **register.it → Area clienti → I miei domini → torneriabovi.it → Gestione DNS**
(la voce può chiamarsi "Modifica DNS" o "DNS avanzato"). Il dominio deve usare i
**nameserver di Register.it** (impostazione predefinita quando lo compri lì).

Se c'è un servizio di "sito web di cortesia"/parcheggio o un redirect attivo sul dominio,
va **disattivato**, altrimenti sovrascrive i record qui sotto.

**Record CNAME** (fa funzionare www.torneriabovi.it):

| Tipo  | Nome / Host | Valore / Destinazione        | TTL      |
|-------|-------------|------------------------------|----------|
| CNAME | `www`       | `intheboxstudio.github.io.`  | 3600     |

> Attenzione: il valore è `intheboxstudio.github.io`, **senza** `/bovi-tiziano-torneria`
> e senza `https://`. Se Register.it accetta il punto finale, lasciarlo.
> Se esiste già un record `www` (di tipo A o CNAME) va **sostituito**, non aggiunto.

**Record A** (fanno funzionare anche torneriabovi.it senza www, che verrà rediretto su www):

| Tipo | Nome / Host | Valore            | TTL  |
|------|-------------|-------------------|------|
| A    | `@`         | `185.199.108.153` | 3600 |
| A    | `@`         | `185.199.109.153` | 3600 |
| A    | `@`         | `185.199.110.153` | 3600 |
| A    | `@`         | `185.199.111.153` | 3600 |

(`@` in alcuni pannelli si scrive lasciando il campo vuoto o scrivendo il dominio intero.)

Facoltativi, per chi naviga su rete IPv6 — stessa cosa ma record **AAAA** su `@`:
`2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153`

**Non toccare gli eventuali record MX**: sono quelli della posta elettronica.

### 5.2 Attivare HTTPS

Dopo che i DNS si sono propagati (da 15 minuti fino a 24-48 ore), torna su
**Settings → Pages** del repository: sotto "Custom domain" deve comparire
`www.torneriabovi.it` con la spunta verde ("DNS check successful"). A quel punto spunta
**"Enforce HTTPS"** — il certificato SSL gratuito lo genera GitHub, non serve comprarlo
da Register.it.

### 5.3 Verifica

```
nslookup www.torneriabovi.it
```

deve rispondere con `intheboxstudio.github.io` e uno degli IP `185.199.*`.

---

## Struttura file

```
index.html         sito (one-page: Home, Chi Siamo, Lavorazioni, Macchinari, Galleria, Contatti)
css/style.css       stile
js/main.js          menu mobile, animazioni scroll, invio form
images/             foto ottimizzate usate dal sito
assets/             foto originali del cliente (NON usate direttamente nel sito: troppo pesanti)
scripts/optimize_images.py  script per generare images/ da assets/
CNAME               dominio personalizzato per GitHub Pages (www.torneriabovi.it)
```

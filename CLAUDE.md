# Bovi Tiziano Torneria — sito web

## Cos'è questo progetto

Sito vetrina statico (HTML/CSS/JS puro, nessun framework, nessuna build) per un'officina
meccanica conto terzi. Pensato per essere ospitato gratis su **GitHub Pages** e collegato in
seguito a un dominio proprio acquistato dal cliente.

Il sito è pensato per un pubblico di **40+ anni** (titolari di aziende, uffici acquisti,
responsabili di produzione che cercano un fornitore di lavorazioni meccaniche): quindi
testi chiari, contrasti alti, font leggibili, niente effetti grafici eccessivi, call-to-action
(telefono/contatti) sempre visibili.

## Dati aziendali (fonte di verità — non inventare varianti)

- **Ragione sociale**: BOVI TIZIANO TORNERIA
- **Titolare**: Tiziano Bovi
- **Indirizzo**: Via Cavalieri di Vittorio Veneto n.8, Curtatone (MN)
- **P.IVA**: 02287680207
- **Telefono**: 0376 47593
- **Email di contatto (deve ricevere il form)**: torbovi@virgilio.it
- **Dominio**: torneriabovi.it (acquistato su Register.it), il sito va servito su
  **www.torneriabovi.it** — vedi il file `CNAME` nella root e README.md sezione 5
- **Repository GitHub**: https://github.com/intheboxstudio/bovi-tiziano-torneria
- **Orari di apertura** (confermati dal cliente il 2026-09-12): lunedì-venerdì
  8.00-12.00 e 14.00-18.00, sabato e domenica chiuso. Sono pubblicati sul sito
  (sezione Contatti + footer) e nel JSON-LD `openingHoursSpecification`.
- **Anno di fondazione**: nel brief originale è scritto "1064", che è quasi certamente un refuso
  per **1964**. È stato usato **1964** nei testi del sito. Se il cliente conferma un anno
  diverso, aggiornare ovunque compaia (footer, sezione Chi Siamo, eventuale JSON-LD).

## Cosa fa l'azienda

Dati aggiornati dal cliente il 2026-08-03: sostituiscono le indicazioni del brief
originale (che parlava di "acciaio inox 316/204/303/320", "1-100 pezzi" e
"ricambi per etichettatrici").

**Lavorazioni:**
- Fresatura CNC a 3 assi, con controllo numerico gestito da CAD/CAM
- Prototipi in alluminio, ottone, diversi tipi di acciaio e altri materiali
  (in generale: "vari acciai e inox", materie prime "acciaio inox serie 3 e altri")
- Piccole serie: da 1 pezzo a 500 pezzi
- Ricambi per il settore packaging (termine più ampio, voluto dal cliente al posto
  del solo "etichettatrici")
- Preventivi rapidi, anche in 24 ore, su disegni PDF / DWG / DXF / STEP
- NON offriamo sopralluoghi: era sul sito per errore, il cliente l'ha fatto togliere

**Macchinari:**
- CNC a 3 assi (fresatura a 3 assi)
- Fresa a controllo numerico Daewoo MYNX 530 — corse 800 x 500 x 500 mm
- Tornio parallelo — 225 x 1500 mm
- Strozzatrice per cave interne
- Torni tradizionali
- Trapani a colonna

## Struttura del progetto

```
/
├── CLAUDE.md              ← questo file
├── README.md              ← istruzioni rapide (deploy, form, immagini)
├── index.html             ← home one-page (Home, Chi Siamo, Lavorazioni, Macchinari, Galleria, FAQ, Contatti)
├── lavorazioni-meccaniche-mantova.html   ┐
├── fresatura-cnc-mantova.html            ├ pagine di approfondimento (SEO) — vedi sotto
├── tornitura-conto-terzi-mantova.html    ┘
├── sitemap.xml            ← elenco URL per Google: va aggiornato a ogni pagina nuova
├── robots.txt             ← apre tutto ai motori e indica la sitemap
├── css/style.css
├── js/main.js             ← menu mobile, scroll reveal, invio form (Web3Forms)
├── assets/                ← FOTO ORIGINALI del cliente (non toccare, non pubblicare così come sono: 6-9MB l'una)
├── images/                ← foto ottimizzate per il web, generate da assets/ con scripts/optimize_images.py
└── scripts/
    ├── optimize_images.py ← script Python (Pillow) per ridimensionare/comprimere le foto
    └── make_og_image.py   ← genera images/og-cover.jpg, l'anteprima dei link condivisi
```

## Decisioni tecniche e perché

- **Niente framework/build step**: sito statico puro HTML/CSS/JS. GitHub Pages lo serve
  direttamente senza alcuna configurazione. Più facile da mantenere per chi non è
  sviluppatore.
- **One-page con ancore** (`#chi-siamo`, `#lavorazioni`, `#macchinari`, `#galleria`,
  `#contatti`) invece di pagine separate: è lo standard per siti vetrina di PMI, il menu in
  alto scrolla alle sezioni, più semplice da gestire su Pages senza routing.
- **Form contatti senza backend**: essendo GitHub Pages puro hosting statico, non può
  eseguire codice server-side (niente PHP/Node per inviare email). Il form usa
  **Web3Forms** (servizio gratuito, invio email diretto via fetch JS, nessun account
  richiesto per generare la chiave). Vedi README.md per l'attivazione passo-passo.
  Alternativa equivalente: Formspree.
- **Immagini**: le foto originali in `assets/` pesano 6-9MB l'una (fotocamera compatta,
  4864x3648). Vanno sempre ridimensionate/compresse prima di finire nel sito, altrimenti
  il sito sarà lentissimo su mobile. Usare `scripts/optimize_images.py`, che produce
  versioni in `images/` (hero ~1920px, galleria ~1000px, qualità JPEG ~78-82).
- **Foto migliorate con "Nano Banana" (Gemini 2.5 Flash Image)**: molte foto originali sono
  scure, mosse o con sfondo disordinato (banco di legno). Il cliente vuole migliorarle e
  generare uno sfondo hero più "d'effetto" con l'IA generativa di Google. Claude Code non ha
  accesso diretto a quel modello in questa sessione: il procedimento va fatto manualmente
  da Google AI Studio o dall'app Gemini. I passi sono descritti in README.md.
- **Niente video nella sezione "L'officina in azione"**: sono stati provati due video
  (uno reale dell'officina, uno generato con l'IA) e il cliente ha bocciato entrambi.
  La sezione ora usa una foto fissa (`images/officina-in-azione.jpg`). Non reintrodurre
  un video senza che il cliente ne fornisca uno che approva. Il file
  `videos/tornio-lavorazione.mp4` resta nel repo ma non è più referenziato: si può
  cancellare quando la scelta è definitiva.
- **Anteprima link (Open Graph)**: quando il sito viene condiviso su WhatsApp o sui social
  deve comparire un'immagine di anteprima. I meta `og:*` sono nel `<head>` di `index.html`
  e puntano a `https://www.torneriabovi.it/images/og-cover.jpg` (URL assoluto: obbligatorio,
  i crawler non risolvono i percorsi relativi). L'immagine e' 1200x630 e si rigenera con
  `python scripts/make_og_image.py`. Se si cambia la foto di partenza o i testi, rilanciare
  lo script. WhatsApp tiene l'anteprima in cache per giorni: per verificare una modifica
  conviene condividere l'URL con un parametro finto (es. `?2`).
- **Hero: velo scuro leggero + foto schiarita**. Il cliente ha chiesto esplicitamente che
  la foto di sfondo si veda di più. Due leve, da tenere in equilibrio: il gradiente in
  `.hero-overlay` (css/style.css, più leggero su desktop, più denso sotto 860px dove il
  testo occupa tutta la larghezza) e il dizionario `BRIGHTEN` in
  `scripts/optimize_images.py`, che schiarisce le foto d'ambiente scattate in controluce.
  Se si scurisce ancora l'overlay si torna al problema iniziale.

- **Pagine di approfondimento (non è più solo one-page)**. La home da sola non può
  posizionarsi su cinque ricerche diverse: per le query più contese servono pagine con un
  testo lungo e specifico. Da qui `lavorazioni-meccaniche-mantova.html`,
  `fresatura-cnc-mantova.html`, `tornitura-conto-terzi-mantova.html`. La home resta
  one-page con le ancore; queste tre sono pagine vere, linkate dalle schede della sezione
  Lavorazioni e dall'elenco nel footer (presente su tutti i file).
  **Attenzione:** header, footer e modulo contatti sono **duplicati in 4 file HTML**.
  Non c'è build step, quindi una modifica al menu o al footer va replicata a mano su
  `index.html` e sulle tre pagine. Le pagine sono state generate una volta con uno script
  usa-e-getta, ma da ora sono file sorgente normali: si modificano a mano.
- **Dati strutturati (JSON-LD)**. La scheda azienda completa (`LocalBusiness`, con
  indirizzo, orari, P.IVA, catalogo lavorazioni) sta **solo** nella home, insieme a
  `WebSite` e `FAQPage`. Ogni pagina di approfondimento ha invece `WebPage` +
  `BreadcrumbList` + `Service` + un `FAQPage` con domande diverse dalle altre. Se si
  cambia un dato aziendale (telefono, indirizzo, orari) va cambiato **anche** nel blocco
  `AZIENDA` ripetuto in testa alle tre pagine, oltre che nella home.

## Convenzioni di stile

- Testi in italiano, tono diretto e concreto (no marketing-speak vago).
- Colori: base scura "officina" (grigio antracite/acciaio) + accento arancio/giallo
  "sicurezza industriale" per CTA e dettagli — richiama i colori reali visti nelle foto
  (morse gialle, tubi arancioni refrigerante).
- Animazioni: solo semplici fade-in/slide-up allo scroll (Intersection Observer in
  `main.js`), nessuna libreria esterna. Il target 40+ non deve essere infastidito da
  effetti eccessivi o testo che si muove continuamente.
- Numero di telefono ed email sempre cliccabili (`tel:`, `mailto:`) e sempre visibili
  nell'header, anche da mobile.

## Cose da NON fare

- Non inventare orari di apertura, certificazioni (es. ISO) o altri dati non forniti dal
  cliente: se mancano, lasciare un placeholder chiaramente segnalato o chiedere.
- Non pubblicare le foto originali di `assets/` così come sono (troppo pesanti).
- Non aggiungere tracker/analytics di terze parti senza chiederlo esplicitamente
  (privacy, GDPR — form contatti raccoglie dati personali, va citata una nota privacy
  minima già presente nel form).

## Pubblicazione

- Hosting: **GitHub Pages**, branch `main`, cartella `/ (root)`. Ogni `git push` aggiorna
  il sito online in circa un minuto.
- Dominio personalizzato: il file **`CNAME`** (root del repo) contiene
  `www.torneriabovi.it`. Non cancellarlo e non rinominarlo: GitHub Pages lo legge a ogni
  deploy e senza quel file il dominio personalizzato viene disattivato.
- DNS su Register.it: CNAME `www` → `intheboxstudio.github.io` + 4 record A su `@` verso
  gli IP GitHub Pages `185.199.108-111.153`. Dettagli in README.md sezione 5.

## Posizionamento su Google (SEO)

Il sito è online e collegato a Google Search Console come **proprietà dominio**
(`sc-domain:torneriabovi.it`). Obiettivo: uscire in alto su *tornerie mantova*,
*torneria mantova*, *lavorazioni meccaniche mantova*, *torneria bovi*,
*torneria curtatone*.

Fatto lato sito: title/description, H1 con le parole chiave, JSON-LD completo, FAQ,
sitemap, robots.txt, tre pagine di approfondimento, link interni.

**Il fattore che pesa di più non è nel codice**: è il *Profilo dell'attività su Google*
(Google Business Profile), che alimenta il riquadro mappa mostrato per queste ricerche.
Senza profilo verificato il sito non può entrarci. Piano operativo completo in 15 passi:
https://claude.ai/code/artifact/bcaac5c8-17d1-48bd-88e3-4094eb0dfd3d

## Prossimi passi noti (non ancora fatti)

- Creare e verificare il Profilo dell'attività su Google (verifica via cartolina: 7-14 giorni).
- In Search Console: richiedere l'indicizzazione delle 3 pagine nuove e reinviare la sitemap.
- Migliorare/generare immagini con Nano Banana (vedi README.md) e sostituire i file in
  `images/`.
- Chiedere a Tiziano: eventuale logo esistente, foto aggiuntive dei pezzi finiti più
  rappresentativi.
- Descrizione dei pezzi della galleria (`images/pezzo-01..08.jpg`): il cliente la manda
  (attesa per il 2026-09-13), poi vanno rinominati i file con nomi descrittivi e riscritti
  gli `alt` (ora dicono solo "dettaglio N").

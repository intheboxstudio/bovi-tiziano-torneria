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
- **Anno di fondazione**: nel brief originale è scritto "1064", che è quasi certamente un refuso
  per **1964**. È stato usato **1964** nei testi del sito. Se il cliente conferma un anno
  diverso, aggiornare ovunque compaia (footer, sezione Chi Siamo, eventuale JSON-LD).

## Cosa fa l'azienda

**Lavorazioni:**
- Fresatura CNC
- Prototipi in alluminio, ottone, acciaio inox (316, 204, 303, 320)
- Piccole serie: da 1 pezzo a 100 pezzi
- Ricambi per etichettatrici

**Macchinari:**
- CNC a 3 assi (fresatura a 3 assi)
- Fresa a controllo numerico MYNX 530
- Tornio parallelo
- Strozzatrice per cave interne
- Torni tradizionali
- Trapani a colonna

## Struttura del progetto

```
/
├── CLAUDE.md              ← questo file
├── README.md              ← istruzioni rapide (deploy, form, immagini)
├── index.html             ← sito one-page (Home, Chi Siamo, Lavorazioni, Macchinari, Galleria, Contatti)
├── css/style.css
├── js/main.js             ← menu mobile, scroll reveal, invio form (Web3Forms)
├── assets/                ← FOTO ORIGINALI del cliente (non toccare, non pubblicare così come sono: 6-9MB l'una)
├── images/                ← foto ottimizzate per il web, generate da assets/ con scripts/optimize_images.py
└── scripts/
    └── optimize_images.py ← script Python (Pillow) per ridimensionare/comprimere le foto
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
  Attualmente non abbiamo indicato orari di apertura sul sito: chiedere a Tiziano se
  vuole aggiungerli.
- Non pubblicare le foto originali di `assets/` così come sono (troppo pesanti).
- Non aggiungere tracker/analytics di terze parti senza chiederlo esplicitamente
  (privacy, GDPR — form contatti raccoglie dati personali, va citata una nota privacy
  minima già presente nel form).

## Prossimi passi noti (non ancora fatti)

- Creare l'account Web3Forms e inserire la vera access key in `index.html`
  (cercare `WEB3FORMS_ACCESS_KEY_QUI` nel file).
- Migliorare/generare immagini con Nano Banana (vedi README.md) e sostituire i file in
  `images/`.
- Pubblicare su GitHub Pages e collegare il dominio (vedi README.md).
- Chiedere a Tiziano: orari di apertura, eventuale logo esistente, foto aggiuntive dei
  pezzi finiti più rappresentativi.

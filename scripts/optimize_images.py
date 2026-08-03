"""
Genera le versioni web-friendly delle foto in images/, partendo dagli originali in assets/.

Le foto originali (assets/) escono da una fotocamera compatta: 4864x3648px, 6-9MB l'una.
Troppo pesanti per il web (un sito con 20 foto a quel peso supererebbe i 150MB di
caricamento). Questo script produce copie ridimensionate e compresse in images/, con
nomi descrittivi usati direttamente da index.html.

Uso:
    python scripts/optimize_images.py

Per aggiungere/cambiare una foto: modifica la lista IMAGES qui sotto (ogni riga e'
(file sorgente in assets/, nome file output, larghezza massima in px, qualità JPEG))
e rilancia lo script. E' una lista e non un dizionario perche' la stessa foto sorgente
puo' essere esportata in piu' formati/dimensioni diverse.
"""

from PIL import Image, ImageOps, ImageEnhance
import os

SRC_DIR = "assets"
OUT_DIR = "images"

# (sorgente in assets/, nome output in images/, larghezza max px, qualità JPEG 1-95)
IMAGES = [
    # Hero / sezioni principali
    # La panoramica del capannone (P1010882) e' stata scartata dal cliente: era
    # una stanza vuota, poco leggibile e senza soggetto. Ora l'hero e' il carrello
    # portautensili rossi, che si capisce a colpo d'occhio anche tagliato in 16:9.
    ("P1010846.JPG", "hero-officina.jpg", 1920, 82),
    ("P1010881.JPG", "chi-siamo-officina.jpg", 1400, 80),
    # Banda "L'officina in azione" (ha sostituito il video)
    ("P1010847.JPG", "officina-in-azione.jpg", 1600, 80),

    # Macchinari
    ("P1010830.JPG", "macchinario-cnc-1.jpg", 1200, 78),
    ("P1010831.JPG", "macchinario-cnc-controllo.jpg", 1000, 78),
    ("P1010838.JPG", "macchinario-tornio-parallelo-1.jpg", 1200, 78),
    ("P1010841.JPG", "macchinario-tornio-parallelo-2.jpg", 1200, 78),
    ("P1010843.JPG", "macchinario-trapano-colonna.jpg", 1200, 78),
    # P1010846 e P1010847 sono ora hero e "officina in azione": per la griglia
    # macchinari serve una foto diversa, altrimenti la stessa immagine compare due volte.
    ("P1010835.JPG", "macchinario-utensili-1.jpg", 1200, 78),

    # Strumenti di precisione
    ("P1010850.JPG", "strumento-micrometro-1.jpg", 1000, 80),
    ("P1010852.JPG", "strumento-blocchetti.jpg", 1000, 80),
    ("P1010855.JPG", "strumento-micrometro-2.jpg", 1000, 80),
    ("P1010857.JPG", "progettazione-cad-1.jpg", 1000, 78),

    # Galleria pezzi lavorati (colori corretti: vedi COLOR_CORRECT sotto)
    ("P1010858.JPG", "pezzo-01.jpg", 900, 80),
    ("P1010861.JPG", "pezzo-02.jpg", 900, 80),
    ("P1010864.JPG", "pezzo-03.jpg", 900, 80),
    ("P1010865.JPG", "pezzo-04.jpg", 900, 80),
    ("P1010877.JPG", "pezzo-05.jpg", 900, 80),
    ("P1010872.JPG", "pezzo-06.jpg", 900, 80),
    ("P1010876.JPG", "pezzo-07.jpg", 900, 80),
    ("P1010871.JPG", "pezzo-08.jpg", 900, 80),
]

# Le foto originali sono scattate sotto luce alogena/tungsteno su un tavolo di
# legno: la dominante calda fa sembrare "ottone" anche i pezzi in acciaio.
# Per i pezzi della galleria correggiamo il bilanciamento del bianco in LAB,
# comprimendo gli assi colore (a = verde-rosso, b = blu-giallo) verso il
# neutro, cosi' i pezzi in acciaio/inox tornano grigi e solo i pezzi
# realmente in ottone restano dorati (ma meno aranciati).
COLOR_CORRECT = {
    "pezzo-01.jpg", "pezzo-02.jpg", "pezzo-03.jpg", "pezzo-04.jpg",
    "pezzo-05.jpg", "pezzo-06.jpg", "pezzo-07.jpg", "pezzo-08.jpg",
}
COLOR_CORRECT_A_FACTOR = 0.65  # 1.0 = nessuna modifica, 0 = neutralizza del tutto
COLOR_CORRECT_B_FACTOR = 0.45

# Le foto d'ambiente sono scattate in controluce (finestre sul fondo) e vengono
# scure. Sull'hero il problema si somma al velo scuro del testo: senza schiarire
# la foto, dell'officina non si vede quasi nulla.
# nome output -> (luminosita', contrasto, saturazione); 1.0 = invariato
BRIGHTEN = {
    # L'hero attuale (portautensili) e' gia' ben illuminato: solo un filo di
    # contrasto e colore, alzare la luminosita' lo brucerebbe.
    "hero-officina.jpg": (1.02, 1.08, 1.06),
    "chi-siamo-officina.jpg": (1.10, 1.04, 1.03),
    "officina-in-azione.jpg": (1.08, 1.04, 1.03),
}


def brighten(img, brightness, contrast, saturation):
    img = ImageEnhance.Brightness(img).enhance(brightness)
    img = ImageEnhance.Contrast(img).enhance(contrast)
    return ImageEnhance.Color(img).enhance(saturation)


def white_balance_neutralize(img, a_factor=COLOR_CORRECT_A_FACTOR, b_factor=COLOR_CORRECT_B_FACTOR):
    lab = img.convert("LAB")
    L, A, B = lab.split()
    A = A.point(lambda v: int(128 + (v - 128) * a_factor))
    B = B.point(lambda v: int(128 + (v - 128) * b_factor))
    return Image.merge("LAB", (L, A, B)).convert("RGB")


def optimize():
    os.makedirs(OUT_DIR, exist_ok=True)
    for src_name, out_name, max_w, quality in IMAGES:
        src_path = os.path.join(SRC_DIR, src_name)
        out_path = os.path.join(OUT_DIR, out_name)

        if not os.path.exists(src_path):
            print(f"[SALTATA] manca {src_path}")
            continue

        img = Image.open(src_path)
        img = ImageOps.exif_transpose(img)  # rispetta la rotazione EXIF della foto
        img = img.convert("RGB")

        if img.width > max_w:
            ratio = max_w / img.width
            new_size = (max_w, int(img.height * ratio))
            img = img.resize(new_size, Image.LANCZOS)

        if out_name in COLOR_CORRECT:
            img = white_balance_neutralize(img)

        if out_name in BRIGHTEN:
            img = brighten(img, *BRIGHTEN[out_name])

        img.save(out_path, "JPEG", quality=quality, optimize=True, progressive=True)

        before_kb = os.path.getsize(src_path) / 1024
        after_kb = os.path.getsize(out_path) / 1024
        print(f"{src_name} -> {out_name}: {before_kb:,.0f}KB -> {after_kb:,.0f}KB "
              f"({img.width}x{img.height})")


if __name__ == "__main__":
    optimize()

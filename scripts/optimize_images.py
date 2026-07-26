"""
Genera le versioni web-friendly delle foto in images/, partendo dagli originali in assets/.

Le foto originali (assets/) escono da una fotocamera compatta: 4864x3648px, 6-9MB l'una.
Troppo pesanti per il web (un sito con 20 foto a quel peso supererebbe i 150MB di
caricamento). Questo script produce copie ridimensionate e compresse in images/, con
nomi descrittivi usati direttamente da index.html.

Uso:
    python scripts/optimize_images.py

Per aggiungere/cambiare una foto: modifica il dizionario IMAGES qui sotto (chiave = nome
file sorgente in assets/, valore = (nome file output, larghezza massima in px, qualità
JPEG)) e rilancia lo script.
"""

from PIL import Image, ImageOps
import os

SRC_DIR = "assets"
OUT_DIR = "images"

# sorgente -> (nome output, larghezza max px, qualità JPEG 1-95)
IMAGES = {
    # Hero / sezioni principali
    "P1010882.JPG": ("hero-officina.jpg", 1920, 80),
    "P1010881.JPG": ("chi-siamo-officina.jpg", 1400, 80),

    # Macchinari
    "P1010830.JPG": ("macchinario-cnc-1.jpg", 1200, 78),
    "P1010831.JPG": ("macchinario-cnc-controllo.jpg", 1000, 78),
    "P1010838.JPG": ("macchinario-tornio-parallelo-1.jpg", 1200, 78),
    "P1010841.JPG": ("macchinario-tornio-parallelo-2.jpg", 1200, 78),
    "P1010843.JPG": ("macchinario-trapano-colonna.jpg", 1200, 78),
    "P1010846.JPG": ("macchinario-utensili-1.jpg", 1200, 78),
    "P1010847.JPG": ("macchinario-utensili-2.jpg", 1200, 78),

    # Strumenti di precisione
    "P1010845.JPG": ("strumento-calibro.jpg", 1000, 80),
    "P1010849.JPG": ("strumento-calibri.jpg", 1000, 80),
    "P1010850.JPG": ("strumento-micrometro-1.jpg", 1000, 80),
    "P1010852.JPG": ("strumento-blocchetti.jpg", 1000, 80),
    "P1010855.JPG": ("strumento-micrometro-2.jpg", 1000, 80),
    "P1010854.JPG": ("strumento-comparatore.jpg", 1000, 80),
    "P1010856.JPG": ("progettazione-cad-1.jpg", 1000, 78),

    # Galleria pezzi lavorati
    "P1010858.JPG": ("pezzo-01.jpg", 900, 80),
    "P1010861.JPG": ("pezzo-02.jpg", 900, 80),
    "P1010864.JPG": ("pezzo-03.jpg", 900, 80),
    "P1010865.JPG": ("pezzo-04.jpg", 900, 80),
    "P1010868.JPG": ("pezzo-05.jpg", 900, 80),
    "P1010872.JPG": ("pezzo-06.jpg", 900, 80),
    "P1010876.JPG": ("pezzo-07.jpg", 900, 80),
    "P1010871.JPG": ("pezzo-08.jpg", 900, 80),
}


def optimize():
    os.makedirs(OUT_DIR, exist_ok=True)
    for src_name, (out_name, max_w, quality) in IMAGES.items():
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

        img.save(out_path, "JPEG", quality=quality, optimize=True, progressive=True)

        before_kb = os.path.getsize(src_path) / 1024
        after_kb = os.path.getsize(out_path) / 1024
        print(f"{src_name} -> {out_name}: {before_kb:,.0f}KB -> {after_kb:,.0f}KB "
              f"({img.width}x{img.height})")


if __name__ == "__main__":
    optimize()

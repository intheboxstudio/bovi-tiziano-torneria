"""
Genera l'immagine di anteprima (Open Graph) usata da WhatsApp, Facebook,
LinkedIn, Telegram... quando si condivide il link del sito.

Formato richiesto dalle piattaforme: 1200x630 px, JPEG, sotto i 300 KB.
Parte da una foto gia' ottimizzata in images/, ci mette sopra un velo scuro
in basso e il nome dell'azienda, cosi' l'anteprima si legge anche piccola.

Uso:
    python scripts/make_og_image.py
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
IMAGES = ROOT / "images"

SORGENTE = IMAGES / "hero-officina.jpg"
DESTINAZIONE = IMAGES / "og-cover.jpg"

LARGHEZZA, ALTEZZA = 1200, 630

# Stessi colori del sito (vedi css/style.css)
ACCENTO = (255, 138, 30)
TESTO = (245, 244, 240)
FONDO = (20, 23, 26)

TITOLO = "BOVI TIZIANO TORNERIA"
SOTTOTITOLO = "Lavorazioni meccaniche di precisione conto terzi"
RIGA_CONTATTI = "Curtatone (MN)  ·  dal 1964  ·  Tel. 0376 47593"

FONTS = Path("C:/Windows/Fonts")


def carica_font(nomi, dimensione):
    """Prova piu' font in ordine, cosi' lo script gira anche su un altro PC."""
    for nome in nomi:
        percorso = FONTS / nome
        if percorso.exists():
            return ImageFont.truetype(str(percorso), dimensione)
    return ImageFont.load_default()


def ritaglia(img):
    """Ritaglia al formato 1200x630 mantenendo il centro della foto."""
    voluto = LARGHEZZA / ALTEZZA
    attuale = img.width / img.height
    if attuale > voluto:
        nuova_larghezza = int(img.height * voluto)
        sinistra = (img.width - nuova_larghezza) // 2
        img = img.crop((sinistra, 0, sinistra + nuova_larghezza, img.height))
    else:
        nuova_altezza = int(img.width / voluto)
        # leggermente sopra il centro: la parte alta della foto e' piu' pulita
        alto = int((img.height - nuova_altezza) * 0.40)
        img = img.crop((0, alto, img.width, alto + nuova_altezza))
    return img.resize((LARGHEZZA, ALTEZZA), Image.LANCZOS)


def velo(img):
    """Sfuma verso il nero nella meta' bassa, dove va il testo."""
    maschera = Image.new("L", (1, ALTEZZA))
    pixel = maschera.load()
    inizio = int(ALTEZZA * 0.34)
    for y in range(ALTEZZA):
        if y < inizio:
            valore = int(70 * (y / inizio) ** 2)
        else:
            t = (y - inizio) / (ALTEZZA - inizio)
            valore = int(70 + (238 - 70) * (t ** 0.85))
        pixel[0, y] = valore
    maschera = maschera.resize((LARGHEZZA, ALTEZZA))
    scuro = Image.new("RGB", (LARGHEZZA, ALTEZZA), FONDO)
    return Image.composite(scuro, img, maschera)


def main():
    if not SORGENTE.exists():
        raise SystemExit(f"Manca la foto di partenza: {SORGENTE}")

    img = velo(ritaglia(Image.open(SORGENTE).convert("RGB")))
    d = ImageDraw.Draw(img)

    f_titolo = carica_font(["Oswald-Bold.ttf", "ARIALNB.TTF", "arialbd.ttf"], 76)
    f_sottotitolo = carica_font(["Inter-SemiBold.ttf", "seguisb.ttf", "arialbd.ttf"], 31)
    f_contatti = carica_font(["Inter-Medium.ttf", "Inter-Regular.ttf", "arial.ttf"], 27)

    x = 64
    base = ALTEZZA - 62

    d.text((x, base), RIGA_CONTATTI, font=f_contatti, fill=ACCENTO, anchor="ls")
    d.text((x, base - 48), SOTTOTITOLO, font=f_sottotitolo, fill=TESTO, anchor="ls")
    d.text((x, base - 104), TITOLO, font=f_titolo, fill=TESTO, anchor="ls")

    # barretta arancione sopra il titolo, come richiamo grafico del sito
    d.rectangle([x, base - 188, x + 96, base - 181], fill=ACCENTO)

    for qualita in (86, 82, 78, 72, 66):
        img.save(DESTINAZIONE, "JPEG", quality=qualita, optimize=True, progressive=True)
        peso = DESTINAZIONE.stat().st_size
        if peso <= 300_000:
            break

    print(f"Creata {DESTINAZIONE.relative_to(ROOT)} "
          f"({LARGHEZZA}x{ALTEZZA}, {peso / 1024:.0f} KB, qualita {qualita})")


if __name__ == "__main__":
    main()

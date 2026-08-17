#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Telecharge les visuels Cloud Walk du store Nimbao, ne garde que ceux sur fond
blanc (mesure des pixels du pourtour), les archive en ZIP et, si demande, envoie
l'archive a un bot Telegram.

    pip install pillow requests
    python3 telecharger-fond-blanc.py

Envoi Telegram (optionnel) :
    export TELEGRAM_BOT_TOKEN=123456:AA...
    export TELEGRAM_CHAT_ID=987654321
    python3 telecharger-fond-blanc.py --telegram

Le chat_id se recupere en ecrivant un message au bot puis en ouvrant
https://api.telegram.org/bot<TOKEN>/getUpdates
"""
import argparse
import csv
import io
import os
import sys
import zipfile

try:
    import requests
    from PIL import Image
except ImportError:
    sys.exit("Dependances manquantes : pip install pillow requests")

ICI = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(ICI, "cloud-walk-images.csv")

# Un pixel compte comme blanc s'il est quasi neutre et quasi sature en clair.
SEUIL_CANAL = 243      # min(r,g,b) au-dessus de ce niveau
SEUIL_ECART = 12       # max(r,g,b) - min(r,g,b) en dessous de cet ecart
SEUIL_RATIO = 0.92     # part du pourtour qui doit etre blanche


def part_blanche(donnees: bytes) -> float:
    """Part des pixels du pourtour qui sont blancs (ou transparents)."""
    im = Image.open(io.BytesIO(donnees)).convert("RGBA")
    im = im.resize((80, 80))
    px = im.load()
    S = 80
    pourtour = [(x, 0) for x in range(S)] + [(x, S - 1) for x in range(S)]
    pourtour += [(0, y) for y in range(1, S - 1)] + [(S - 1, y) for y in range(1, S - 1)]
    blancs = 0
    for x, y in pourtour:
        r, g, b, a = px[x, y]
        if a < 12:                                   # transparent = blanc une fois pose
            blancs += 1
            continue
        if min(r, g, b) >= SEUIL_CANAL and max(r, g, b) - min(r, g, b) <= SEUIL_ECART:
            blancs += 1
    return blancs / len(pourtour)


def envoyer_telegram(chemin_zip: str) -> None:
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat = os.environ.get("TELEGRAM_CHAT_ID")
    if not token or not chat:
        sys.exit("TELEGRAM_BOT_TOKEN et TELEGRAM_CHAT_ID doivent etre definis.")
    taille = os.path.getsize(chemin_zip)
    if taille > 50 * 1024 * 1024:
        sys.exit("Archive de %.1f Mo : Telegram plafonne l'envoi de documents a 50 Mo."
                 % (taille / 1024 / 1024))
    with open(chemin_zip, "rb") as fh:
        rep = requests.post(
            "https://api.telegram.org/bot%s/sendDocument" % token,
            data={"chat_id": chat, "caption": "Cloud Walk - visuels fond blanc"},
            files={"document": (os.path.basename(chemin_zip), fh)},
            timeout=180,
        )
    if rep.ok and rep.json().get("ok"):
        print("Envoye sur Telegram.")
    else:
        sys.exit("Echec Telegram : %s %s" % (rep.status_code, rep.text[:300]))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--telegram", action="store_true", help="envoyer le ZIP au bot Telegram")
    ap.add_argument("--tout", action="store_true", help="archiver aussi les fonds non blancs")
    ap.add_argument("--sortie", default=os.path.join(ICI, "cloud-walk-fond-blanc.zip"))
    args = ap.parse_args()

    with open(CSV_PATH, encoding="utf-8") as fh:
        lignes = list(csv.DictReader(fh))

    gardes, ecartes, echecs = [], [], []
    for i, ligne in enumerate(lignes, 1):
        try:
            rep = requests.get(ligne["url"], timeout=60)
            rep.raise_for_status()
            ratio = part_blanche(rep.content)
        except Exception as exc:                     # reseau, format, image tronquee
            echecs.append((ligne["fichier"], str(exc)[:80]))
            print("[%3d/%d] ECHEC   %s" % (i, len(lignes), ligne["fichier"]))
            continue
        blanc = ratio >= SEUIL_RATIO
        (gardes if blanc else ecartes).append((ligne, rep.content, ratio))
        print("[%3d/%d] %s %3d%%  %s" % (i, len(lignes), "BLANC  " if blanc else "autre  ",
                                          round(ratio * 100), ligne["fichier"]))

    a_archiver = gardes + ecartes if args.tout else gardes
    if not a_archiver:
        sys.exit("Aucune image a archiver.")

    with zipfile.ZipFile(args.sortie, "w", zipfile.ZIP_DEFLATED) as z:
        for ligne, contenu, ratio in a_archiver:
            dossier = "fond-blanc" if ratio >= SEUIL_RATIO else "fond-non-blanc"
            nom = "%s/%s/%s" % (dossier, ligne["produit"].replace("/", "-"), ligne["fichier"])
            z.writestr(nom, contenu)

    print("\n%d fond blanc, %d autres, %d echecs" % (len(gardes), len(ecartes), len(echecs)))
    for nom, err in echecs:
        print("  echec %s : %s" % (nom, err))
    print("Archive : %s (%.1f Mo)" % (args.sortie, os.path.getsize(args.sortie) / 1024 / 1024))

    if args.telegram:
        envoyer_telegram(args.sortie)


if __name__ == "__main__":
    main()

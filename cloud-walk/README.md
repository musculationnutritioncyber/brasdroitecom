# Cloud Walk — visuels fond blanc

Inventaire complet des visuels Cloud Walk du store Nimbao : **197 images uniques**
réparties sur **9 fiches produits** (relevé Shopify Admin API du 17 août 2026).
Les doublons inter-fiches sont éliminés, ainsi que les deux fiches dont tous les
visuels sont repris d'une autre (`cloud-walk2`, `cloud-walk2nb`).

| Fiche | Visuels |
|---|---|
| Cloud Walk | 49 |
| Cloud Walk Love | 10 |
| Cloud Walk Classic | 28 |
| Cloud Walk Multicolor | 28 |
| Cloud Walk Summer | 20 |
| Cloud Walk Sova | 18 |
| Cloud Walk Vela | 16 |
| Cloud Walk Classic (v2) | 15 |
| Cloud Walk Multicolor (v2) | 13 |

## `cloud-walk-fond-blanc.html`

Le fichier principal. À ouvrir dans un navigateur, connexion internet requise
(les images sont servies par le CDN Shopify).

Chaque image est lue sur un canvas et les pixels de son pourtour sont
échantillonnés : une image est classée **fond blanc** si au moins 92 % du
pourtour est blanc quasi neutre (`min(r,g,b) ≥ 243`, écart entre canaux ≤ 12) ou
transparent. Le fond n'est donc pas deviné d'après le nom du fichier, il est
mesuré. Si le CDN refuse la lecture cross-origin, le classement retombe sur la
convention de nommage Shopify (`_pack_` = packshot, `_life_` = lifestyle) et
l'étiquette est préfixée de `~`.

Boutons : filtrer fond blanc / fond non blanc / tout, copier les URLs affichées
(toujours en pleine résolution), exporter la liste en `.txt`. `Ctrl/Cmd+P`
produit une planche-contact PDF.

## `cloud-walk-images.csv`

Le manifeste : produit, handle, product_id, fichier, largeur, texte alternatif,
indice de nature, URL pleine résolution.

## `telecharger-fond-blanc.py`

Télécharge les 197 visuels, applique la même mesure de fond en Python (Pillow),
archive les fonds blancs en ZIP et, en option, envoie l'archive à un bot Telegram.

```bash
pip install pillow requests
python3 telecharger-fond-blanc.py                 # ZIP des fonds blancs
python3 telecharger-fond-blanc.py --tout          # + les fonds non blancs, dans un dossier séparé

export TELEGRAM_BOT_TOKEN=123456:AA...
export TELEGRAM_CHAT_ID=987654321
python3 telecharger-fond-blanc.py --telegram      # ZIP puis envoi au bot
```

Le `chat_id` s'obtient en écrivant un message au bot puis en ouvrant
`https://api.telegram.org/bot<TOKEN>/getUpdates`. Telegram plafonne l'envoi de
documents à 50 Mo ; le script s'arrête avec un message clair au-delà.

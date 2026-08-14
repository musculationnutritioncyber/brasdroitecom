# Typeform — Bras droit e-commerce (CRÉÉ)

**Form ID :** `tR1HYRlV`
**URL publique :** https://form.typeform.com/to/tR1HYRlV
**Éditeur :** https://admin.typeform.com/form/tR1HYRlV/create

Créé via l'API le 14/08/2026. 22 questions, 6 règles de logique, 9 sorties de disqualification.
Thème « Bras droit e-commerce — Violet » (`lgGynPae`), police Inter, boutons #4F46E5, accordé à la landing.
Déjà câblé dans `index.html` (variable `TYPEFORM_URL`).

---

## ✅ Déjà configuré par l'API

| Réglage | Valeur |
|---|---|
| Langue | Français |
| Thème | Violet #4F46E5 + Inter, accordé à la landing |
| Barre de progression | Proportionnelle, affichée |
| Branding Typeform | Masqué |
| Uploads publics | Non |
| Sauvegarde auto de la progression | ON |
| Réponses partielles → intégrations | ON |
| Indexation moteurs de recherche | Bloquée |
| Champs cachés | `utm_source` · `utm_medium` · `utm_campaign` · `utm_content` · `fbclid` |
| Redirection succès | `https://brasdroitecom.vercel.app/thank-you` |
| Redirection disqualification | `https://brasdroitecom.vercel.app/not-a-fit` |

## ⚠️ À faire à la main dans Typeform

- [ ] **Facebook Pixel** — Settings → Integrations → Facebook Pixel. Sur le formulaire Assistante Phuket tu utilises `1347473683378093`. À confirmer avant de le coller ici.
- [ ] **Notifications** — Settings → Notifications, vers ton email (ou brancher Google Sheets / Notion).
- [ ] **Un passage de test complet** depuis un téléphone, pour vérifier que la fin normale redirige bien vers `/thank-you`.
- [ ] **Un passage de test disqualifiant** (répondre « Non » à la question 1) → doit atterrir sur `/not-a-fit`, sans compter comme conversion.

---

## Structure du formulaire

### Écran d'accueil
> Bras droit e-commerce — marque US, plein temps, 100% remote
> *On veut vraiment te connaître, pas juste lire un CV. Compte 8 à 10 minutes, au calme. Les réponses bâclées se voient tout de suite.*

### 🚧 Filtres (questions 1 à 6) — sortie vers `/not-a-fit`

| # | Question | Disqualifie sur |
|---|---|---|
| 1 | Disponible à temps plein ? | Non |
| 2 | Niveau de français | Bon mais pas courant · Notions |
| 3 | Niveau d'anglais | Je lis mais je parle mal · Notions |
| 4 | Démarrage possible | Dans plus de 3 mois |
| 5 | Lien avec le e-commerce | Aucun lien, je découvre |
| 6 | Usage des outils IA | J'ai testé deux ou trois fois · Je n'en utilise pas |

> **Note sur la question 6 :** tu as demandé quelqu'un qui sait déjà s'en servir. Du coup « j'ai testé deux ou trois fois » disqualifie. Si tu trouves ça trop serré au vu du volume de candidatures, c'est cette règle qu'il faut assouplir en premier.

### 👤 Contact (questions 7 à 11)
Prénom · Email · WhatsApp · Ville et pays · Lien LinkedIn/portfolio (optionnel)

> Le contact est demandé **avant** les questions lourdes : avec les réponses partielles activées, quelqu'un qui abandonne à la vidéo reste joignable.

### 🎯 Fit (questions 12 à 18)
Années d'expérience · Outils maîtrisés (multi) · Outils IA utilisés (multi) ·
**Une chose concrète faite avec l'IA le mois dernier** ·
Une fois où tu as vu un problème avant les autres · Aisance face à l'inconnu (échelle 1-10) ·
Rémunération visée

> La question « raconte un projet mené du début à la fin » a été retirée : c'est la vidéo qui
> porte maintenant le parcours du candidat.

### 💬 Motivation (question 19)
Pourquoi CE poste, et pourquoi maintenant

### 🎥 Vidéo (questions 20 et 21)
Upload de fichier (**optionnel**) + lien externe (**obligatoire**, avec l'astuce « écris FAIT »).
Le candidat se présente, **raconte ce qu'il a déjà fait concrètement**, et dit pourquoi ce poste
l'intéresse. C'est la pièce qui remplace la question projet.
L'upload Typeform ne peut pas être rendu fiablement obligatoire au-delà de 10 Mo, donc c'est le
champ **lien** qui porte l'obligation. Bonus : qui n'écrit ni FAIT ni un lien valide n'a pas lu.

### 📝 Fin (question 22)
Autre chose à savoir (optionnel) → redirection `/thank-you`

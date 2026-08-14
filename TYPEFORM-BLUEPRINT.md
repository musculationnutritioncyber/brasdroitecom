# Typeform — Candidature Bras droit e-commerce

Blueprint à recopier tel quel dans Typeform. Compte ~10 min de montage.

**Ordre voulu :** on filtre AVANT de demander des efforts. Un profil hors-cible tombe sur une
fin de disqualification avant d'avoir à écrire quoi que ce soit ou à enregistrer une vidéo.
Le contact est demandé tôt (question 8-10), donc avec les **réponses partielles activées**,
quelqu'un qui abandonne à la vidéo reste joignable.

---

## ⚙️ Réglages à activer (Settings)

| Réglage | Valeur |
|---|---|
| **Partial submissions** (réponses partielles) | **ON** — capital, sinon tu perds les abandons |
| **Redirect on completion** | `https://<ton-projet>.vercel.app/thank-you` |
| Progress bar | ON |
| Question numbers | OFF (plus léger visuellement) |
| Notifications | ON vers ton email (ou intégration Google Sheets / Notion) |

## 🔒 Champs cachés (Hidden fields) — à créer avant de construire

`utm_source` · `utm_medium` · `utm_campaign` · `utm_content` · `fbclid`

La landing les lit dans l'URL de la page et les repasse automatiquement au Typeform.
Aucune manip supplémentaire de ton côté.

---

## 0. Welcome screen

```
Titre : Bras droit e-commerce — marque US, plein temps, 100% remote
Texte : On veut vraiment te connaître, pas juste lire un CV. Compte 8 à 10 minutes,
        au calme. Les réponses bâclées se voient tout de suite.
Bouton : Je commence
```

---

## 🚧 PARTIE 1 — Filtres (les 6 premières questions)

Chaque « ✕ » ci-dessous = saut logique vers l'**Ending B (disqualification)**.

```
1. [YES/NO] — requis : oui
   Q: Ce poste est à temps plein. Tu es disponible à temps plein ?
   Desc: On ne cherche pas une mission freelance à côté d'autre chose.
   Logic: Non → Ending B ✕
```

```
2. [MULTIPLE CHOICE] — requis : oui
   Q: Quel est ton niveau de français ?
   Desc: C'est ta langue de travail quotidienne avec le fondateur.
   Choices: Langue maternelle / Courant / Bon mais pas courant / Notions
   Logic: "Bon mais pas courant" → Ending B ✕
          "Notions" → Ending B ✕
```

```
3. [MULTIPLE CHOICE] — requis : oui
   Q: Et ton niveau d'anglais ?
   Desc: Une partie de l'équipe ne parle qu'anglais. Pas besoin d'être bilingue,
         mais il faut pouvoir échanger à l'écrit comme à l'oral.
   Choices: Bilingue / Courant / Conversationnel pro (je me débrouille bien) /
            Je lis mais je parle mal / Notions
   Logic: "Je lis mais je parle mal" → Ending B ✕
          "Notions" → Ending B ✕
```

```
4. [MULTIPLE CHOICE] — requis : oui
   Q: Tu pourrais démarrer quand ?
   Choices: Tout de suite / Sous 2 semaines / Sous 1 mois /
            Sous 2 à 3 mois / Dans plus de 3 mois
   Logic: "Dans plus de 3 mois" → Ending B ✕
```

```
5. [MULTIPLE CHOICE] — requis : oui
   Q: Quel est ton lien avec le e-commerce aujourd'hui ?
   Desc: Sois honnête, on préfère un débutant motivé qu'un CV gonflé.
   Choices: Je travaille (ou j'ai travaillé) dans une marque e-commerce /
            J'ai bossé en agence ou en freelance pour des marques e-commerce /
            J'ai lancé ou géré ma propre boutique /
            J'ai un side-project e-commerce sérieux /
            Je m'y intéresse beaucoup mais je n'ai jamais pratiqué /
            Aucun lien, je découvre
   Logic: "Aucun lien, je découvre" → Ending B ✕
```

```
6. [MULTIPLE CHOICE] — requis : oui
   Q: Ton rapport aux outils IA aujourd'hui ?
   Desc: On pilote une bonne partie de la boîte avec l'IA. C'est central, pas décoratif.
   Choices: J'en utilise tous les jours dans mon travail /
            J'en utilise régulièrement /
            J'ai testé, je veux vraiment aller plus loin /
            Je n'en utilise pas et ça ne m'intéresse pas
   Logic: "Je n'en utilise pas et ça ne m'intéresse pas" → Ending B ✕
```

---

## 👤 PARTIE 2 — Contact (on capture le lead ici)

```
7. [SHORT TEXT] — requis : oui
   Q: Ton prénom ?
   Desc: —
   (sert à personnaliser la suite avec @prenom)
```

```
8. [EMAIL] — requis : oui
   Q: Ton email ?
   Desc: C'est là qu'on te répond. Vérifie qu'il n'y a pas de faute.
```

```
9. [PHONE NUMBER] — requis : oui
   Q: Ton numéro WhatsApp ?
   Desc: On l'utilise seulement pour caler un échange si ton profil nous intéresse.
```

```
10. [SHORT TEXT] — requis : oui
    Q: Tu vis où en ce moment ? (ville + pays)
    Desc: On est en Asie. Ça nous sert juste à savoir sur quel fuseau on cale les calls.
```

```
11. [WEBSITE] — requis : non
    Q: Ton LinkedIn, ou un lien qui montre ce que tu as fait ?
    Desc: Portfolio, site perso, boutique que tu as lancée. Ce que tu veux.
```

---

## 🎯 PARTIE 3 — Le fit (ce qui décide vraiment)

```
12. [MULTIPLE CHOICE] — requis : oui
    Q: Combien d'années d'expérience pro as-tu au total ?
    Choices: Moins d'1 an / 1 à 3 ans / 3 à 5 ans / 5 à 10 ans / Plus de 10 ans
```

```
13. [MULTIPLE CHOICE — multi-select] — requis : oui
    Q: Sur lesquels de ces outils tu es déjà à l'aise ?
    Desc: Coche tout ce que tu as réellement utilisé. Aucun n'est obligatoire.
    Choices: Shopify / Facebook Ads Manager / Google Ads / Klaviyo ou autre outil email /
             Google Sheets niveau avancé (formules, tableaux croisés) /
             Un outil de gestion de projet (Asana, Notion, ClickUp) /
             Canva ou un outil de créa / Un outil d'analytics (GA4, Triple Whale) /
             Aucun de ceux-là
```

```
14. [MULTIPLE CHOICE — multi-select] — requis : oui
    Q: Et côté IA, tu as déjà utilisé quoi ?
    Choices: ChatGPT / Claude / Claude Code / Cursor ou un autre éditeur IA /
             Midjourney, Gemini ou un générateur d'images / Des automatisations (Make, n8n, Zapier) /
             J'ai déjà construit un agent ou un script IA moi-même / Aucun pour l'instant
```

```
15. [LONG TEXT] — requis : oui
    Q: Raconte-nous un projet que tu as mené du début à la fin, tout seul.
    Desc: Peu importe le sujet. Ce qui nous intéresse : c'était quoi, ce qui a coincé,
          et comment tu t'en es sorti. 5 à 10 lignes, pas besoin de plus.
```

```
16. [LONG TEXT] — requis : oui
    Q: Une fois où tu as vu un problème avant tout le monde. Il s'est passé quoi ?
    Desc: C'est le cœur du poste : voir venir les trucs. Un exemple concret vaut mieux
          qu'un paragraphe de théorie.
```

```
17. [OPINION SCALE 1-10] — requis : oui
    Q: Sur une échelle de 1 à 10, à quel point tu es à l'aise quand on te confie un sujet
       que tu ne maîtrises pas encore ?
    Desc: 1 = j'ai besoin d'un cadre précis · 10 = je creuse et je reviens avec une solution
```

```
18. [SHORT TEXT] — requis : oui
    Q: Quelle rémunération mensuelle nette tu vises ?
    Desc: Donne un chiffre ou une fourchette, avec la devise. Ça ne disqualifie personne,
          ça nous évite juste de se faire perdre du temps mutuellement.
```

---

## 💬 PARTIE 4 — Motivation

```
19. [LONG TEXT] — requis : oui
    Q: Pourquoi CE poste, et pourquoi maintenant ?
    Desc: On lit tout. Les réponses génériques se repèrent en trois secondes.
```

---

## 🎥 PARTIE 5 — La vidéo (le vrai filtre)

```
20. [FILE UPLOAD] — requis : NON
    Q: 🎥 Dernière étape : enregistre une courte vidéo de toi (2 à 3 minutes).
       Présente-toi, dis ce que tu as fait, et pourquoi ce poste t'intéresse.
       Tu peux l'envoyer directement ici.
    Desc: Si ta vidéo fait plus de 10 Mo, passe cette question et colle un lien
          à la question suivante.
```

```
21. [SHORT TEXT] — requis : OUI
    Q: Ou si ta vidéo est sur Google Drive, WeTransfer, YouTube ou ailleurs,
       colle simplement le lien ici.
    Desc: Assure-toi que le lien est réglé sur « Toute personne disposant du lien peut voir ».
          Tu as déjà envoyé ta vidéo à la question précédente ? Écris juste « FAIT ».
```

> **Pourquoi cette paire :** Typeform ne peut pas rendre l'upload de gros fichier fiablement
> obligatoire. On rend donc le **lien** obligatoire, et le mot « FAIT » permet à ceux qui ont
> uploadé de valider le champ. Bonus : quiconque n'écrit ni « FAIT » ni un lien valide n'a pas lu.

---

## 📝 PARTIE 6 — Fin

```
22. [LONG TEXT] — requis : non
    Q: Autre chose qu'on devrait savoir sur toi ?
    Desc: Champ libre. Ou laisse vide.
```

```
ENDING A — succès (candidature complète)
Texte : Merci @prenom, c'est bien reçu. On revient vers toi rapidement.
Action : Redirect on completion → https://<ton-projet>.vercel.app/thank-you
```

```
ENDING B — disqualification
Texte : Merci d'avoir pris le temps. Sur ce poste précis, on a des contraintes fermes
        (temps plein, français courant, anglais pro, démarrage rapide) et le fit n'y est
        pas cette fois. Rien contre ton profil, on garde ta candidature de côté si un
        autre poste s'ouvre.
Action : PAS de redirection — c'est ce qui garantit que le pixel ne compte
         que les vraies candidatures.
```

---

## ✅ Checklist avant de lancer les pubs

- [ ] Les 5 champs cachés sont créés
- [ ] Redirect on completion actif sur **Ending A uniquement**
- [ ] Partial submissions **ON**
- [ ] Testé une fois de bout en bout depuis un téléphone
- [ ] Testé un parcours disqualifiant (répondre « Non » à la Q1) → doit finir sur Ending B, sans redirection
- [ ] L'URL du formulaire est collée dans `index.html` (variable `TYPEFORM_URL`)

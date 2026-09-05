# Roadmap bras droit — ce qu'on lui donne, dans quel ordre, et pourquoi

Doc de travail Nicolas ↔ bras droit.
Chiffres tirés le 5 septembre 2026 : Shopify (90 derniers jours), Meta Ads (compte Fit005, 90 j), Klaviyo (90 j).

---

## 1. La photo du business, en vrai

| | 90 derniers jours |
|---|---|
| Commandes | 29 463 |
| Ventes brutes | 4 125 390 $ |
| **Remises** | **-1 917 428 $ (46,5 % du brut)** |
| Ventes nettes | 2 133 018 $ |
| Ventes totales | 2 408 725 $ |
| AOV | 73,27 $ |
| Sessions | 1 180 088 |
| Taux de conversion | 2,25 % |
| Nouveaux clients | 23 573 |
| Clients qui reviennent | 4 741 → **18,7 %** |
| Dépense Meta (Fit005) | 928 643 $ · ROAS in-platform 2,05 · CPM 36,97 $ · CTR 7,34 % |
| **MER** | **2,59** |
| **CAC nouveau client** | **≈ 39 $** (dépense / nouveaux clients) |

Deux lectures qui comptent :

- **Le MER (2,59) est meilleur que le ROAS Meta (2,05).** Meta sous-déclare, c'est sain. La créa n'est pas le problème le plus urgent — le CTR à 7,34 % est excellent.
- **CAC 39 $ pour un AOV de 73 $ net de remise.** Après COGS + livraison, le premier achat rapporte peu. **Tout l'argent est dans ce qui se passe après le clic** : conversion sur site, panier moyen, et rachat. C'est exactement le périmètre à donner au bras droit.

---

## 2. Où fuit l'argent — classé par montant

### Fuite n°1 — la page produit (le plus gros, de loin)

Sur 1 180 088 sessions :

| Étape | Sessions | Taux |
|---|---|---|
| Arrivée | 1 180 088 | 100 % |
| **Ajout au panier** | **51 873** | **4,4 %** |
| Checkout atteint | 49 490 | 4,2 % (95,4 % des paniers → OK) |
| **Achat** | **26 577** | **2,25 % (53,7 % des checkouts)** |

**95,6 % des visiteurs n'ajoutent jamais rien au panier.** Le passage panier → checkout est excellent (95 %). Le tunnel n'est pas cassé : c'est la **page produit** qui ne convainc pas, et le **checkout** qui perd 46 % de ceux qui l'ont commencé.

> +0,25 pt de conversion (2,25 % → 2,50 %) = **+2 950 commandes / 90 j ≈ +215 000 $**, à zéro dollar de média.
> Checkout de 53,7 % à 58 % = **+2 100 commandes ≈ +155 000 $ / 90 j**.

### Fuite n°2 — 46,5 % de remise

1,92 M$ de remise sur 90 jours. Chaque point de remise récupéré = **41 000 $ par trimestre**. Le BOGO / la 2e paire offerte marche, personne ne dit le contraire — mais personne n'a testé si elle a besoin d'être aussi agressive.

### Fuite n°3 — le rachat à 18,7 %

23 573 nouvelles clientes en 90 jours qui ne rachètent quasiment pas, sur un produit qui s'use et qui se décline (couleurs, sandales, semelles). Passer le rachat à 25 % = **+110 000 $ / 90 j**, sans un dollar de média.

### Fuite n°4 — l'attache semelles

Semelles orthopédiques + Soft Cloud : 2 087 commandes sur 29 463 = **7 % d'attache**. Sur un produit à 29 $ quasi tout en marge, pour une cliente de 60 ans qui achète des chaussures pour ses pieds. Ça devrait être 15-20 %.

> 7 % → 15 % = **+68 000 $ / 90 j en marge quasi pure**.

---

## 3. Les 10 missions à lui confier

Classées par retour sur le temps investi. Les 4 premières valent plus que tout le reste réuni.

---

### Mission 1 — Faire un audit CRO de la page produit et le tester

**Pourquoi :** c'est la fuite n°1. 95,6 % des gens partent sans rien mettre au panier.

**Ce qu'il fait :**
- Il enregistre 30 sessions mobile réelles (Hotjar / Clarity — gratuit) sur la fiche Cloud Walk. Mobile uniquement : 79 % du trafic.
- Il fait tester la fiche à 5 femmes de 55-70 ans (sa mère, sa tante, une voisine, peu importe) : *« achète-moi cette chaussure, dis tout ce que tu penses à voix haute »*. On apprend plus en 5 tests qu'en 3 mois d'analytics.
- Il liste les frictions dans l'ordre où elles bloquent : sélecteur de taille, tableau de pointures, preuve sociale au-dessus de la ligne de flottaison, délai de livraison, politique de retour, poids de la page.
- Il propose **un test par semaine, un seul changement à la fois**, sur au moins 7 jours pleins.

**Livrable :** un doc « 15 frictions classées » + un planning de tests A/B sur 8 semaines.
**KPI qu'il possède :** taux d'ajout au panier (base 4,4 %).
**Objectif 90 j :** 4,4 % → 5,5 %.

---

### Mission 2 — Réparer le checkout

**Pourquoi :** 22 913 personnes ont commencé un checkout et ne l'ont pas fini, sur 90 jours.

**Ce qu'il fait :**
- Il passe une commande lui-même, sur son téléphone, en payant vraiment. Puis il chronomètre.
- Il vérifie : les moyens de paiement (PayPal ? Apple Pay ? Shop Pay ? une femme de 65 ans veut PayPal), les frais de port affichés trop tard, les champs obligatoires inutiles, l'express checkout en haut de page.
- Il vérifie combien de commandes échouent au paiement (Shopify → commandes abandonnées, motif).
- Il teste **le prix barré et le compte à rebours** dans le checkout, pas seulement sur la fiche.

**Livrable :** rapport de test + 5 correctifs déployés.
**KPI :** checkout → achat (base 53,7 %).
**Objectif 90 j :** 58 %.

---

### Mission 3 — Reconstruire les flows Klaviyo (il en manque la moitié)

**Pourquoi :** voilà l'état réel des flows sur 90 jours.

| Flow | CA 90 j | Note |
|---|---|---|
| Welcome Series | 348 760 $ | dont **238 862 $ sur un seul SMS à 16,7 % de conversion** — à vérifier, ça sent l'attribution du code popup sur un achat qui aurait eu lieu de toute façon |
| View Product (browse abandon) | 78 100 $ | ouverture 12,8 %, **281 plaintes spam** |
| Abandoned Checkout | 25 548 $ | |
| Feedback Post-Purchase | 5 932 $ | 45 % d'ouverture, 8,4 % de clic — **l'audience la plus chaude du compte, zéro exploitée** |
| Doublons « Triple Pixel » | 10 516 $ | **deux flows dupliqués tournent en parallèle des originaux** |

**Total flows ≈ 469 000 $ sur 2,41 M$ de CA = 19 %.** Correct, mais gonflé par le Welcome, et il manque des briques entières.

**Ce qui n'existe pas et devrait exister :**

1. **Panier abandonné (Added to Cart)** — aujourd'hui il n'y a que *Checkout Started*. 51 873 sessions ont ajouté au panier, seules 49 490 ont atteint le checkout, et le flow ne touche que 15 989 destinataires. Il manque un flow entre les deux.
2. **Retour en stock** — la metric `Subscribed to Back in Stock` existe dans Klaviyo, **et aucun flow ne l'écoute**. Des gens lèvent la main pour acheter et personne ne les rappelle. À faire cette semaine.
3. **Winback 60 / 90 / 180 jours** — inexistant. 23 573 nouvelles clientes par trimestre qui ne reçoivent jamais rien.
4. **2e paire / réachat** — inexistant. C'est le flow qui porte l'objectif de rachat.
5. **VIP (2 commandes et +)** — inexistant. 4 741 clientes fidèles traitées comme tout le monde.
6. **Sunset / hygiène de liste** — inexistant, et c'est urgent (voir mission 4).
7. **Post-livraison → avis + photo** — le flow Feedback existe mais ne demande ni avis ni photo. Il devrait alimenter la banque d'UGC.

**Et à nettoyer tout de suite :** les deux flows « - Triple Pixel » dupliqués. Ils tournent **en même temps** que les originaux. Double envoi vers les mêmes gens, attribution polluée. Il en garde un des deux, il archive l'autre.

**Livrable :** 6 flows construits et live, 2 doublons archivés.
**KPI :** part du CA venant des flows (base 19 %).
**Objectif 90 j :** 28 %, avec le Welcome retiré du calcul pour ne pas se mentir.

---

### Mission 4 — Sauver la délivrabilité (avant que ça coûte cher)

**Pourquoi :** le flow *View Product* a **281 plaintes spam** sur 90 jours, soit 0,09 %. Le seuil de tolérance de Google et Microsoft est de 0,03 %. On est à 3× au-dessus. Et l'ouverture y est à 12,8 % — c'est le signal que les boîtes mail commencent déjà à trier.

En face, les campagnes ouvrent à 25-45 %. Autrement dit : **un flow qui envoie 329 350 messages est en train d'abîmer la réputation d'expédition de tout le compte**, campagnes comprises.

**Ce qu'il fait :**
- Il limite *View Product* aux profils engagés dans les 60 derniers jours (ça va diviser le volume par 3 et remonter l'ouverture).
- Il crée un flow sunset : pas d'ouverture depuis 120 jours → une dernière relance → désabonnement automatique.
- Il segmente toutes les campagnes sur « engagé 90 jours », sauf les 2 gros temps forts de l'année.
- Il surveille chaque semaine : taux de plainte, taux d'ouverture, taux de rebond.

**KPI :** taux de plainte spam **sous 0,03 %** sur tous les flows. Non négociable, c'est un risque existentiel pour le canal.

---

### Mission 5 — Monter l'AOV : semelles, bundles, post-achat

**Pourquoi :** 7 % d'attache sur les semelles. AOV 73 $ pour un CAC de 39 $.

**Ce qu'il fait :**
- Semelles en **bump offer sur la fiche produit** (case à cocher « ajouter les semelles orthopédiques -40 % », pas une page séparée).
- Semelles en **upsell post-achat** (après le paiement, en un clic — aucun frein, aucune re-saisie de carte). C'est le levier le plus rentable du e-commerce et il n'est pas branché.
- Un **bundle « paire + semelles + chaussettes »** à prix de pack.
- Test d'un **palier de livraison gratuite** juste au-dessus de l'AOV actuel (ex. 89 $).

**KPI :** AOV (base 73,27 $) et taux d'attache semelles (base 7 %).
**Objectif 90 j :** AOV 82 $, attache 15 %.

---

### Mission 6 — Ouvrir le SMS pour de vrai

**Pourquoi :** 3 campagnes SMS en 90 jours contre ~30 emails. Et le SMS du Welcome sort à **14,56 $ de CA par destinataire** — le meilleur chiffre du compte, tous canaux confondus.

**Attention quand même :** le SMS de panier abandonné désabonne à 3,8-5,8 %, ce qui est très élevé. Le canal marche, mais il est mal écrit ou trop fréquent.

**Ce qu'il fait :**
- 1 SMS par semaine, segmenté engagés.
- Il réécrit les SMS des flows (les taux de désabonnement actuels sont un signal de rejet).
- Il installe un **flow SMS panier abandonné** distinct de l'email, à 30 minutes.
- Il fait grossir la liste SMS : opt-in téléphone dans la popup, en deuxième étape (jamais en première, ça tue le taux d'inscription email).

**KPI :** CA SMS / mois, taux de désabonnement SMS sous 2 %.

---

### Mission 7 — Ouvrir Google Ads

**Pourquoi :** sur 90 jours, **1 920 commandes et 165 149 $ sont arrivés par Google sans qu'on dépense un dollar dessus.** Plus 10 062 commandes en « direct » — c'est-à-dire, en bonne partie, des gens qui ont vu une pub Facebook puis ont tapé la marque dans Google.

Aujourd'hui, **100 % du média est sur Meta.** C'est un risque de concentration et un manque à gagner.

**Ce qu'il fait, dans cet ordre :**
1. **Search de marque** en premier (petit budget, ROAS énorme, protège contre les concurrents qui enchérissent sur le nom).
2. **Shopping / PMax** avec le flux produit propre.
3. Il lit le rapport de termes de recherche toutes les semaines.

**KPI :** ROAS Google, part du CA hors Meta (base ~48 % du CA hors « facebook »).
**Objectif 90 j :** un canal Google rentable et scalable.

---

### Mission 8 — Industrialiser la voix client et l'UGC

**Pourquoi :** le flow post-achat touche 37 605 personnes avec 45 % d'ouverture et 8,4 % de clic. C'est une mine, et elle sert à rien aujourd'hui.

**Ce qu'il fait :**
- Il ajoute une demande d'**avis + photo** au post-achat, avec une contrepartie (bon d'achat, tirage au sort).
- Il transforme les meilleurs verbatims en angles de statiques et de scripts vidéo — **c'est le pont direct avec la team créa qu'il est en train de recruter.**
- Il fait tourner un **sondage post-achat** (« qu'est-ce qui vous a presque fait renoncer ? ») : les réponses vont directement nourrir la mission 1.
- Il tient une banque UGC organisée que les créatifs piochent en libre-service.

**KPI :** nombre de photos clientes exploitables par mois, nombre d'avis collectés.

---

### Mission 9 — Tester la profondeur de remise

**Pourquoi :** 46,5 % de remise. 3 points récupérés = 124 000 $ par trimestre.

**Ce qu'il fait :** un test propre, une variante à la fois, sur 2 semaines pleines, sur une seule ligne (les sandales par exemple, pas le produit principal), en surveillant **le CA total, pas le taux de conversion**. Une baisse du taux de conversion compensée par une meilleure marge est une victoire.

**À cadrer avec toi avant de lancer** — c'est du prix, ça touche à l'offre.

---

### Mission 10 — Le cockpit hebdo

**Pourquoi :** aujourd'hui il n'y a pas un endroit unique où on voit si la semaine a été bonne.

**Ce qu'il fait :** un tableau, un seul, mis à jour tous les lundis matin avant votre point, avec **8 chiffres et rien d'autre** :

1. CA / dépense média / **MER**
2. Commandes et **AOV**
3. **Taux de conversion**, et **taux d'ajout au panier** à côté
4. CAC nouveau client
5. Taux de remise (% du brut)
6. % du CA venant de l'email + SMS
7. Taux de rachat
8. Ruptures de stock à venir sous 30 jours

Avec la variation vs semaine précédente et **une phrase par chiffre qui bouge de plus de 10 %**. Pas un dashboard de 40 tuiles que personne ne lit.

---

## 4. Ce qu'on ne lui donne PAS tout de suite

- **Le budget média Meta.** Il regarde, il analyse, il propose. La main sur les budgets vient au bout de 90 jours, quand tu as vu son jugement à l'œuvre.
- **Le prix et l'offre.** Il propose des tests, tu valides. C'est le cœur du business.
- **Les fournisseurs et les négos.** Plus tard.
- **Le recrutement de la team créa** — sauf que là, il est déjà dessus, donc : cadre-le avec un budget plafond et un nombre de personnes maximum, sinon ça dérive.

Le principe : **il possède le site, le CRM et la donnée. Toi tu gardes l'offre, le prix et le budget média** jusqu'à ce que la confiance soit faite sur du concret.

---

## 5. Le rituel

**Lundi, 45 minutes, ordre du jour fixe :**
1. Le cockpit (10 min) — les 8 chiffres, ce qui bouge
2. Les tests en cours (10 min) — un test = un résultat = une décision garder / jeter
3. Les créas de la semaine (10 min) — briefs, feedbacks, ce qui part en prod
4. La semaine à venir (10 min) — promos, emails, lancements
5. Les blocages (5 min) — ce sur quoi il a besoin de toi, et rien d'autre

**Vendredi :** un message écrit de 10 lignes. Ce qui a été fait, ce qui a bougé, ce qui coince. Pas de réunion.

**Règle qui change tout :** un test A/B par semaine, un seul, 7 jours pleins minimum, résultat écrit et archivé. Au bout d'un an ça fait 50 apprentissages qui appartiennent à la boîte et pas à une personne.

---

## 6. Les 90 premiers jours

**Jours 1-30 — il nettoie et il comprend**
- Il archive les 2 flows Triple Pixel dupliqués
- Il branche le flow retour en stock (la metric existe déjà, il n'y a qu'à l'écouter)
- Il segmente View Product sur les engagés → il fait tomber le taux de plainte
- Il passe une commande réelle, il enregistre 30 sessions mobile, il fait tester la fiche à 5 vraies femmes
- Il monte le cockpit hebdo
- **Résultat attendu :** taux de plainte sous 0,03 %, cockpit qui tourne, liste de frictions écrite

**Jours 31-60 — il construit**
- Panier abandonné, winback, 2e paire, VIP, sunset
- Bump offer semelles + upsell post-achat
- Premier test CRO sur la fiche produit
- Search de marque Google ouvert
- **Résultat attendu :** ajout au panier 4,4 % → 5 %, attache semelles 7 % → 12 %

**Jours 61-90 — il pousse**
- SMS hebdo qui tourne
- Réparation du checkout déployée
- Test de profondeur de remise sur une ligne
- Machine à UGC branchée sur la team créa
- **Résultat attendu :** conversion 2,25 % → 2,45 %, AOV 73 $ → 80 $, rachat 18,7 % → 22 %

---

## 7. Le calcul qui justifie tout

Si les 4 premières missions atteignent leur cible, sur un trimestre :

| Levier | Impact / 90 j |
|---|---|
| Conversion 2,25 % → 2,50 % | +215 000 $ |
| Checkout 53,7 % → 58 % | +155 000 $ |
| AOV 73 $ → 82 $ | +265 000 $ |
| Rachat 18,7 % → 25 % | +110 000 $ |
| 3 pts de remise récupérés | +124 000 $ |
| **Total** | **≈ +870 000 $ par trimestre** |

**Sans augmenter d'un dollar le budget média.** C'est ça qu'il faut lui mettre sous les yeux le premier jour : son poste ne se paie pas, il se rembourse vingt fois.

---

## Deux réserves d'honnêteté

1. **Les 238 862 $ du SMS de bienvenue.** Un taux de conversion de 16,7 % sur un flow de bienvenue, c'est anormalement haut. C'est presque certainement le code promo de la popup attribué à un achat qui allait se faire de toute façon. **À vérifier avant de bâtir quoi que ce soit dessus** — sinon on croit que l'email pèse 19 % du CA alors qu'il en pèse peut-être 12 % en incrémental.

2. **La dépense média ne couvre que le compte Fit005.** S'il y a du budget sur d'autres comptes, le MER et le CAC réels sont moins bons que ceux affichés ici. À recaler avant de fixer les objectifs.

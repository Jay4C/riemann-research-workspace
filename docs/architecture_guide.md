---
title: "Guide d’architecture du Riemann Research Workspace"
subtitle: "Infrastructure reproductible pour l’étude de l’hypothèse de Riemann"
author: "Jason ALOYAU"
date: "2026"
lang: "fr-FR"
documentclass: article
papersize: a4
fontsize: 11pt
geometry:
  - margin=2.5cm
colorlinks: true
toc: true
toc-depth: 3
numbersections: true
---

# Introduction

Le **Riemann Research Workspace** est une infrastructure de recherche destinée à organiser des travaux mathématiques et numériques autour de l’hypothèse de Riemann.

Le projet combine :

- la rédaction mathématique en LaTeX ;
- la documentation scientifique en Markdown ;
- l’expérimentation numérique en Python ;
- le suivi explicite des hypothèses et obligations de preuve ;
- la préparation à la vérification formelle ;
- la production de documents PDF ;
- les tests automatiques et l’intégration continue ;
- la revue contradictoire des résultats.

> **Avertissement scientifique**
>
> Ce dépôt ne constitue pas une démonstration de l’hypothèse de Riemann.
> Son rôle est de fournir une méthode rigoureuse pour développer, vérifier,
> documenter et réfuter des propositions mathématiques associées au problème.

# Objectif scientifique

L’hypothèse de Riemann concerne les zéros non triviaux de la fonction zêta de Riemann.

Pour tout nombre complexe \(s\) tel que \(\Re(s)>1\), la fonction zêta est définie par :

\[
\zeta(s)=\sum_{n=1}^{\infty}\frac{1}{n^s}.
\]

Elle admet un prolongement méromorphe au plan complexe, avec un pôle simple en \(s=1\).

L’hypothèse de Riemann affirme que :

\[
\zeta(\rho)=0
\quad\text{et}\quad
0<\Re(\rho)<1
\quad\Longrightarrow\quad
\Re(\rho)=\frac{1}{2}.
\]

La droite

\[
\Re(s)=\frac{1}{2}
\]

est appelée **droite critique**.

La région

\[
0<\Re(s)<1
\]

est appelée **bande critique**.

# Principes d’architecture

L’architecture du dépôt repose sur plusieurs principes obligatoires.

## Séparation des responsabilités

Chaque catégorie de contenu possède un emplacement spécifique :

- les définitions et cartes de connaissances sont placées dans `docs/` ;
- le manuscrit scientifique est placé dans `paper/` ;
- les fonctions numériques réutilisables sont placées dans `src/` ;
- les tests automatiques sont placés dans `tests/` ;
- les expériences reproductibles sont placées dans `experiments/` ;
- les affirmations mathématiques sont enregistrées dans `claims/` ;
- les revues contradictoires sont enregistrées dans `reviews/` ;
- les travaux de formalisation sont placés dans `formal/` ;
- les données sont placées dans `data/` ;
- les outils d’automatisation sont placés dans `scripts/`.

## Reproductibilité

Tout résultat numérique doit indiquer au minimum :

- le script utilisé ;
- les paramètres d’entrée ;
- la précision numérique ;
- les dépendances logicielles ;
- la version de Python ;
- la date d’exécution ;
- les données sources ;
- les critères d’arrêt ;
- les erreurs numériques estimées ;
- l’identifiant de l’expérience.

## Traçabilité

Toute affirmation nouvelle doit posséder un identifiant unique.

Exemples :

```text
HYP-0001
LEM-0001
THM-0001
EXP-0001
REV-0001
DATA-0001
```

Chaque résultat doit pouvoir être relié :

1. à son énoncé mathématique ;
2. à ses dépendances ;
3. à sa démonstration ou tentative de démonstration ;
4. à ses expériences numériques ;
5. à sa revue contradictoire ;
6. à son statut actuel.

## Falsifiabilité

Une proposition ne doit pas uniquement être accompagnée d’arguments favorables.

Elle doit également préciser :

- les cas limites ;
- les contre-exemples recherchés ;
- les hypothèses susceptibles d’être trop fortes ;
- les erreurs possibles ;
- les singularités ;
- les défauts potentiels d’uniformité ;
- les dépendances pouvant introduire une circularité.

## Distinction entre calcul et démonstration

Une vérification numérique, même effectuée sur un très grand nombre de zéros, reste un résultat fini.

Elle ne démontre pas une propriété portant sur une infinité de zéros.

Les résultats du dépôt doivent donc être classés comme :

- théorème démontré ;
- lemme démontré ;
- résultat conditionnel ;
- conjecture ;
- hypothèse de travail ;
- observation numérique ;
- heuristique ;
- résultat réfuté ;
- expérience non concluante.

# Structure générale du dépôt

```text
riemann-research-workspace/
├── README.md
├── GOVERNANCE.md
├── LICENSE
├── Makefile
├── pyproject.toml
├── .gitignore
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── docs/
│   ├── 00_problem_statement.md
│   ├── 01_knowledge_map.md
│   ├── 02_research_program.md
│   ├── 03_proof_obligations.md
│   ├── 04_publication_and_awards.md
│   ├── 05_peer_review_checklist.md
│   ├── architecture_guide.md
│   └── architecture_guide.pdf
│
├── paper/
│   ├── main.tex
│   ├── references.bib
│   └── sections/
│       ├── 01_statement.tex
│       ├── 02_known_results.tex
│       ├── 03_candidate_strategy.tex
│       ├── 04_lemmas.tex
│       ├── 05_failure_analysis.tex
│       ├── 06_computational_evidence.tex
│       └── 07_conclusion.tex
│
├── src/
│   └── riemann_lab/
│       ├── __init__.py
│       ├── zeta.py
│       └── zeros.py
│
├── tests/
│   ├── test_zeta.py
│   └── test_zeros.py
│
├── experiments/
│   ├── registry.csv
│   └── 001_zeta_sanity/
│       ├── README.md
│       └── run.py
│
├── claims/
│   └── claims.yaml
│
├── reviews/
│   └── REVIEW_TEMPLATE.md
│
├── formal/
│   └── README.md
│
├── data/
│   └── README.md
│
└── scripts/
    └── check_claim_language.py
```

# Description des fichiers racine

## `README.md`

Le fichier principal du dépôt présente :

- l’objectif scientifique ;
- le statut du projet ;
- les avertissements méthodologiques ;
- les prérequis ;
- les commandes d’installation ;
- les commandes de test ;
- les modalités de contribution ;
- les liens vers la documentation détaillée.

Il doit préciser explicitement que le dépôt ne revendique pas de résolution de l’hypothèse de Riemann.

## `GOVERNANCE.md`

Ce fichier définit les règles de gouvernance scientifique.

Il précise notamment :

- les règles de contribution ;
- les conventions de nommage ;
- les conditions de validation d’une affirmation ;
- les responsabilités des relecteurs ;
- les règles de publication ;
- les règles relatives aux résultats négatifs ;
- la procédure de gestion des désaccords mathématiques.

## `LICENSE`

Ce fichier définit les conditions juridiques de réutilisation du code et du contenu.

Les licences du code, des textes, des données et des documents externes peuvent être différentes. Chaque élément importé doit conserver ses propres mentions d’attribution.

## `Makefile`

Le `Makefile` centralise les principales commandes du projet.

Exemples de cibles :

```makefile
test:
	python -m pytest -q

experiment:
	python experiments/001_zeta_sanity/run.py

paper:
	latexmk -pdf -interaction=nonstopmode paper/main.tex

architecture:
	pandoc docs/architecture_guide.md \
		-o docs/architecture_guide.pdf \
		--pdf-engine=xelatex \
		--toc \
		--number-sections

clean:
	rm -rf build .pytest_cache
	rm -f paper/*.aux paper/*.log paper/*.out paper/*.toc
```

## `pyproject.toml`

Ce fichier décrit le projet Python.

Il contient :

- le nom du paquet ;
- sa version ;
- la version minimale de Python ;
- les dépendances ;
- les dépendances de développement ;
- la configuration de `pytest` ;
- la configuration éventuelle des outils de qualité.

## `.gitignore`

Ce fichier exclut du dépôt les éléments qui ne doivent pas être versionnés.

Exemples :

```gitignore
.venv/
__pycache__/
*.pyc
.pytest_cache/
build/
dist/
*.aux
*.log
*.out
*.toc
```

## `.github/workflows/ci.yml`

Ce fichier décrit le pipeline d’intégration continue.

Le pipeline peut notamment :

1. récupérer le dépôt ;
2. installer Python ;
3. installer les dépendances ;
4. exécuter les tests ;
5. contrôler le format du code ;
6. vérifier la compilation du manuscrit ;
7. publier les rapports de test.

# Dossier `docs/`

Le dossier `docs/` contient la documentation conceptuelle et méthodologique du projet.

## `00_problem_statement.md`

Ce document contient l’énoncé contrôlé du problème.

Il doit distinguer :

- la définition initiale de \(\zeta(s)\) ;
- son prolongement analytique ;
- les zéros triviaux ;
- les zéros non triviaux ;
- la bande critique ;
- la droite critique ;
- l’énoncé exact de l’hypothèse de Riemann.

Aucune approximation informelle ne doit remplacer l’énoncé mathématique.

## `01_knowledge_map.md`

Ce document organise les connaissances nécessaires.

Domaines concernés :

- analyse complexe ;
- théorie analytique des nombres ;
- fonctions arithmétiques ;
- théorie spectrale ;
- matrices aléatoires ;
- fonctions \(L\) ;
- calcul numérique ;
- arithmétique d’intervalles ;
- vérification formelle.

Ce fichier doit également identifier les relations entre les domaines.

## `02_research_program.md`

Ce document définit les axes de recherche.

Chaque axe doit préciser :

- la question étudiée ;
- les résultats connus ;
- le verrou principal ;
- les hypothèses nouvelles ;
- les expériences possibles ;
- les critères d’échec ;
- les livrables attendus.

## `03_proof_obligations.md`

Ce fichier constitue le registre des obligations de preuve.

Une obligation doit au minimum comporter :

```yaml
id: PO-0001
statement: "Énoncé mathématique exact"
status: OPEN
dependencies:
  - LEM-0001
assumptions:
  - "Hypothèse explicite"
verification:
  analytic: false
  numerical: false
  formal: false
reviewer: null
```

Statuts autorisés :

```text
OPEN
PARTIAL
PROVED
REFUTED
BLOCKED
```

## `04_publication_and_awards.md`

Ce document décrit la stratégie de publication et présente séparément les distinctions scientifiques.

Le processus de publication doit privilégier :

1. la correction mathématique ;
2. la revue indépendante ;
3. la reproductibilité ;
4. la transparence des limites ;
5. la publication spécialisée ;
6. l’acceptation par la communauté scientifique.

La recherche ne doit pas être organisée autour de la promesse d’une récompense. Une distinction ne peut jamais être considérée comme automatique.

## `05_peer_review_checklist.md`

Ce fichier contient la checklist de revue.

La revue doit notamment contrôler :

- la précision des définitions ;
- la cohérence des notations ;
- la direction des implications ;
- les hypothèses cachées ;
- les singularités ;
- les échanges de limites ;
- la convergence uniforme ;
- les termes de bord ;
- les erreurs numériques ;
- les références bibliographiques ;
- les risques de circularité.

## `architecture_guide.md`

Il s’agit du présent document.

Il constitue la source éditable du guide d’architecture.

## `architecture_guide.pdf`

Ce fichier est la version PDF générée à partir de `architecture_guide.md`.

Il ne doit pas être modifié manuellement. Toute modification doit être effectuée dans la source Markdown, puis compilée.

# Dossier `paper/`

Le dossier `paper/` contient le manuscrit scientifique principal.

## `main.tex`

Le fichier principal :

- charge les paquets LaTeX ;
- définit les environnements mathématiques ;
- fixe les métadonnées ;
- importe les différentes sections ;
- génère la table des matières ;
- charge la bibliographie.

Exemple d’organisation :

```latex
\input{sections/01_statement}
\input{sections/02_known_results}
\input{sections/03_candidate_strategy}
\input{sections/04_lemmas}
\input{sections/05_failure_analysis}
\input{sections/06_computational_evidence}
\input{sections/07_conclusion}
```

## `references.bib`

La bibliographie doit contenir des références vérifiables.

Chaque référence doit être utilisée dans le manuscrit et, lorsque cela est possible, comporter :

- l’auteur ;
- le titre ;
- l’année ;
- la revue ou l’éditeur ;
- le volume ;
- les pages ;
- le DOI ;
- l’identifiant arXiv ;
- une URL institutionnelle.

## `sections/01_statement.tex`

Cette section fixe l’énoncé exact et les notations.

## `sections/02_known_results.tex`

Cette section présente uniquement les résultats déjà établis.

Chaque théorème externe doit être accompagné d’une référence précise.

## `sections/03_candidate_strategy.tex`

Cette section décrit la stratégie candidate.

Elle doit identifier :

- le point de départ ;
- les transformations ;
- la propriété intermédiaire ;
- la relation exacte avec RH ;
- le premier lemme réellement nouveau ;
- le principal obstacle.

## `sections/04_lemmas.tex`

Cette section contient les lemmes.

Chaque lemme doit préciser :

- ses hypothèses ;
- son domaine de validité ;
- ses dépendances ;
- sa conclusion exacte ;
- sa preuve ;
- les étapes nécessitant une revue indépendante.

## `sections/05_failure_analysis.tex`

Cette section étudie les faiblesses de l’approche.

Elle doit rechercher activement :

- les raisonnements circulaires ;
- les divergences cachées ;
- les singularités non traitées ;
- les changements de domaine ;
- les échanges injustifiés ;
- les estimations non uniformes ;
- les arguments uniquement numériques.

## `sections/06_computational_evidence.tex`

Cette section présente les résultats numériques.

Chaque résultat doit indiquer :

- l’identifiant de l’expérience ;
- le script utilisé ;
- la précision ;
- la méthode ;
- les données ;
- les erreurs ;
- la portée exacte de l’observation.

## `sections/07_conclusion.tex`

La conclusion doit séparer explicitement :

- ce qui est démontré ;
- ce qui est observé ;
- ce qui reste conjectural ;
- ce qui a été réfuté ;
- ce qui reste ouvert.

# Dossier `src/`

Le dossier `src/riemann_lab/` contient le code Python réutilisable.

## `__init__.py`

Ce fichier identifie le dossier comme paquet Python et peut exposer la version du projet.

```python
__version__ = "0.1.0"
```

## `zeta.py`

Ce module contient les fonctions relatives à la fonction zêta.

Responsabilités possibles :

- évaluation de \(\zeta(s)\) ;
- calcul sur la droite critique ;
- test numérique de l’équation fonctionnelle ;
- gestion de la précision ;
- validation des paramètres.

Le module doit préciser que les calculs exploratoires ne constituent pas automatiquement des calculs certifiés.

## `zeros.py`

Ce module contient les fonctions relatives aux zéros.

Responsabilités possibles :

- chargement de tables de zéros ;
- calcul exploratoire de zéros ;
- comparaison avec des valeurs de référence ;
- contrôle de la partie réelle ;
- export des résultats.

# Dossier `tests/`

Le dossier `tests/` contient les tests automatisés.

## `test_zeta.py`

Ce fichier vérifie notamment :

\[
\zeta(2)=\frac{\pi^2}{6}.
\]

Il peut également tester l’équation fonctionnelle en des points ne correspondant ni à un pôle ni à une singularité de la représentation utilisée.

## `test_zeros.py`

Ce fichier contrôle les fonctions de calcul ou de chargement des zéros.

Les tests numériques doivent utiliser une tolérance adaptée à la précision réellement demandée.

# Dossier `experiments/`

Le dossier `experiments/` contient les expériences indépendantes.

## `registry.csv`

Le registre permet de suivre les expériences.

Structure recommandée :

```csv
id,title,status,claim,script,input,output,precision
EXP-001,Zeta sanity checks,READY,,001_zeta_sanity/run.py,,001_zeta_sanity/results.json,80
```

## `001_zeta_sanity/`

Cette première expérience vérifie que l’environnement numérique fonctionne correctement.

Elle peut :

- calculer quelques zéros connus ;
- mesurer le résidu de l’équation fonctionnelle ;
- enregistrer la précision ;
- exporter les résultats dans un fichier structuré.

Cette expérience ne doit comporter aucune revendication concernant une démonstration générale de RH.

# Dossier `claims/`

Le fichier `claims/claims.yaml` constitue le registre central des affirmations.

Exemple :

```yaml
claims:
  - id: HYP-0001
    title: "Propriété intermédiaire candidate"
    statement: >
      Énoncé mathématique complet de la propriété.
    status: OPEN
    implies_rh: unknown
    implied_by_rh: unknown
    dependencies: []
    experiments: []
    reviews: []
    formalization: null
    notes: >
      Aucun résultat démontré à ce stade.
```

Une affirmation ne doit jamais recevoir le statut `PROVED` sur la seule base de calculs numériques.

# Dossier `reviews/`

Le dossier `reviews/` contient les revues critiques.

Chaque revue doit utiliser un modèle commun :

```markdown
# Revue de CLAIM-ID

## Énoncé examiné

## Résumé de l’argument

## Première étape non standard

## Vérification des dépendances

## Hypothèses cachées possibles

## Recherche de circularité

## Tentatives de contre-exemple

## Contrôle des calculs

## Points bloquants

## Verdict
```

Les verdicts possibles sont :

```text
OPEN
PARTIAL
PROVED
REFUTED
BLOCKED
```

# Dossier `formal/`

Ce dossier prépare la vérification formelle.

La formalisation doit être progressive :

1. définir les objets utilisés ;
2. formaliser les résultats élémentaires ;
3. formaliser les lemmes locaux ;
4. vérifier les dépendances ;
5. relier les lemmes ;
6. comparer l’énoncé formalisé avec l’énoncé mathématique du manuscrit.

La présence d’un squelette de formalisation ne signifie pas qu’une démonstration a été formellement vérifiée.

# Dossier `data/`

Le dossier `data/` contient les données du projet.

Les données peuvent être organisées en sous-dossiers :

```text
data/
├── raw/
├── processed/
├── generated/
├── reference/
├── external/
├── benchmarks/
└── metadata/
```

Chaque jeu de données doit indiquer :

- son origine ;
- sa licence ;
- sa date d’obtention ;
- sa méthode de génération ;
- sa précision ;
- sa somme de contrôle ;
- les transformations appliquées.

Les données brutes ne doivent pas être modifiées directement.

# Dossier `scripts/`

Le dossier `scripts/` contient les outils d’automatisation.

## `check_claim_language.py`

Ce script peut rechercher des formulations excessives ou ambiguës.

Il peut notamment signaler :

- « preuve de RH » ;
- « résolution définitive » ;
- « démonstration complète » ;
- « tous les zéros ont été vérifiés » ;
- « résultat certain » sans statut associé.

Le script constitue une aide éditoriale. Il ne remplace pas la revue mathématique.

# Workflow scientifique

Le cycle normal d’une proposition est le suivant :

```text
Idée
  ↓
Affirmation formalisée
  ↓
Enregistrement dans claims.yaml
  ↓
Identification des dépendances
  ↓
Décomposition en obligations de preuve
  ↓
Tentative analytique
  ↓
Recherche de contre-exemples
  ↓
Expérience numérique
  ↓
Analyse des erreurs
  ↓
Revue contradictoire
  ↓
Formalisation éventuelle
  ↓
Rédaction LaTeX
  ↓
Relecture indépendante
  ↓
Publication éventuelle
```

# Cycle de vie d’une affirmation

## Étape 1 : création

L’affirmation reçoit un identifiant et le statut `OPEN`.

## Étape 2 : décomposition

L’affirmation est séparée en lemmes plus petits.

## Étape 3 : vérification des dépendances

Chaque résultat externe est cité précisément.

## Étape 4 : expérimentation

Des expériences peuvent être utilisées pour :

- détecter un contre-exemple ;
- comparer des formulations ;
- mesurer un comportement ;
- identifier une erreur ;
- orienter la recherche.

## Étape 5 : démonstration

Une démonstration doit être indépendante de l’évidence numérique lorsque l’énoncé est universel.

## Étape 6 : revue

Un relecteur tente activement d’invalider l’argument.

## Étape 7 : changement de statut

Le statut n’est modifié qu’après justification.

# Contrôles mathématiques essentiels

Avant de considérer un argument comme complet, vérifier les points suivants.

## Convergence

- La série converge-t-elle ?
- La convergence est-elle absolue ?
- La convergence est-elle uniforme ?
- Sur quel domaine ?
- Les paramètres sont-ils contrôlés ?

## Échanges d’opérations

Chaque échange doit être justifié :

\[
\lim \sum \leftrightarrow \sum \lim,
\]

\[
\int \sum \leftrightarrow \sum \int,
\]

\[
\frac{d}{ds}\int \leftrightarrow \int\frac{d}{ds},
\]

\[
\lim \int \leftrightarrow \int \lim.
\]

## Analyticité

- La fonction est-elle holomorphe sur le domaine utilisé ?
- Le prolongement analytique est-il applicable ?
- Les pôles ont-ils été exclus ?
- Les coupures et branches sont-elles spécifiées ?

## Estimations

- La constante implicite dépend-elle d’un paramètre ?
- L’estimation est-elle uniforme ?
- Le terme d’erreur est-il suffisamment contrôlé ?
- Le passage à l’infini est-il valide ?

## Implications

Pour une équivalence

\[
\mathrm{RH}\Longleftrightarrow P,
\]

il faut démontrer séparément :

\[
\mathrm{RH}\Longrightarrow P
\]

et

\[
P\Longrightarrow\mathrm{RH}.
\]

Démontrer une seule direction ne suffit pas.

# Contrôles numériques essentiels

Toute expérience doit indiquer :

```yaml
experiment:
  id: EXP-0001
  python: "3.11"
  library: "mpmath"
  precision_digits: 100
  tolerance: "1e-90"
  seed: null
  input_dataset: null
  output_file: "results.json"
```

Lorsque le résultat doit être rigoureux, l’arithmétique flottante ordinaire peut être insuffisante.

Il faut alors envisager :

- l’arithmétique d’intervalles ;
- les bornes d’erreur explicites ;
- la reproduction indépendante ;
- des méthodes de certification ;
- la vérification des bibliothèques utilisées.

# Installation de l’environnement

## Création de l’environnement virtuel

Sous Windows PowerShell :

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Sous Windows `cmd.exe` :

```bat
python -m venv .venv
.venv\Scripts\activate.bat
```

Sous Linux ou macOS :

```bash
python -m venv .venv
source .venv/bin/activate
```

## Installation du projet

```bash
python -m pip install --upgrade pip
pip install -e ".[dev]"
```

## Exécution des tests

```bash
pytest -q
```

## Exécution de l’expérience initiale

```bash
python experiments/001_zeta_sanity/run.py
```

# Génération du PDF

## Prérequis possibles

La conversion peut être effectuée avec :

- Pandoc ;
- XeLaTeX ;
- une distribution LaTeX compatible.

## Commande Pandoc recommandée

Depuis la racine du dépôt :

```bash
pandoc docs/architecture_guide.md \
  --from markdown \
  --to pdf \
  --output docs/architecture_guide.pdf \
  --pdf-engine=xelatex \
  --toc \
  --number-sections
```

Sous PowerShell, la commande peut être écrite ainsi :

```powershell
pandoc docs/architecture_guide.md `
  --from markdown `
  --to pdf `
  --output docs/architecture_guide.pdf `
  --pdf-engine=xelatex `
  --toc `
  --number-sections
```

## Génération avec une police personnalisée

```bash
pandoc docs/architecture_guide.md \
  --output docs/architecture_guide.pdf \
  --pdf-engine=xelatex \
  --variable mainfont="DejaVu Sans" \
  --variable monofont="DejaVu Sans Mono" \
  --toc \
  --number-sections
```

## Contrôle du document généré

Après génération, vérifier :

- la présence de toutes les pages ;
- la table des matières ;
- les équations ;
- les blocs de code ;
- les caractères accentués ;
- les sauts de page ;
- les dépassements de marge ;
- les liens ;
- l’absence de symboles manquants.

# Stratégie Git

## Création d’une branche

```bash
git checkout -b docs/architecture-guide
```

## Ajout des fichiers

```bash
git add docs/architecture_guide.md
git add docs/architecture_guide.pdf
```

## Commit

```bash
git commit -m "docs: add research architecture guide"
```

## Publication

```bash
git push -u origin docs/architecture-guide
```

# Conventions de commit

Exemples :

```text
docs: clarify Riemann hypothesis statement
feat: add zeta functional equation checks
test: add reference zero validation
experiment: add Jensen polynomial exploration
fix: correct precision handling
refactor: separate zero loading and computation
review: document counterexample analysis
formal: add initial zeta definitions
data: add dataset provenance metadata
```

# Critères de maturité

## Niveau 0 : structure

- [ ] Arborescence créée.
- [ ] Documentation initiale présente.
- [ ] Environnement Python défini.
- [ ] Manuscrit LaTeX compilable.

## Niveau 1 : reproduction

- [ ] Tests exécutables.
- [ ] Première expérience reproductible.
- [ ] Résultats enregistrés.
- [ ] Précision documentée.

## Niveau 2 : proposition

- [ ] Première affirmation enregistrée.
- [ ] Obligations de preuve identifiées.

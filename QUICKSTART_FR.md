# Guide de Démarrage Rapide

Guide rapide pour commencer à utiliser le projet de reconnaissance de panneaux de signalisation.

## Installation Rapide

```bash
# 1. Cloner le projet
git clone https://github.com/thchateau/traffic_sign.git
cd traffic_sign

# 2. Créer un environnement virtuel (recommandé)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Tester l'installation
python test_structure.py
```

## Configuration de Mapillary

Pour utiliser le module Mapillary :

```bash
# 1. Copier le fichier template
cp .env.template .env

# 2. Obtenir un token Mapillary
# - Créer un compte sur https://www.mapillary.com/
# - Aller sur https://www.mapillary.com/dashboard/developers
# - Créer une application et copier le token

# 3. Éditer .env et ajouter le token
# MAPILLARY_ACCESS_TOKEN=votre_token_ici
```

## Utilisation des Trois Modules

### 1. Florence - Description de Panneaux

```python
from traffic_sign.florence import FlorenceDescriptor

# Initialiser
descriptor = FlorenceDescriptor()

# Décrire un panneau
description = descriptor.describe_traffic_sign('panneau.jpg')
print(f"Description : {description}")

# Exemple de sortie :
# "Un panneau stop octogonal rouge avec bordure et texte blancs"
```

### 2. OpenCLIP - Comparaison d'Images

```python
from traffic_sign.openclip import TrafficSignMatcher, create_default_descriptions

# Initialiser
matcher = TrafficSignMatcher()

# Charger une base de descriptions
descriptions = create_default_descriptions()
matcher.load_descriptions_database(descriptions)

# Trouver les meilleures correspondances
matches = matcher.find_best_match('panneau_inconnu.jpg', top_k=3)
for desc, score in matches:
    print(f"{desc}: {score:.3f}")
```

### 3. Mapillary - Détection Géographique

```python
from traffic_sign.mapillary import MapillarySignDetector
import os

# Initialiser avec token
detector = MapillarySignDetector(
    access_token=os.getenv('MAPILLARY_ACCESS_TOKEN')
)

# Chercher des panneaux dans une zone (exemple: Paris)
bbox = (2.3, 48.85, 2.35, 48.87)  # (min_lon, min_lat, max_lon, max_lat)
signs = detector.search_traffic_signs(bbox, limit=50)

print(f"Trouvé {len(signs)} panneaux")
for sign in signs[:5]:
    print(f"Type: {sign.get('value')}")
```

## Workflow Complet

Combiner les trois approches :

```python
from traffic_sign.florence import FlorenceDescriptor
from traffic_sign.openclip import TrafficSignMatcher
from traffic_sign.mapillary import MapillarySignDetector
import os

# 1. Détecter les panneaux dans une zone avec Mapillary
detector = MapillarySignDetector(access_token=os.getenv('MAPILLARY_ACCESS_TOKEN'))
signs = detector.search_traffic_signs((2.3, 48.85, 2.35, 48.87), limit=20)

# 2. Décrire les panneaux avec Florence
descriptor = FlorenceDescriptor()
descriptions = []
for sign in signs:
    # Télécharger l'image et générer la description
    desc = descriptor.describe_traffic_sign('image_panneau.jpg')
    descriptions.append(desc)

# 3. Matcher avec la base de données via OpenCLIP
matcher = TrafficSignMatcher()
matcher.load_descriptions_database(descriptions)
matches = matcher.find_best_match('nouveau_panneau.jpg', top_k=3)

# Afficher les résultats
for desc, score in matches:
    print(f"Correspondance : {desc} ({score:.3f})")
```

## Exemples Prêts à l'Emploi

Le dossier `examples/` contient des scripts prêts à utiliser :

```bash
# Voir l'exemple Florence
python examples/example_florence.py

# Voir l'exemple OpenCLIP
python examples/example_openclip.py

# Voir l'exemple Mapillary
python examples/example_mapillary.py

# Voir le workflow complet
python examples/complete_workflow.py
```

## Cas d'Usage

### 1. Inventaire de Panneaux d'une Ville

```python
# Récupérer tous les panneaux de Paris
detector = MapillarySignDetector(access_token=token)
bbox = (2.25, 48.81, 2.42, 48.90)  # Paris complet
signs = detector.search_traffic_signs(bbox, limit=1000)

# Analyser la distribution
types = {}
for sign in signs:
    sign_type = sign.get('value', 'unknown')
    types[sign_type] = types.get(sign_type, 0) + 1

print("Distribution des panneaux :")
for sign_type, count in sorted(types.items(), key=lambda x: x[1], reverse=True):
    print(f"  {sign_type}: {count}")
```

### 2. Reconnaître un Panneau Inconnu

```python
# Utiliser Florence pour la description
descriptor = FlorenceDescriptor()
desc = descriptor.describe_traffic_sign('panneau_mystere.jpg')
print(f"Description AI : {desc}")

# Utiliser OpenCLIP pour matcher
matcher = TrafficSignMatcher()
matcher.load_descriptions_database(create_default_descriptions())
matches = matcher.find_best_match('panneau_mystere.jpg', top_k=1)
print(f"Type probable : {matches[0][0]}")
```

### 3. Comparer Deux Panneaux

```python
matcher = TrafficSignMatcher()
similarity = matcher.compare_images('panneau1.jpg', 'panneau2.jpg')
print(f"Similarité : {similarity:.3f}")

if similarity > 0.9:
    print("Panneaux très similaires")
elif similarity > 0.7:
    print("Panneaux similaires")
else:
    print("Panneaux différents")
```

## Dépannage

### Erreur : "No module named 'PIL'"
```bash
pip install Pillow
```

### Erreur : "No module named 'transformers'"
```bash
pip install transformers torch
```

### Erreur : "No module named 'open_clip'"
```bash
pip install open_clip_torch
```

### Erreur Mapillary : "Mapillary access token is required"
```bash
# Vérifier que le token est bien configuré dans .env
cat .env
# Ou définir la variable d'environnement
export MAPILLARY_ACCESS_TOKEN=votre_token
```

### Mémoire insuffisante pour les modèles
```python
# Utiliser CPU au lieu de GPU
descriptor = FlorenceDescriptor(device='cpu')
matcher = TrafficSignMatcher(device='cpu')
```

## Ressources Supplémentaires

- **README.md** - Documentation complète
- **CONTRIBUTING.md** - Guide de contribution
- **examples/** - Exemples d'utilisation
- **.env.template** - Template de configuration

## Support

Pour toute question :
1. Consulter la documentation complète dans README.md
2. Regarder les exemples dans examples/
3. Ouvrir une issue sur GitHub

---

Bon développement ! 🚦🤖

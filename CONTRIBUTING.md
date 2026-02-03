# Contributing to Traffic Sign Recognition

Bienvenue dans le projet de reconnaissance de panneaux de signalisation ! Ce guide vous aidera à contribuer au projet.

## Structure du Projet

Le projet est organisé en trois modules principaux :

### 1. Florence (`traffic_sign/florence/`)
Module pour la description de panneaux de signalisation utilisant le modèle Florence de Microsoft.

**Responsabilités :**
- Générer des descriptions en langage naturel des panneaux
- Traitement batch de plusieurs images
- Interface avec le modèle Florence-2

**Technologies :**
- PyTorch
- Transformers (Hugging Face)
- Microsoft Florence-2 model

### 2. OpenCLIP (`traffic_sign/openclip/`)
Module pour la comparaison d'images avec une base de descriptions.

**Responsabilités :**
- Calculer la similarité image-texte
- Maintenir une base de descriptions
- Comparer des images entre elles

**Technologies :**
- PyTorch
- OpenCLIP
- Vision-Language models

### 3. Mapillary (`traffic_sign/mapillary/`)
Module pour la détection géographique de panneaux via l'API Mapillary.

**Responsabilités :**
- Interface avec l'API Mapillary
- Recherche géographique de panneaux
- Récupération de métadonnées

**Technologies :**
- Requests (HTTP)
- Mapillary API v4

## Configuration de l'Environnement

### Installation Initiale

```bash
# Cloner le repository
git clone https://github.com/thchateau/traffic_sign.git
cd traffic_sign

# Créer un environnement virtuel
python -m venv venv

# Activer l'environnement virtuel
# Sur Linux/Mac:
source venv/bin/activate
# Sur Windows:
venv\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt
```

### Configuration de l'API Mapillary

1. Créer un compte sur [Mapillary](https://www.mapillary.com/)
2. Aller sur [Dashboard Developers](https://www.mapillary.com/dashboard/developers)
3. Créer une application et obtenir un token d'accès
4. Copier `.env.template` vers `.env`
5. Ajouter votre token dans `.env`

```bash
cp .env.template .env
# Éditer .env et ajouter votre token
```

## Tester Votre Installation

```bash
# Tester la structure du projet
python test_structure.py

# Tester les imports (nécessite les dépendances)
python -c "from traffic_sign import florence, openclip, mapillary; print('OK')"
```

## Workflow de Développement

### 1. Créer une Branche

```bash
git checkout -b feature/votre-fonctionnalite
```

### 2. Faire vos Modifications

Quelques règles à suivre :
- Suivre le style de code existant
- Documenter vos fonctions avec des docstrings
- Ajouter des exemples d'utilisation
- Tester votre code

### 3. Tester

```bash
# Tester votre module
python -c "from traffic_sign.votre_module import votre_fonction"

# Tester avec un exemple
python examples/example_votre_module.py
```

### 4. Commit et Push

```bash
git add .
git commit -m "Description de vos changements"
git push origin feature/votre-fonctionnalite
```

## Guide de Style

### Code Python

```python
def ma_fonction(param1: str, param2: int = 10) -> dict:
    """
    Description courte de la fonction.
    
    Description plus détaillée si nécessaire.
    
    Args:
        param1: Description du paramètre 1
        param2: Description du paramètre 2
        
    Returns:
        Description de ce qui est retourné
        
    Example:
        >>> result = ma_fonction("test", 5)
        >>> print(result)
        {'status': 'ok'}
    """
    # Votre code ici
    return {'status': 'ok'}
```

### Documentation

- Utiliser des docstrings pour toutes les fonctions et classes
- Ajouter des exemples d'utilisation
- Documenter les paramètres et valeurs de retour
- Inclure des notes sur les dépendances ou limitations

## Idées d'Améliorations

### Florence
- [ ] Support pour d'autres modèles Florence
- [ ] Optimisation des performances (batching)
- [ ] Cache des embeddings
- [ ] Support pour Florence-2-large

### OpenCLIP
- [ ] Sauvegarde/chargement de bases de descriptions
- [ ] Support pour d'autres architectures CLIP
- [ ] Visualisation des similarités
- [ ] Interface de recherche avancée

### Mapillary
- [ ] Cache des requêtes API
- [ ] Support pour l'upload d'images
- [ ] Filtres avancés (date, type de panneau)
- [ ] Téléchargement d'images haute résolution

### Général
- [ ] Tests unitaires
- [ ] Interface en ligne de commande (CLI)
- [ ] Interface web avec Streamlit/Gradio
- [ ] Documentation API complète
- [ ] Tutoriels Jupyter Notebook
- [ ] Benchmarks de performance
- [ ] Support Docker

## Ressources

### Documentation Officielle
- [Florence-2](https://huggingface.co/microsoft/florence-2-base) - Modèle Florence
- [OpenCLIP](https://github.com/mlfoundations/open_clip) - OpenCLIP documentation
- [Mapillary API](https://www.mapillary.com/developer/api-documentation) - API Mapillary

### Tutoriels
- [PyTorch](https://pytorch.org/tutorials/) - Tutoriels PyTorch
- [Transformers](https://huggingface.co/docs/transformers/) - Documentation Transformers
- [CLIP](https://github.com/openai/CLIP) - CLIP original

## Questions ?

Pour toute question :
1. Vérifier la documentation dans README.md
2. Regarder les exemples dans `examples/`
3. Ouvrir une issue sur GitHub
4. Contacter l'équipe du projet

## Licence

Voir le fichier [LICENSE](LICENSE) pour les détails.

---

Merci de contribuer au projet de reconnaissance de panneaux de signalisation ! 🚦

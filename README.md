# 🏦 Système de Détection de Fraude Bancaire en Temps Réel
# 📋 Description
Application web de détection de fraudes bancaires utilisant un modèle de Machine Learning (Random Forest) pour classifier les transactions en temps réel. Le système analyse les caractéristiques d'une transaction pour déterminer si elle est potentiellement frauduleuse ou légitime.
# 🚀 Fonctionnalités

Prédiction en temps réel : Classification instantanée des transactions
Interface utilisateur intuitive : Application web Streamlit facile à utiliser
Modèle pré-entraîné : Utilise un Random Forest optimisé
Prétraitement intégré : Normalisation automatique des données avec StandardScaler

# 🛠️ Technologies Utilisées

Python : Langage de programmation principal
Streamlit : Framework pour l'interface web
Scikit-learn : Bibliothèque de Machine Learning
Joblib : Sérialisation et chargement des modèles
NumPy : Manipulation des données numériques

# 📦 Prérequis
bashPython 3.7+
pip (gestionnaire de paquets Python)
⚙️ Installation

Cloner le repository

bashgit clone [URL_DU_REPO]
cd [NOM_DU_DOSSIER]

Installer les dépendances

bashpip install streamlit
pip install scikit-learn
pip install joblib
pip install numpy
Ou créez un fichier requirements.txt :
txtstreamlit==1.28.0
scikit-learn==1.3.0
joblib==1.3.0
numpy==1.24.0
Puis installez avec :
bashpip install -r requirements.txt
📁 Structure du Projet
├── app.py                 # Application Streamlit principale
├── Examen_ML.ipynb
├── model_rf.pkl          # Modèle Random Forest sauvegardé
├── scaler.pkl            # StandardScaler sauvegardé
└── README.md             # Documentation du projet
🎯 Utilisation

Lancer l'application

bashstreamlit run app.py

Accéder à l'interface

Ouvrez votre navigateur à l'adresse : http://localhost:8501


Effectuer une prédiction

Entrez les valeurs pour les 16 caractéristiques (V1 à V21)
Cliquez sur le bouton "Prédire"
Le système affichera si la transaction est frauduleuse ou normale



# 📊 Caractéristiques d'Entrée
Le modèle utilise 16 caractéristiques principales issues d'une analyse PCA (Principal Component Analysis) :

V1, V2, V3, V4, V5, V6, V7 : Composantes principales 1 à 7
V9, V10, V11, V12 : Composantes principales 9 à 12
V14, V16, V17, V18 : Composantes principales 14, 16, 17, 18
V21 : Composante principale 21


Note : Ces caractéristiques sont des valeurs transformées par PCA pour protéger la confidentialité des données bancaires originales.

⚠️ Configuration Importante
Avant d'exécuter l'application, modifiez les chemins des fichiers dans app.py :
python# Remplacez ces lignes avec vos propres chemins
model = joblib.load('model_rf.pkl')  # Chemin relatif
scaler = joblib.load('scaler.pkl')   # Chemin relatif
🔍 Exemple d'Utilisation

Lancez l'application
Entrez des valeurs pour chaque caractéristique (généralement entre -5 et 5)
Cliquez sur "Prédire"
Résultat :

✅ "La transaction est prédite comme normale"
⚠️ "La transaction est prédite comme frauduleuse"



📈 Performance du Modèle
Le modèle Random Forest a été entraîné pour :

Maximiser la détection des fraudes (rappel élevé)
Minimiser les faux positifs
Fournir des prédictions rapides en temps réel

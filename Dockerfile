# Utilise l'image officielle Python (basée sur Debian par défaut)
FROM python:3.12-slim

# Crée un dossier de travail
WORKDIR /app

# Copie les fichiers de l’hôte dans le conteneur
COPY . /app

# Installe les dépendances si requirements.txt est présent
# (tu peux ignorer cette ligne si tu n’en as pas)
RUN pip install --no-cache-dir -r requirements.txt

# Commande par défaut
CMD ["python"]

# Utiliser une image de base (par exemple, Python pour une application Flask/Django)
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de l'application
COPY ./requirements.txt ./

# Installer les dépendances
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copier les fichiers de l'application
COPY ./app.py ./

# Exposer le port (par exemple, 5000 pour Flask)
EXPOSE 5000

# Commande pour démarrer l'application
CMD ["python", "app.py"]

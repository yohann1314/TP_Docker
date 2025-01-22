# Utiliser une image de base (par exemple, Python pour une application Flask/Django)
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de l'application
COPY . .

# Installer les dépendances
RUN pip install -r requirements.txt

# Exposer le port (par exemple, 5000 pour Flask)
EXPOSE 5000

# Commande pour démarrer l'application
CMD ["python", "app.py"]

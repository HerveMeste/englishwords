# Utilisez une image de base qui inclut Python (par exemple, python:3.10)
FROM python:latest

# Installez Git
RUN apt-get update && apt-get install bash && apt-get install -y git

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Clonez le dépôt Git dans le répertoire de travail
RUN git clone https://github.com/HerveMeste/englishwords.git .
RUN pip install tomli

CMD ["python", "quiz.py"]



import subprocess
import os

# Chemin vers le fichier
file_path = 'list_of_name.txt'

# Lire et exécuter chaque ligne du fichier comme une commande shell
with open(file_path, 'r') as file:
    for line in file:
        line = line.strip()  # Enlever les espaces et sauts de ligne
        if line:  # Vérifier si la ligne n'est pas vide
            # Extraire le chemin du fichier de sortie de la commande
            out_path_arg = "--out_path '"
            start = line.find(out_path_arg) + len(out_path_arg)
            end = line.find("'", start)
            out_path = line[start:end]

            # Créer le dossier si nécessaire
            os.makedirs(os.path.dirname(out_path), exist_ok=True)

            try:
                # Exécuter la ligne comme une commande shell
                subprocess.run(line, shell=True, check=True)
            except subprocess.CalledProcessError as e:
                print(f"Erreur lors de l'exécution de la commande '{line}': {e}")
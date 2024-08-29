import time
import subprocess
import requests

# Fonction pour démarrer le serveur SRS
def start_srs():
    print("Le serveur SRS a déjà été démarré via GitHub Actions.")
    return

# Fonction pour vérifier l'état du serveur SRS
def check_srs():
    try:
        print("Vérification de l'état du serveur SRS...")
        time.sleep(5)
        response = requests.get("http://localhost:8080")
        if response.status_code == 200:
            print("SRS fonctionne correctement.")
        else:
            print(f"SRS ne répond pas correctement, code: {response.status_code}")
    except Exception as e:
        print(f"Erreur lors de la vérification du serveur SRS : {e}")

if __name__ == "__main__":
    start_srs()
    check_srs()

    # Maintenir le script en cours d'exécution
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        print("Interruption manuelle du processus de surveillance."

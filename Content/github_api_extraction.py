import requests
import json
from time import sleep

# === CONFIGURACIÓN ===

GITHUB_TOKEN = "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"

HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28"
}

def search_repositories(query="machine learning", per_page=5):
    """
    Buscar repositorios públicos relacionados con un tema.
    """
    url = f"https://api.github.com/search/repositories?q={query}&per_page={per_page}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        data = response.json()
        print("🔍 Repositorios encontrados:")
        for repo in data["items"]:
            print(f"- {repo['full_name']}")
        return data
    else:
        print(f"❌ Error {response.status_code}: {response.text}")
        return None

def get_commits(owner, repo, max_pages=2):
    """
    Obtener lista de commits con paginación.
    """
    all_commits = []
    for page in range(1, max_pages + 1):
        url = f"https://api.github.com/repos/{owner}/{repo}/commits?page={page}&per_page=5"
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 200:
            commits = response.json()
            all_commits.extend(commits)
            print(f"✅ Página {page}: {len(commits)} commits")
        elif response.status_code == 403:
            print("⚠️ Rate limit alcanzado. Esperando 60 segundos...")
            sleep(60)
        else:
            print(f"❌ Error {response.status_code}: {response.text}")
            break
    return all_commits

def get_readme(owner, repo):
    """
    Obtener el contenido del archivo README.md de un repositorio.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/README.md"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        content = response.json()
        print("📄 README.md encontrado:")
        print(f"- Nombre: {content['name']}")
        print(f"- Primeros 100 caracteres (Base64):\n{content['content'][:100]}")
    elif response.status_code == 404:
        print("❌ No se encontró el archivo README.md.")
    else:
        print(f"❌ Error {response.status_code}: {response.text}")

# === PRUEBA DE EJECUCIÓN ===

if __name__ == "__main__":
    print("==> BUSCAR REPOSITORIOS")
    repos_data = search_repositories("machine learning")
    
    if repos_data:
        owner, repo = repos_data["items"][0]["full_name"].split("/")
        
        print("\n==> OBTENER COMMITS")
        commits = get_commits(owner, repo)

        print("\n==> OBTENER README.md")
        get_readme(owner, repo)

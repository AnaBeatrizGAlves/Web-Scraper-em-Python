import requests
from bs4 import BeautifulSoup

URL = "https://www.imdb.com/chart/toptv/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/117.0.0.0 Safari/537.36"
}

response = requests.get(URL, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    print("📺 Top 10 Séries do IMDb:\n")
    series = soup.select("li.ipc-metadata-list-summary-item")[:10]

    for idx, item in enumerate(series, start=1):
        title = item.select_one("h3").text.strip()
        rating = item.select_one("span.ipc-rating-star--imdb").text.strip().split()[0]
        print(f"{idx}. {title} ⭐ {rating}")

else:
    print("Erro ao acessar a página:", response.status_code)

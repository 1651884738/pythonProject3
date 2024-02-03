import requests
import bs4

header = {
    "Referer":
        "https://ssr1.scrape.center/",
    "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
}

response = requests.get("https://p0.meituan.net/movie/ce4da3e03e655b5b88ed31b5cd7896cf62472.jpg@464w_644h_1e_1c",
                        headers=header)

name = 1

with open(f"test_{name}.jpg", "wb") as f:
    f.write(response.content)

# res = requests.get("https://ssr1.scrape.center/",headers=header)
# print(res.text)

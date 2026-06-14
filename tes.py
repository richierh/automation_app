import requests

API_KEY = "56125298-2c52cff0f8587aff9bf7e1441"

url = "https://pixabay.com/api/videos/"



params = {
    "key": API_KEY,
    "q": "relaxing",
    "per_page": 3
}

res = requests.get(url, params=params)

print("STATUS:", res.status_code)
print(res.text[:500])

if res.status_code == 200: 
    data = res.json()

    print("TOTAL:", data["total"])
    print("HITS:", len(data["hits"]))

    if data["hits"]:
        print("IMAGE URL:")
        print(data["hits"][0]["largeImageURL"])
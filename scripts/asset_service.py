import requests
from pathlib import Path
import hashlib
from dotenv import load_dotenv
import os

load_dotenv()

CACHE_DIR = Path("cache/videos")
CACHE_DIR.mkdir(parents=True, exist_ok=True)

pexels_key = os.getenv("PEXELS_API_KEY")
pixabay_key = os.getenv("PIXABAY_API_KEY")

# PEXELS_API_KEY = "YOUR_PEXELS_KEY"
# PIXABAY_API_KEY = "YOUR_PIXABAY_KEY"
PEXELS_API_KEY = pexels_key
PIXABAY_API_KEY = pixabay_key


def get_cache_path(keyword: str):
    filename = hashlib.md5(keyword.encode()).hexdigest() + ".mp4"
    return CACHE_DIR / filename


def fetch_from_pexels(keyword: str):
    url = "https://api.pexels.com/v1/videos/search"

    headers = {
        "Authorization": PEXELS_API_KEY
    }

    params = {
        "query": keyword,
        "per_page": 5
    }

    res = requests.get(url, headers=headers, params=params, timeout=10)
    data = res.json()

    videos = data.get("videos", [])
    if not videos:
        return None

    video = videos[0]
    files = video["video_files"]

    best = max(files, key=lambda x: x.get("width", 0))
    return best["link"]


def fetch_from_pixabay(keyword: str):
    url = "https://pixabay.com/api/videos/"

    params = {
        "key": PIXABAY_API_KEY,
        "q": keyword,
        "per_page": 5
    }

    res = requests.get(url, params=params, timeout=10)
    data = res.json()

    hits = data.get("hits", [])
    if not hits:
        return None

    video = hits[0]["videos"]["medium"]
    return video["url"]

def download_video(url: str, path: Path):
    r = requests.get(url, stream=True, timeout=30)

    with open(path, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024 * 1024):
            f.write(chunk)



def get_background_video(keyword: str):
    cache_path = get_cache_path(keyword)

    # 0. CACHE FIRST (biar cepat)
    if cache_path.exists():
        print("CACHE HIT")
        return str(cache_path)



    # 1. PEXELS
    print("TRY PEXELS")
    url = fetch_from_pexels(keyword)

    # 2. PIXABAY
    if not url:
        print("TRY PIXABAY")
        url = fetch_from_pixabay(keyword)

    # 3. MANUAL / LOCAL fallback
    if not url:
        print("FALLBACK LOCAL")
        local = Path("assets/videos") / "default.mp4"

        if local.exists():
            return str(local)

        raise Exception("No video found anywhere")

    # 4. DOWNLOAD & CACHE
    print("DOWNLOADING")
    download_video(url, cache_path)

    return str(cache_path)
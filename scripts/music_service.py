import requests
from pathlib import Path
import hashlib
from dotenv import load_dotenv
import os

load_dotenv()

CACHE_DIR = Path("cache/music")
CACHE_DIR.mkdir(parents=True, exist_ok=True)

PIXABAY_API_KEY = os.getenv("PIXABAY_API_KEY")


def get_cache_path(mood: str):
    filename = hashlib.md5(mood.encode()).hexdigest() + ".mp3"
    return CACHE_DIR / filename


def fetch_music_from_pixabay(mood: str):

    url = "https://pixabay.com/api/audio/"

    params = {
        "key": PIXABAY_API_KEY,
        "q": mood,
        "per_page": 10
    }

    try:
        res = requests.get(
            url,
            params=params,
            timeout=15
        )

        data = res.json()
        print(res.status_code)
        print(res.text[:500])
        print('apaan sih')

        hits = data.get("hits", [])

        if not hits:
            return None

        track = hits[0]

        return track["audio"]

    # except Exception as e:
    #     import traceback
    #     traceback.print_exc()
    #     return None    
    except Exception as e:
        print(e)
        return None


def download_music(url: str, path: Path):

    r = requests.get(
        url,
        stream=True,
        timeout=30
    )

    with open(path, "wb") as f:

        for chunk in r.iter_content(
            chunk_size=1024 * 1024
        ):
            f.write(chunk)


def get_music(mood):

    cache_path = get_cache_path(mood)

    # 1. CACHE
    if cache_path.exists():
        print("MUSIC CACHE HIT")
        return str(cache_path)

    # 2. PIXABAY
    print("SEARCH PIXABAY MUSIC")

    url = fetch_music_from_pixabay(mood)
    print(f"PIXABAY MUSIC URL: {url}")

    # 3. LOCAL FALLBACK
    if not url:

        print("LOCAL MUSIC FALLBACK")

        local = Path(
            f"assets/musics/{mood}.mp3"
        )

        if local.exists():
            return str(local)

        default_music = Path(
            "assets/musics/default.mp3"
        )

        if default_music.exists():
            return str(default_music)

        raise Exception(
            f"No music found for mood: {mood}"
        )

    # 4. DOWNLOAD
    print("DOWNLOADING MUSIC")

    download_music(
        url,
        cache_path
    )

    return str(cache_path)
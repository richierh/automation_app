from pathlib import Path
from datetime import datetime

# five parameters to the function of render_video
def render_video(
    title,
    template,
    texts,
    asset_keyword,
    music_mood
):

    filename = datetime.now().strftime("%Y%m%d_%H%M%S")

    output_path = f"outputs/videos/{filename}.mp4"
    print('berhasil kok gimana sih')

    # nanti panggil ffmpeg di sini

    Path(output_path).touch()

    return {
        "status": "success",
        "video_path": output_path,
        "preview_url": f"/preview/{filename}.mp4",
        "llll":"berhasil kok"
    }
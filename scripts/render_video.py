from fileinput import filename
from pathlib import Path
from datetime import datetime
from scripts.asset_service import get_background_video 
from scripts.music_service import get_music
from scripts.ffmpeg_renderer import render_video_ffmpeg

# five parameters to the function of render_video
def render_video(
    title ='oalah',
    template = 'Educational',
    texts=['dd','dfd','dfdf','dfdf','dfdf'],
    asset_keyword='ocean',
    music_mood='relaxing'):



    video_asset = get_background_video(
        asset_keyword
    )

    music_asset = get_music(
        music_mood
    )

    print('berhasil kok gimana sih')


    filename = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = f"outputs/videos/{filename}.mp4"


    render_video_ffmpeg(
    template_path=template,
    src_video=video_asset,
    src_music=music_asset,
    out_video=output_path,
    title=title,
    texts=texts
    )    
    print('berhasil kok gimana sih')

    # nanti panggil ffmpeg di sini
    print('hello')

    return {
        "status": "success",
        "video_path": output_path,
        "preview_url": f"/preview/{filename}.mp4",
        "llll":"berhasil kok"
    }
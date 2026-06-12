from pathlib import Path
from datetime import datetime
from scripts.asset_service import get_background_video

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
    print('berhasil kok gimana sih')

    import pdb 
    pdb.set_trace()

    music_asset = download_music_from_pixabay(
        music_mood
    )


    filename = datetime.now().strftime("%Y%m%d_%H%M%S")


    output_path = render_ffmpeg(
        template=template,
        texts=texts,
        background_video=video_asset,
        music=music_asset
    )    
    print('berhasil kok gimana sih')

    # nanti panggil ffmpeg di sini
    print('hello')
    Path(output_path).touch()

    return {
        "status": "success",
        "video_path": output_path,
        "preview_url": f"/preview/{filename}.mp4",
        "llll":"berhasil kok"
    }
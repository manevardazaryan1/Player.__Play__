def upload_image(instance, filename):
    """Upload images function"""

    filename = filename.replace(" ", "_").replace("'", "").replace("-", "")
    return f'music_images/{filename}'

def upload_audio(instance, filename):
    """Upload audio function"""

    filename = filename.replace(" ", "_").replace("'", "")
    return f'music_audios/{filename}'

def upload_video(instance, filename):
    """Upload audio function"""
    
    filename = filename.replace(" ", "_").replace("'", "")
    return f'music_videos/{filename}'
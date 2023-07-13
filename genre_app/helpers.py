def upload_image(instance, filename):
    """Upload images function"""

    filename = filename.replace(" ", "_").replace("'", "")
    return f'genre_images/{filename}'
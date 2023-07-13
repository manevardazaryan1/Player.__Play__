def upload_image(instance, filename):
    """Upload images function"""

    filename = filename.replace(" ", "_").replace("'", "")
    return f'singer_images/{filename}'
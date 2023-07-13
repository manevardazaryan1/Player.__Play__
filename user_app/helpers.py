def upload_user_profile__image(instance, filename):
    """Upload user profile image"""

    instance_user_username = instance.user.username.replace(" ", "_").replace("'", "")
    filename = filename.replace(" ", "_").replace("'", "")
    return f'profile_images/{instance_user_username}_{instance.user.id}/{filename}'
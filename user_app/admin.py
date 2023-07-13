from django.contrib import admin
from user_app.models import User
from .models import Profile


admin.site.register(Profile)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


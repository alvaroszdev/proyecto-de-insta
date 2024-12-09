from django.contrib import admin

# Register your models here.
from profiles.models import UserProfile,Follow



@admin.register(UserProfile)
class UserProfile(admin.ModelAdmin):
    list_display = ["user","birth_date"]
    
@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ["follower","following","created_at"]
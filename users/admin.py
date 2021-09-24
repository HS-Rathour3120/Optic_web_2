from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username' ,'first_name', 'last_name',
    'year' ,'is_staff',]
    


admin.site.register(CustomUser,  UserAdmin)
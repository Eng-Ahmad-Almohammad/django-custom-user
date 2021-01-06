from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CusomUserCreationForm
from .models import CustomUser
# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CusomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username','email']


admin.site.register(CustomUser, CustomUserAdmin)
from django.contrib import admin

from .models import CustomUser

from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
   add_form = CustomUserCreationForm
   form = CustomUserChangeForm
   model = CustomUser
   list_display = ['email', 'username', 'Interest','is_staff',]

admin.site.register(CustomUser, CustomUserAdmin)
   
#admin.site.register(Page)
# Register your models here.
# Register your models here.

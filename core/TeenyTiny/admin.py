from django.contrib import admin
from .models import *

@admin.register(CategoriiPicturi)
class CategoriiPicturiAdmin(admin.ModelAdmin):
    list_display = ('nume_categorie', 'descriere_categorie', 'imagine_categorie')

@admin.register(Picturi)
class PicturiAdmin(admin.ModelAdmin):
    list_display = ('nume_pictura', 'descriere_pictura', 'imagine_pictura', 'categorie_pictura')

@admin.register(ReceivedEmails)
class ReceivedEmailsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'subject', 'date_and_time')

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('titlu', 'descriere', 'marime_imagine')

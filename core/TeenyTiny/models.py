from django.db import models

# Create your models here.

class CategoriiPicturi(models.Model):
    nume_categorie = models.CharField(max_length=100)
    descriere_categorie = models.TextField()
    imagine_categorie = models.ImageField(upload_to='TeenyTiny/images/')
    marime_imagine = models.CharField(max_length=100, default='1597px X 1597px circle png')

    class Meta:
        verbose_name_plural = 'Categorii de picturi'

    def __str__(self):
        return self.nume_categorie


class Picturi(models.Model):
    nume_pictura = models.CharField(max_length=100)
    descriere_pictura = models.TextField()
    imagine_pictura = models.ImageField(upload_to='TeenyTiny/images/')
    categorie_pictura = models.ForeignKey(CategoriiPicturi, default='Nealocat', on_delete=models.SET_DEFAULT)
    marime_imagine = models.CharField(max_length=100, default='1654px(latime) X 2339px (inaltime) jpg')
    class Meta:
        verbose_name_plural = 'Picturi'

class ReceivedEmails(models.Model):
    subject = models.CharField(max_length=100)
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    email = models.EmailField()
    question = models.TextField(max_length=3500)
    date_and_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Emailuri primite'


class AboutUs(models.Model):
    titlu = models.CharField(max_length=100)
    descriere = models.TextField()
    imagine = models.ImageField(upload_to='TeenyTiny/images/')
    marime_imagine = models.CharField(max_length=100, default='1654px(latime) X 2339px (inaltime) jpg')

    class Meta:
        verbose_name_plural = 'About us'

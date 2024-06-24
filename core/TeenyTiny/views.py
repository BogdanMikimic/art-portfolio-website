from django.shortcuts import render
from .models import *
from .forms import MyContactForm
from .sisiMailSender import MailSender
# Create your views here.

def homepage(request):
    return render(request, 'TeenyTiny/home.html')

def categories(request):
    cat_objects = CategoriiPicturi.objects.all()
    return render(request, 'TeenyTiny/categories.html', {'cat_handle':cat_objects})

def category(request, categorie):
    id_categorie_raw = CategoriiPicturi.objects.filter(nume_categorie=categorie).values('id')[0]
    id_categorie = id_categorie_raw['id']
    obiecte = Picturi.objects.filter(categorie_pictura=id_categorie).all()
    return render(request, 'TeenyTiny/category.html', {'handle_obiecte':obiecte, 'handle_categorie':categorie})

def pictura(request, id_pictura):
    pictura_selectata = Picturi.objects.filter(id=id_pictura).all()
    id_categorie_in_care_e_pictura_dirty = Picturi.objects.filter(id=id_pictura).values('categorie_pictura')[0]
    id_categorie_in_care_e_pictura_clean  = id_categorie_in_care_e_pictura_dirty['categorie_pictura']
    nume_categorie_dirty = CategoriiPicturi.objects.filter(id=id_categorie_in_care_e_pictura_clean).values('nume_categorie')[0]
    nume_categorie_clean = nume_categorie_dirty['nume_categorie']
    return render(request, 'TeenyTiny/pictura.html', {'obiect_handle':pictura_selectata, 'nume_categorie':nume_categorie_clean})

def aboutme(request):
    about_me = AboutUs.objects.all()
    return render(request, 'TeenyTiny/aboutme.html', {'about_me':about_me})

def contact(request, question):
    if request.method == 'GET':
        if question != 0: #in question e stocat id-ul picturrii. Daca e zero, e general question
            pictura_selectata = Picturi.objects.filter(id=question).all()[0]
        elif question == 0:
            pictura_selectata = None
        my_form = MyContactForm()
        return render(request, 'TeenyTiny/contact.html', {'pictura_handle':pictura_selectata , 'form_handle':my_form})
    elif request.method == 'POST':
        if question == 0:
            subiect = 'Intrebare generala'
        elif question != 0:
            sub = Picturi.objects.filter(id=question).values('nume_pictura')[0]
            sub1 = sub['nume_pictura']
            subiect = f'Pictura de interes: {sub1}'
        filled_form = MyContactForm(request.POST)
        if filled_form.is_valid():
            email_content = f'''
First name: {filled_form.cleaned_data["first_name"]}
Last Name: {filled_form.cleaned_data["last_name"]}
Email: {filled_form.cleaned_data["email"]}
Question: {filled_form.cleaned_data["question"]}'''
            email_title = subiect
            MailSender(email_title, email_content)
            obiect = filled_form.save(commit=False)
            obiect.subject = subiect
            obiect.save()
        return render(request, 'TeenyTiny/thankyou.html')

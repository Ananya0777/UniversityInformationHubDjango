from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from .models import Contact


# Create your views here.

def contact(request):
    contacts = Contact.objects.all()

    data = {
        'contacts': contacts,
    }
    return render(request, 'contact.html', data)


def contacts(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        print(name, email, phone, content)
        contacts = Contact(name=name, email=email, phone=phone, content=content)
        contacts.save()
        return render(request, 'admin/contact.html')



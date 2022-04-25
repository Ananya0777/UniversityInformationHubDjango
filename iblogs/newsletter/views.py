# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import SubscribersForm, MailMessageForm
from .models import Subscribers
from django.contrib import messages
from django.core.mail import send_mail
from django_pandas.io import read_frame


# Create your views here.

def index(request):
    if request.method == 'POST':
        form = SubscribersForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subscription successful')
            return redirect('/newsletter')
    else:
        form = SubscribersForm()

    context = {
        'form': form,
    }

    return render(request, 'index.html', context)


def mail_letter(request):
    emails = Subscribers.objects.all()
    df = read_frame(emails, fieldnames=['email'])
    mail_list = df['email'].values.tolist()
    print(mail_list)

    if request.method == 'POST':
        form = MailMessageForm(request.POST)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')
            message = form.cleaned_data.get('message')

            send_mail(
                title,
                message,
                'ananyavij777@gmail.com',
                mail_list,
                fail_silently=False,
            )
            messages.success(request, 'Message has been sent to the mail list')
            return redirect('/mail')
    else:
        form = MailMessageForm()

    context = {
        'form': form,
    }
    return render(request, 'mail_letter.html', context)

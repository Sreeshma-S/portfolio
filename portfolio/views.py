from django.shortcuts import render, redirect
from . forms import ContactForm
from django.http import HttpResponse
from django.core.mail import EmailMessage

def home(request):
    # return render(request, 'portfolio/backup_11042024.html')
    return render(request, 'portfolio/index.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            EmailMessage(
                'Contact Form Submission from {}'.format(name),
                message,
                'form-response@example.com',  # Send from (your website)
                ['JohnDoe@gmail.com'],  # Send to (your admin email)
                [],
                reply_to=[email]  # Email from the form to get back to
            ).send()

            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'portfolio/contact.html', {'form': form})


def success(request):
   return HttpResponse('Success, your message is delivered. Thanks!')
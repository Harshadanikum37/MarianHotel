from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request,'index.html',{})

def contact(request):
    if request.method=="POST":
        Enter_Message=request.POST['message']
        Enter_your_name=request.POST['name']
        Email=request.POST['email']
        # to send an email
        send_mail(
            Enter_your_name , # subject
           Enter_Message, # message
            Email, # from message
              ['harshadanikum37@gmail.com'],  # to mail
        )
        return render(request, 'contact.html', {'Enter_your_name': Enter_your_name})
    else:
        return render(request, 'contact.html', {})

def about(request):
    return render(request, 'about.html', {})

def services(request):
    return render(request, 'services.html', {})

def blog(request):
    return render(request, 'blog.html', {})

def rooms(request):
    return render(request, 'rooms.html', {})

def elements(request):
    return render(request, 'elements.html', {})






# Create your views here.

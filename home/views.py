from django.shortcuts import render

from django.core.mail import send_mail
#from .forms import ContactForm

def home(request):
    print("home called")
    return render(request, 'home/index.html')


def about(request):
    return render(request, 'home/about-us.html')


def service(request):
    return render(request, 'home/services.html')


def portfolio(request):
    return render(request, 'home/portfolio.html')


def download(request):
    return render(request, 'home/desktopWMS.html')




def contact(request):
    return render(request, 'home/contact-us.html')

def contactF(request):
    #return render(request, 'home/contact-us.html')
    if request.method == "POST":
        name_form = request.POST.get('name')
        email_form = request.POST.get('email')
        message_form = request.POST.get('message')

        # query = request.GET.post("q")

        # send_mail('test email', message_form + email_form, email_form, ['oksmailsoft@gmail.com'])

        # form = ContactForm
    # return render(request, 'home/contact-us.html', {'form': form})
    return render(request, 'home/contact-us.html')



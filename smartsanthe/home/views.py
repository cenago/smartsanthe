from django.shortcuts import render
from django.core.mail import send_mail
#from .forms import ContactForm
import matplotlib.pyplot as plt
import numpy as np
import io, base64

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

def report(request):


    # Data for plotting
    t = np.arange(0.0, 2.0, 0.01)
    s = 1 + np.sin(2 * np.pi * t)

    t = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9
         ]

    s = [1, 3, 1, 2, 4, 3, 2, 4, 6, 4]

    fig, ax = plt.subplots()
    ax.plot(t, s)

    ax.set(xlabel='time (s)', ylabel='voltage (mV)',
           title='About as simple as it gets, folks')
    ax.grid()

    fig.savefig("test.png")
    flike = io.BytesIO()
    fig.savefig(flike)
    b64 = base64.b64encode(flike.getvalue()).decode()


    return render(request, 'home/plotxxreport.html',
                  { "chart": b64}, status=200)


def contact(request):
    return render(request, 'home/contact-us.html')

def contactF(request):
    #return render(request, 'home/contact-us.html')
    if request.method == "POST":
        name_form = request.POST.get('name')
        email_form = request.POST.get('email')
        message_form = request.POST.get('message')

        #query = request.GET.post("q")

        # send_mail('test email', message_form + email_form, email_form, ['oksmailsoft@gmail.com'])

        #form = ContactForm
    #return render(request, 'home/contact-us.html', {'form': form})
    return render(request, 'home/contact-us.html')



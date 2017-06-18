from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import RequestContext
from django.core.mail import send_mail
from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages

from .forms import ContactUsForm
from .forms import MemberForm
from .forms import VolunteerForm

from django.core.mail import send_mail


def dsdash(request):
    return HttpResponse("Hello, world. You're at the index.")


def contactus(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':

        form = ContactUsForm(request.POST)

        # if form.is_valid():

        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        send_to = 'abungaphares@gmail.com'

        subject = 'New Contact US Form SignUp'


        mail = "Name :" + " " + name + " " + "Email :" + " " + email + " " + "Phone" + " " + phone + " " + "Message" + " " + message

        sendmail(send_to, subject, mail)

        messages.success(request, 'Thank you for contacting us. '
                                  'Your message has been received, o'
                                  'ne of our representatives will be '
                                  'in touch with you shortly')

         #  redirect to a new URL:

        return HttpResponseRedirect('/contacts/')

        # else:
        #     form = ContactUsForm()

    # if a GET (or any other method) we'll create a blank form
    else:

        return HttpResponseRedirect('/contacts/')
        form = ContactUsForm()

    return HttpResponseRedirect('/contacts/')
    #return render(request, '/contacts/', {'form': form})



def member(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':

        form = MemberForm(request.POST)

        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        membertype = request.POST['membertype']
        condition = request.POST['condition']
        interest = request.POST.getlist('interest')

        send_to = 'abungaphares@gmail.com'

        subject = 'New deserve Member'


        mail = "Name :" + " " + name + " " + "Email :" + " " + email + " " + "Phone" + " " + phone + " " + "Member Type" \
               + " " + membertype + " " + "Condition" + " " + condition + " " + "Interest" + " " + str(interest)
        sendmail(send_to, subject, mail)

        messages.success(request, 'Thank you for contacting us. '
                                  'Your message has been received, o'
                                  'ne of our representatives will be '
                                  'in touch with you shortly')

         #  redirect to a new URL:

        return HttpResponseRedirect('/member/')

    else:

        return HttpResponseRedirect('/member/')
        form = MemberForm

    return HttpResponseRedirect('/member/')


def volunteer(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':

        form = VolunteerForm(request.POST)

        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        country = request.POST['country']
        period = request.POST['period']
        message = request.POST['message']
        interest = request.POST.getlist('interest')

        send_to = 'abungaphares@gmail.com'

        subject = 'New deserve Volunteer'


        mail = "Name :" + " " + name + " " + "Email :" + " " + email + " " + "Phone" + " " + phone + " " + "Country" + \
               " " + country + " " + "Period" + " " + period + " " + "Interest" + " " + str(interest) + " " + "Message" + " " + message


        sendmail(send_to, subject, mail)

        messages.success(request, 'Thank you for contacting us. '
                                  'Your message has been received, o'
                                  'ne of our representatives will be '
                                  'in touch with you shortly')

         #  redirect to a new URL:

        return HttpResponseRedirect('/volunteer/')

    else:

        return HttpResponseRedirect('/volunteer/')
        form = VolunteerForm

    return HttpResponseRedirect('/volunteer/')
    #return render(request, '/contacts/', {'form': form})

def sendmail( to, subject, message ):

    send_mail(subject, message, 'abungaphares@gmail.com',
              [to], fail_silently=True)

    return
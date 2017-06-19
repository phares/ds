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

send_to = ['abungaphares@gmail.com', 'info@deservefoundation.org']

def dsdash(request):
    return HttpResponse("Hello, world. You're at the index.")


def contactus(request):

    try:

        # if this is a POST request we need to process the form data
        if request.method == 'POST':

            form = ContactUsForm(request.POST)

            # if form.is_valid():

            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            message = request.POST['message']

            subject = 'New Contact US Form SignUp'

            mail = "Name :" + " " + name + " " + "Email :" + " " + email + " " + "Phone" + " " + phone + " " + "Message" + " " + message

            for email in send_to:
                sendmail(email, subject, mail)

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

    except Exception as e:
        return HttpResponseRedirect('/contacts/')



def member(request):

    try:

        # if this is a POST request we need to process the form data
        if request.method == 'POST':

            form = MemberForm(request.POST)

            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            membertype = request.POST['membertype']
            condition = request.POST['condition']
            interest = request.POST.getlist('interest')
            message = request.POST['message']

            subject = 'New deserve Member'


            mail = "Name :" + " " + name + " " + "Email :" + " " + email + " " + "Phone" + " " + phone + " " + "Member Type" \
                   + " " + membertype + " " + "Condition" + " " + condition + " " + "Interest" + " " + str(interest) \
                   + "Message" + " " + message

            for email in send_to:
                sendmail(email, subject, mail)

            messages.success(request, 'Thank you for contacting us. '
                                      'Your message has been received, o'
                                      'ne of our representatives will be '
                                      'in touch with you shortly')

             #  redirect to a new URL:

            return HttpResponseRedirect('/contacts/')

        else:

            return HttpResponseRedirect('/contacts/')
            form = MemberForm

        return HttpResponseRedirect('/contacts/')
    except Exception as e:
        return HttpResponseRedirect('/contacts/')


def volunteer(request):

    try:
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

            subject = 'New deserve Volunteer'


            mail = "Name :" + " " + name + " " + "Email :" + " " + email + " " + "Phone" + " " + phone + " " + "Country" + \
                   " " + country + " " + "Period" + " " + period + " " + "Interest" + " " + str(interest) + " " + "Message" + " " + message


            for email in send_to:
                sendmail(email, subject, mail)

            messages.success(request, 'Thank you for contacting us. '
                                      'Your message has been received, o'
                                      'ne of our representatives will be '
                                      'in touch with you shortly')

             #  redirect to a new URL:

            return HttpResponseRedirect('/contacts/')

        else:

            return HttpResponseRedirect('/contacts/')
            form = VolunteerForm

        return HttpResponseRedirect('/contacts/')
        #return render(request, '/contacts/', {'form': form})
    except Exception as e:
        return HttpResponseRedirect('/contacts/')

def sendmail( to, subject, message ):
    
    try:
        send_mail(subject, message, 'abungaphares@gmail.com',
                  [to], fail_silently=True)

        return
    except Exception as e:
        return HttpResponseRedirect('/contacts/')
from django.shortcuts import render
from .models import *
# Create your views here.
def viewEvents(request):
    return render(request,'EventParticipant_module/viewEvents.html')

from EventManager_module.models import EventDetails
def event_details_list(request):
    event_details_list = EventDetails.objects.all()
    return render(request,'EventParticipant_module/viewevents.html',{'event_details_list':event_details_list})

def add_eventparticipant_profile(request):
    return render(request,'EventParticipant_module/addeventparticipantprofile.html')

def submit_form(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        address = request.POST['address']
        university = request.POST['university']

        applicant = Applicant(first_name = first_name,
                              last_name = last_name,
                              phone_number = phone_number,
                              email = email,
                              address = address,
                              university = university)
        applicant.save()
        return render(request, 'EventParticipantHomePage.html')
    return render(request, 'EventParticipantHomePage.html')


from django.shortcuts import render,redirect,aget_list_or_404,get_object_or_404
from django.http import HttpResponse
from .forms import *
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib import messages


def register_to_event(request, event_id):
    event_details = get_object_or_404(EventDetails, id=event_id)

    if request.method == 'POST':
        form = EventApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            event_application = form.save(commit=False)
            event_application.event_details = event_details

            # Assuming users are logged in, get the username from the authenticated user
            if request.user.is_authenticated:
                event_application.username = request.user.username

            event_application.save()

            subject = 'Event Application Received'
            message = f'Thank you, {event_application.username}, for Registering for the event "{event_details.event_title}". Your application is received and under process.'
            from_email = 'sakethkunuku205@gmail.com'
            recipient_list = [event_application.email]

            try:
                send_mail(subject, message, from_email, recipient_list)
                messages.success(request, 'Registration successful! An email has been sent with event details.')
                return redirect('EventParticipant_module:event_details_list')
            except Exception as e:
                # Handle the exception (log it, display an error message, etc.)
                error_message = f"Error sending email: {e}"
                messages.error(request, error_message)
                # Include the error message in the email to the participant
                message += f'\n\nError: {error_message}'
                send_mail('Error in Event Application', message, from_email, recipient_list)
                return redirect('EventParticipant_module:event_details_list')
        else:
            messages.error(request, 'Error in the form. Please check the details.')
    else:
        form = EventApplicationForm()

    return render(request, 'EventParticipant_module/register_to_event.html', {'event_details': event_details, 'form': form})
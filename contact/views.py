from django.shortcuts import render
from .forms import ContactForm
from .models import contact 
from settings.models import Settings
# Create your views here.
def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    if contact_form.is_valid():
        name = contact_form.cleaned_data.get('name')
        email = contact_form.cleaned_data.get('email')
        message = contact_form.cleaned_data.get('message')
        new_contact = contact.objects.create(name=name,email=email,message=message)
    settings = Settings.objects.first()
    context ={
        'contact_form': contact_form,
        'settings' : settings
    }
    return render(request,'contact.html',context)
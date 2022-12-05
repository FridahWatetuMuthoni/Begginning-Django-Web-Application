from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView
from . import forms


# Create your views here.


def home(request):
    return render(request, 'home.html')


def contact(request):
    form = forms.ContactForm()

    # get values of a post request
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Submitted successfully')
            return redirect('/')

    context = {
        'form': form,
    }
    return render(request, 'contact.html', context)


def sharingPage(request):
    form = forms.SharingForm()
    if request.method == "POST":
        form = forms.SharingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form
    }
    return render(request, 'sharing.html', context)


class AboutPage(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        # **kwargs contains keyword context initialization values(if any) call base implementation to get a context
        context = super(AboutPage, self).get_context_data(**kwargs)
        # pass data to the context
        context['data'] = 'custom data'
        return context

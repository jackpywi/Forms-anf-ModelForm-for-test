from django.shortcuts import render
from .forms import ContactForm, SnippetForm


def contact(request):

    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            print(name, email)
            #form = ContactForm()   # clean fields

    context = {'form': form}
    return render(request, 'formularze/form.html', context)


def snippet_detail(request):

    form = SnippetForm()

    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            body = form.cleaned_data['body']
            print('Valid ', name, body)
            form.save()
            #form = SnippetForm()   # clean fields
    
    context = {'form': form}
    return render(request, 'formularze/form.html', context)


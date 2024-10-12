
# myapp/views.py
from django.shortcuts import render, redirect
from django import forms

# List to hold Person instances
people = []

class Person:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class PersonForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

def add_view(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            new_person = Person(username, password)
            people.append(new_person)
            return redirect('default_view')
    else:
        form = PersonForm()
    
    return render(request, 'add.html', {'form': form})


def default_view(request):
    return render(request, 'default.html', {'people': people})

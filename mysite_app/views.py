from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def home_page(request):
    return render(request, "pages/home.html")

@login_required
def view_page(request):
    return render(request, "pages/view.html")

@login_required
def edit_page(request):
    if request.user.has_perm("mysite_app.my_custom_edit_perm"):
        return render(request, "pages/edit.html")
    else:
        return render(request, "pages/error_no_perm.html")

def signup_page(request):
    if request.method == 'GET':
        my_data = {
        'form': UserCreationForm() 
        }
        return render(render, 'registration/signup.html',my_data)
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()


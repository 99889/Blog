from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def sign_ip(request):
    form = UserCreationForm()
    registered = False
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_vaild():
            form.save()
            registered = True
    
    dict = {'form':form, 'registered': registered}
    return render (request, 'App_Login/signup.html', context=dict)
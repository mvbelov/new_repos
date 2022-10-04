from django.shortcuts import render

from .forms import LoginForm
from django.contrib.auth import authenticate, login

def loginView(request):
    form = LoginForm()
    context = {'form': form}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

                return render(request, 'loginSuccess', context)

        return render(request, 'login.html')

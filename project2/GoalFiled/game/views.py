from django.shortcuts import render
from django.contrib.auth import authenticate

def homepage(request):
    return render(request,'game/index.html')

def mytodos(request):
    return render(request,'game/mytodos.html')

def loginRegisterPage(request):
    return render(request,'game/loginRegisterPage.html')


def loginRegister(request):
    if request.method == "POST":
        if request.POST.get('submit') == 'login':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username, password)
            if user is None:
                return redirect('loginRegisterPage')
            else:
                login(request, user)
                return redirect('homepage')


        elif request.POST.get('submit') == 'sign_up':
            form = UserCreationForm()
            if request.method == 'POST':
                form = UserCreationForm(request.POST)
                if form.is_valid():
                    form.save()
                    username = form.cleaned_data.get('username')
                    raw_password = form.cleaned_data.get('password1')
                    user = authenticate(username=username, password=raw_password)
                    account = Account(user=user)
                    account.save()
                    login(request, user)
                    return redirect('homepage')
            else:
                form = UserCreationForm()
            return render(request, 'loginRegisterPage', {'form': form})

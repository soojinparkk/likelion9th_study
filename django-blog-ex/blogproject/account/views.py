from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm      # 각각 로그인, 회원가입을 위한 form
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    # POST 방식으로 요청이 들어올 경우
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username=username, password=password)  # 인증을 받을 객체
            if user is not None:
                login(request, user)
            return redirect('home')

    # GET 방식으로 요청이 들어올 경우
    else :
        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('home')
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User


#username이랑 email이랑 뒤죽박죽인듯
#username = request.POST["email"] email을 username으로 바꾸면 로그인 안됨ㅋㅋ
#로그인할때는 email쓰라는 칸에 username 써야 로그인됨ㅋㅋㅋㅋㅋ
# ex) abc@naver.com 1234 abc 인 user이면 abc 1234 로 로그인해야함
def login(request):
    if request.method == "POST":
        username = request.POST["email"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
        else: 
            return render(request, 'bad_login.html')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def signup(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['repeat']:
            #회원가입
            new_user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'], email=request.POST['email'])
            #로그인
            auth.login(request, new_user ,backend='django.contrib.auth.backends.ModelBackend')
            #홈리다이렉션
            return redirect('home')
    return render(request, 'signup.html')
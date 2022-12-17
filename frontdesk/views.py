from django.shortcuts import render


# Create your views here.
def login(request):
    return render(request, "1.login.html")


def signup(request):
    return render(request, "2.signup.html")

def USstock(request):
    return render(request, "3.USstock.html")

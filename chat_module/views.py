from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import message
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User

# Create your views here.
def home(request):
	return render(request, "index.html")

def UserMessages(request):
	if request.method == "POST":
		userMessage = request.POST.get("message")
		user = request.POST.get("user")
		if len(userMessage) == 0:
			messages.error(request, "Please Enter Message Text.")
			return redirect("messages")
		else:
			addMessage = message(user=user, message=userMessage)
			addMessage.save()
			messages.success(request, "Your Message Has Been Added.")
			return redirect("messages")

	else:
		allMessages = message.objects.all()
		print(allMessages)
		context = {
		'userMessages': allMessages
		}
		return render(request, "messages.html", context)


def signup(request):
	if request.method == "POST":
		username = request.POST.get("username")
		email = request.POST.get("email")
		password1 = request.POST.get("pass1")
		password2 = request.POST.get("pass2")
		myuser = User.objects.create_user(username=username, email=email, password=password1)
		myuser.save()
		messages.success(request, "Account Created Successfully")
		return redirect("home")

	else:
		return HttpResponse("404 Not Found")

def handleLogin(request):
	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("password")
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "Logged In Successfully")
			return redirect("home")
		else:
			messages.error(request, "Invalid Username or Password. Please Try Again.")
			return redirect("home")

	else:
		return HttpResponse("404 Not Found")


def logoutUser(request):
	logout(request)
	messages.success(request, "Account Logged Out Successfully")
	return redirect("home")





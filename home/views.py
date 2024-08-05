from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .models import statistic, revenue
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm

# Create your views here.
def homepage(request):
	return render(request=request,
				  template_name="home/homex.html")

def explore(request):
	return render(request=request,
				  template_name="home/explore.html")

def stats(request):
	return render(request=request,
				  template_name="home/stats.html",
				  context={"statistics": statistic.objects.all,
				  		   "revenues": revenue.objects.all})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"Welcome, {username}")
				return redirect("home:homepage")
			else:
				messages.error(request, "Invalid username or password")
		else:
			messages.error(request, "Invalid username or password")
	form = AuthenticationForm()
	return render(request=request,
				  template_name="home/login.html",
				  context={"form":form})

def signup(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			fname = form.cleaned_data.get('fname')
			lname = form.cleaned_data.get('lname')
			messages.info(request, f"Welcome, {fname} {lname}")
			messages.success(request, f"Successfully Signed Up Account: {username}")
			login(request, user)
			return redirect("home:homepage")
		else:
			for msg in form.error_messages:
				messages.error(request, f"{msg}: {form.error_messages[msg]}")


	form = NewUserForm()
	return render(request=request,
				  template_name="home/signup.html",
				  context={"form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "Logged Out")
	return redirect("home:homepage")

def profile(request):
	return render(request=request,
				  template_name="home/profile.html")

def trans(request):
	return render(request=request,
				  template_name="home/trans.html")



from django.shortcuts import render
import requests
from .models import Users


# Create your views here.

base_url = "https://api.github.com/users/"  # Base URL for GitHub RestAPI

def index(request):
    if request.method == "POST":
        try:
            githubname = request.POST['githubname'] # Username information we got from textfield
            

        except KeyError:
            githubname = None
        response_user = requests.get(base_url+githubname)   # Get the user information using requests package
        user_info = response_user.json()              # Parse the response and put it in to user_info
        response_repos = requests.get(base_url+githubname+"/repos") # Same process for repos
        repo_info = response_repos.json()
        
      # Create an object from our model and put the data we got from API in it
        newUser = Users(username = user_info['login'],name = user_info['name'],Repos = user_info['public_repos'])  
      # Save that model to Postgre database
        newUser.save()

      # If we have "message" data in response instead of user information then return the errorpage.html 
        if "message" in user_info:   
            return render(request,"errorpage.html",{'error': "User can not found!"})
        else:
            return render(request,"index.html",{'profile':user_info,'repos':repo_info})
    else:
       return render(request,"index.html")




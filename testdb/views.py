from django.shortcuts import render
import requests
from .models import Users


# Create your views here.

base_url = "https://api.github.com/users/"

def index(request):
    if request.method == "POST":
        try:
            githubname = request.POST['githubname']
            

        except KeyError:
            githubname = None
        response_user = requests.get(base_url+githubname)
        user_info = response_user.json()
        response_repos = requests.get(base_url+githubname+"/repos")
        repo_info = response_repos.json()

        newUser = Users(username = user_info['login'],name = user_info['name'],Repos = user_info['public_repos'])
        newUser.save()


        if "message" in user_info:
            return render(request,"errorpage.html",{'error': "User can not found!"})
        else:
            return render(request,"index.html",{'profile':user_info,'repos':repo_info})
    else:
       return render(request,"index.html")




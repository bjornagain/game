from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
import content
import pdb
from models import UserProfile
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
# Create your views here.


def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response("login.html", c)
    
def auth_view(request):
    username = request.POST.get("username", "")
    password = request.POST.get("password", "")
    user = auth.authenticate(username=username, password=password)
    
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect("/accounts/loggedin")
    else:
        return HttpResponseRedirect("/accounts/invalid")
        
def loggedin(request):
    return render_to_response("loggedin.html",
                             {"full_name": request.user.username})
                             
def invalid_login(request):
    return render_to_response("invalid_login.html")
    
def logout(request):
    auth.logout(request)
    return render_to_response("logout.html")
    
def register_user(request):
    if request.method== "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/accounts/register_success")
            
    args = {}
    args.update(csrf(request))
    
    args["form"] = UserCreationForm()
    print args
    return render_to_response("register.html", args)
    
def register_success(request):
    return render_to_response("register_success.html")

@login_required
def home(request):
    user = request.user
    profile = user.profile
    if profile.textfield:
        archive = profile.textfield
        return render_to_response("home1.html", {'archive': archive})
    else:
        archive = content.intro["intro"]    
        profile.textfield = archive
        profile.save()
        return render_to_response("home1.html", {'archive': archive})

    
@csrf_exempt    
def name(request):
    user = request.user
    print user
    profile = user.profile
    name = request.POST.get('name')
    text = content.tavern["entry"] %name
    profile.charname = name
    profile.textfield = text
    profile.save()
    return HttpResponse(text)
    

@csrf_exempt  
def actions(request):
    user = request.user
    profile = user.profile
    act = request.POST.get('action')
    if act=='johnson':
        return HttpResponse(content.johnson["intro"])
    if act=='reynold':
        return HttpResponse(content.reynold["talk"])
    elif act=='look':
        text = content.tavern["look"]
        archive = profile.textfield + text
        profile.textfield = archive
        profile.save()
        return HttpResponse(text)
    else:
        return HttpResponse("didn't work")
        
def test(request):
    return render_to_response("test2.html")
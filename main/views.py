from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from content import act1
from models import UserProfile
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from formatting import parse_request
# Create your views here.

@csrf_exempt
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
        return HttpResponseRedirect("/")
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

@csrf_exempt
def register_user(request):
    if request.method== "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/accounts/login")

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
    username = str(user)
    profile = user.profile
    if profile.textfield:
        #text_body, text_end = profile.textfield, profile.textend
        save_content = profile.textfield
        charname = profile.charname
        sex = profile.sex
        attrs = profile.attrs
        return render_to_response("home.html", {'archive': save_content, 'username': username, 'charname': charname, 'sex': sex, 'attrs': attrs})
    else:
        charname = profile.charname
        sex = profile.sex
        text = act1['intro']['intro']
        return render_to_response("home.html", {'archive': text, 'username': username, 'charname': charname, 'sex': sex})





@csrf_exempt
def actions(request):
    user = request.user
    profile = user.profile
    text = parse_request(request)
    return HttpResponse(text, {'charname': profile.charname})#, 'sex': profile.sex})


def test(request):
    return render_to_response("test2.html")
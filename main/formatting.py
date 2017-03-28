from content import act1
from models import UserProfile
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
import ast

def format_handler(content, request):
    processed_content = []
    for i in content:
        if type(i) == dict:
            processed_dict = choice_selector(i, request)
            processed_content.append(processed_dict)
        elif type(i) == str:
            processed_content.append(i)
    #new_content = "<p>" + " ".join(processed_content) + "</p>"
    new_content = " ".join(processed_content)
    return new_content



def choice_selector(dict_choices, request):
    user = request.user
    profile = user.profile
    attrs = profile.attrs
    for attr in attrs:
        for key, value in dict_choices.iteritems():
            if attr == key:
                choice = dict_choices[key]
                if type(choice) == dict:
                    return choice_selector(choice,request)
                else:
                    return choice


def pronouns_format(choice, request):
    user = request.user
    profile = user.profile
    if choice==profile.sex:
        if profile.sex=='male':
            gender_nouns = {'hisher':'his', 'heshe':'he', 'himselfherself':'himself', 'heshe':'he', 'himher':'him', 'hisherS': 'his', \
            'Chisher':'His', 'Cheshe':'He', 'Chimselfherself':'Himself', 'Cheshe':'He', 'Chimher':'Him', 'ChisherS': 'His', 'manwom': 'man'}
            profile.gender_nouns = gender_nouns
            profile.save()
            return gender_nouns
        elif profile.sex=='female':
            gender_nouns = {'hisher':'her', 'heshe':'she', 'himselfherself':'herself', 'heshe':'she', 'himher':'her', 'hisherS': 'hers',  \
            'Chisher':'Her', 'Cheshe':'She', 'Chimselfherself':'Herself', 'Cheshe':'She', 'Chimher':'Her', 'ChisherS': 'Hers', 'manwom': 'lady'}
            return gender_nouns


#saves all POST data to the database, including text output, and returns formatted text
def parse_request(request):
    user = request.user
    profile = user.profile
    name, action = str(request.POST.get('name')), str(request.POST.get('action'))
    for i in request.POST:
        if i=='charname':
            attrs = profile.attrs
            charname = str(request.POST.get('charname'))
            charname = charname.capitalize()
            #attrs.append(str(request.POST.get('sex')))
            profile.attrs = attrs
            profile.charname = charname
            profile.save()
        elif i=='sex':
            attrs = []
            profile.sex = str(request.POST.get('sex'))
            attrs.append(str(request.POST.get('sex')))
            profile.attrs = attrs
            profile.save()
        elif i=='wealth':
            attrs = profile.attrs
            profile.wealth = str(request.POST.get('wealth'))
            attrs.append(str(request.POST.get('wealth')))
            profile.attrs = attrs
            profile.save()
        elif i=='form_val':
            attrs = profile.attrs
            attrs.append(str(request.POST.get('form_val')))
            profile.attrs = attrs
            profile.save()
        elif i=='form_val2':
            attrs = profile.attrs
            attrs.append(str(request.POST.get('form_val2')))
            profile.attrs = attrs
            profile.save()
        elif i=='hair_color':
            attrs = profile.attrs
            attrs.append(str(request.POST.get('hair_color')))
            profile.attrs = attrs
            profile.save()
        elif i=='hair_style':
            attrs = profile.attrs
            attrs.append(str(request.POST.get('hair_style')))
            profile.attrs = attrs
            profile.save()
    name, action = str(request.POST.get('name')), str(request.POST.get('action')) #From POST request get name and action from html button
    gender_nouns = pronouns_format(profile.sex, request)
    text_retrieve = act1[name][action] #Use name and action from POST request button attributes to retrieve next content from Content.
    test_text = format_handler(text_retrieve, request) #Pass new content through formatter to remove '['s and format output
    text = test_text.format(  \
                                      charname=profile.charname, himher=gender_nouns['himher'], heshe=gender_nouns['heshe'], \
                                      hisher=gender_nouns['hisher'], himselfherself=gender_nouns['himselfherself'], hishers=gender_nouns['hisherS'], Chimher=gender_nouns['Chimher'], \
                                      Cheshe=gender_nouns['Cheshe'], Chisher=gender_nouns['Chisher'], Chimselfherself=gender_nouns['Chimselfherself'], Chishers=gender_nouns['ChisherS'], manwom=gender_nouns['manwom'],)
    #test_text = formatter(text)
    #save_game(text, request)
    profile.textfield = text
    profile.save()
    return text





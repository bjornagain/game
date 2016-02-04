from content import act1
from models import UserProfile
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
import ast



'''def save_game(text, request):
    user = request.user
    profile = user.profile
    str1 = '<but'
    str2 = '<field'
    if text.find(str1):
        save_body, save_end = text[:text.find(str1)], text[text.find(str1):]
        profile.textfield = profile.textfield + save_body
        profile.textend = save_end
        profile.save()
    elif text.find(str2):
        save_body, save_end = text[:text.find(str2)], text[text.find(str2):]
        profile.textfield = profile.textfield + save_body
        profile.textend = save_end
        profile.save()
    else:
        profile.textfield = profile.textfield + text
        profile.save()'''

def formatter(content, request):
    if content.find('[') >= 0:
        user = request.user
        profile = user.profile
        attrs = profile.attrs
        ind, indend = content.find('['), content.find(']')
        choice = ast.literal_eval(content[ind+1:indend])
        for attr in attrs:
            for key, value in choice.iteritems():
                if attr == key:
                    new_choice = choice[key]
                    new_string = content[:ind] + new_choice + content[indend+1:]
                    return formatter(new_string, request)
    else:
        return content

def pronouns_format(choice, request):
    user = request.user
    profile = user.profile
    if choice==profile.sex:
        if profile.sex=='male':
            gender_nouns = {'hisher':'his', 'heshe':'he', 'himselfherself':'himself', 'heshe':'he', 'himher':'him', 'hisherS': 'his', \
            'Chisher':'His', 'Cheshe':'He', 'Chimselfherself':'Himself', 'Cheshe':'He', 'Chimher':'Him', 'ChisherS': 'His'}
            profile.gender_nouns = gender_nouns
            profile.save()
            return gender_nouns
        elif profile.sex=='female':
            gender_nouns = {'hisher':'her', 'heshe':'she', 'himselfherself':'herself', 'heshe':'she', 'himher':'her', 'hisherS': 'hers',  \
            'Chisher':'Her', 'Cheshe':'She', 'Chimselfherself':'Herself', 'Cheshe':'She', 'Chimher':'Her', 'ChisherS': 'Hers'}
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
    name, action = str(request.POST.get('name')), str(request.POST.get('action'))
    gender_nouns = pronouns_format(profile.sex, request)
    text_retrieve = act1[name][action]
    test_text = formatter(text_retrieve, request)
    text = test_text.format(  \
                                      charname=profile.charname, himher=gender_nouns['himher'], heshe=gender_nouns['heshe'], \
                                      hisher=gender_nouns['hisher'], himselfherself=gender_nouns['himselfherself'], hishers=gender_nouns['hisherS'], Chimher=gender_nouns['Chimher'], \
                                      Cheshe=gender_nouns['Cheshe'], Chisher=gender_nouns['Chisher'], Chimselfherself=gender_nouns['Chimselfherself'], Chishers=gender_nouns['ChisherS'],)
    #test_text = formatter(text)
    #save_game(text, request)
    profile.textfield = text
    profile.save()
    return text





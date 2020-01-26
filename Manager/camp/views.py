from django.shortcuts import render
from django.http import request, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from camp.forms import UserForm
from camp.models import CampData

def index(request):
    return render(request, 'index.html')

@csrf_exempt
@login_required
def add_rule(request):
    #qs = CampData.objects.all()
    campdata = CampData()
    if request.method == 'POST':
        campdata.rule_name = request.POST.get('rule_name')
        campdata.campaigns = request.POST.get('campaign_name')
        campdata.schedule_start = request.POST.get('schedule_start')
        campdata.schedule_stop = request.POST.get('schedule_stop')
        campdata.impressions = request.POST.get('impressions')
        campdata.clicks = request.POST.get('clicks')
        campdata.spend = request.POST.get('spend')
        campdata.eCPM = request.POST.get('eCPM')
        campdata.eCPC = request.POST.get('eCPC')
        campdata.installs = request.POST.get('installs')
        campdata.eCPI = request.POST.get('eCPI')
        campdata.status = request.POST.get('status')
    campdata.save()
    #context = {'queryset': qs}
    return render(request, 'add_rule.html', {})

@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        #profile_form = UserProfileInfoForm
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    context = {'user_form': user_form,'registered': registered }
    return render(request, 'register.html', context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive")
        else:
            return HttpResponse("Invalid details")
    else:
        return render(request, 'login.html', {})

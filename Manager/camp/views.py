from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import request, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from camp.forms import UserForm
from .models import CampData, CampGatheredData
from django.core.mail import send_mail

import datetime

def index(request):
    qs = CampData.objects.all()
    context = {"data": qs}
    return render(request, 'index.html', context)


@login_required
def add_rule(request):
    qs = CampData.objects.all()
    context = {"queryset": qs}
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
        return redirect('/')
    else:
        return render(request, 'add_rule.html', context)

def send_notification(subject):
    send_mail(['Subject'], ["The campaign is inactive"], ['inbox.kapil@outlook.com'],
    ['inbox.pawar@gmail.com'], fail_silently = False)

def criteria():
    qs = CampData.objects.all()
    ds = CampGatheredData.all()
    if qs.schedule_stop != '' and qs.schedule_stop <= datetime.now():
        status = False
        subject = 'Scheduled To Stop'
        send_notification(subject)
    if qs.impressions != '' and qs.impressions !=0 and ds.impressions <= qs.impressions:
        status = False
        subject = 'Impressions Low'
        send_notification(subject)
    if qs.clicks != '' and qs.click !=0 and ds.clicks <= qs.clicks:
        status = False
        subject = 'No of Clicks Low'
        send_notification(subject)
    if qs.eCPM != '' and qs.eCPM !=0 and ds.eCPM <= qs.eCPM:
        status = False
        subject = 'eCPM Low'
        send_notification(subject)
    if qs.eCPC != '' and qs.eCPC !=0 and ds.eCPC <= qs.eCPC:
        status = False
        subject = 'eCPC Low'
        send_notification(subject)
    if qs.installs != '' and qs.installs != 0 and ds.installs <= qs.installs:
        status = False
        subject = 'Installs Low'
        send_notification(subject)
    if qs.eCPI != '' and qs.eCPI !=0 and qs.eCPI <= ds.eCPI:
        status = False
        subject = 'eCPI Low'
        send_notification(subject)

def edit_rule(request, rule_name):
    rule = request.POST.get(name = rule_name)
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
        return redirect('/')
    else:
        return render(request, 'add_rule.html', context)

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

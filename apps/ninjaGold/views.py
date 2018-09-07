# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0

    if 'msg' not in request.session:
        request.session['msg'] = []

    context ={
    'gold': request.session['gold'],
    'msg': request.session['msg']
    } 

    return render(request, 'ninjaGold/index.html', context)

def process(request):

    if request.POST['place'] == 'Farming':
        farmMoney = random.randrange(10,21)
        request.session['gold'] = farmMoney
        request.session['msg'].append("You are in the Farm")
        

    if request.POST['place'] == 'Caveing':
        caveMoney = random.randrange(5,11)
        request.session['gold'] = caveMoney
        request.session['msg'].append("You are in the Cave")

    if request.POST['place'] == 'Housing':
        houseMoney = random.randrange(2,6)
        request.session['gold'] = houseMoney
        request.session['msg'].append("You are in the House")

    if request.POST['place'] == 'Casinoing':
        casinoMoney = random.randrange(-50,50)
        request.session['gold'] = casinoMoney
        if casinoMoney < 0:
            request.session['msg'].append("You lost at the Casino")    
        else:
            request.session['msg'].append("You won at the Casino") 

    return redirect('/')



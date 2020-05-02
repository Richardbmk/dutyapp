from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

# Create your views here.

def index(request):
    duties = Duty.objects.all()

    form = DutyForm()

    if request.method == 'POST':
        form = DutyForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = { 'duties' : duties, 'form' : form }
    return render(request, 'duties/todolist.html', context)

def updateDuty(request, pk):
    duty = Duty.objects.get(id=pk)

    form = DutyForm(instance=duty)

    if request.method == 'POST':
        form = DutyForm(request.POST, instance=duty)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form' : form}

    return render(request, 'duties/updateduty.html', context)

def deleteDuty(request, pk):
    item = Duty.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')


    context = { 'item' : item }

    return render(request, 'duties/deleteduty.html', context)
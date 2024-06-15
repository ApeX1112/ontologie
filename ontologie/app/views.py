from django.shortcuts import render,redirect
from .forms import exoform
from .models import exercice

def addview(request):
    if request.method == 'POST':

        form=exoform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=exoform()

    context={'form':form}

    return render (request,'add.html',context)


def home(request):
    exos=exercice.objects.all()
    context={'exos':exos}

    return render(request,'home.html',context)


def details(request,pk):
    exo=exercice.objects.get(pk=pk)

    context={'exo':exo}

    return render(request,'details.html',context)

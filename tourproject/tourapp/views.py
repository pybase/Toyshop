from django.shortcuts import render, redirect

from .forms import toy_form
from . models import Toy

def index(request):
    toy=Toy.objects.all()
    return render(request,'index.html',{'toy':toy})
def detail(request,id):
    toy=Toy.objects.get(id=id)
    return render(request,'detail.html',{'toy':toy})

def add_toy(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        price=request.POST.get('price')
        img=request.FILES['img']
        toy=Toy(name=name,desc=desc,price=price,img=img)
        toy.save()

    return render(request,'add.html')

def update(request,id):
    toy=Toy.objects.get(id=id)
    form=toy_form(request.POST or None,request.FILES,instance=toy)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'toy':toy,'form':form})

def delete(request,id):
    if request.method=='POST':
        toy=Toy.objects.get(id=id)
        toy.delete()
        return redirect('/')
    return render(request,'delete.html')

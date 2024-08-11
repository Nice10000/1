from django.shortcuts import render
from .forms import * # type: ignore
from .models import * TestForm



# Create your views here.
def categoryview (request) :
  categories = Category.objects.all()
  context = {'cats':categories}
  return render(request, 'category.html',context)

def unitview(request) :
  units = unit.objects.all()
  context = {'uts':units}
  return render(request, 'unit.html',context)

def test(request) :
  form = TestForm()
  context = {'form':forms}
  return render(request, 'test.html', context)
def test(request):
  form =  TestForm()
  context = {'form':form}
  return render(request, 'test.html', context)

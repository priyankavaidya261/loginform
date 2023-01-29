from django.shortcuts import render
from django.http import HttpResponse 
from django.shortcuts import render
from .forms import MyForm
# Create your views here.

def get_name(request):
	if request.method == "POST":
		form = MyForm(request.POST)
		if form.is_valid():
			return HttpResponse('/thanks')
	else:
		form = MyForm()
	return render(request,'form.html',{'form':form})
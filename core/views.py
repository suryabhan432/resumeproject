from django.shortcuts import render

# Create your views here.
def home(request):
	con = {'home':'active'}
	return render(request,'core/home.html',con)


def contact(request):
	con = {'contact':'active'}
	return render(request,'core/contact.html',con)
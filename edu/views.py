from django.shortcuts import render

# Create your views here.
def skill(request):
	con = {'skill':'active'}
	return render(request,'edu/skill.html',con)

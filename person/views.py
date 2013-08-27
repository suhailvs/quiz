from django.shortcuts import render
# Create your views here.
#from django.contrib.auth.decorators import login_required
from exam.models import ExamType,ExamSubjects
from exam import helper
#@login_required
def exam(request):
	ename='JEE Main 2013'#request.GET['examtype']
	etype=ExamType.objects.get(name=ename)
	exam,dur=helper.start_exam(etype)
	min_left=dur/60
	e_subjs=ExamSubjects.objects.filter(examtype = etype)
	return render(request,'persons/pages/showexam.html',
		{'exam_id':exam.id,'min_left':min_left,
		'subjects':e_subjs,'etype':ename})


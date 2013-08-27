# Create your views here.
import json
from django.http import HttpResponse,Http404
from django.shortcuts import render
from exam.models import Question,ExamType
from person.models import ExamAttended,OptionsSelected
from exam import helper
	
def show_question(request):
	etype=ExamType.objects.get(name=request.GET['param2'])
	#$(".examid").text();
	e_id=int(request.GET['param1'])
	exam=ExamAttended.objects.get(id=e_id)	 
		
	#subject name,qustion number,option selected 
	qlist=[request.GET['param3'],request.GET['param4'],request.GET['param5']]
	if qlist[2] in "1234":
		#next button click so it is nextquestion(save optsel of nextquestion-1)
		helper.save_option(exam,etype,qlist)	
	#full saved opts of a subject is required since we need to set the btncolors
	saved_opts=OptionsSelected.objects.get_opts(exam=exam,subj=qlist[0])
	qst=Question.objects.get(examtype=etype,
			qn=int(qlist[1]),subject=qlist[0])
	n={ 
		"qst": qst.quest,
    	"opts": [qst.quest+'_'+x for x in '1234'],
    	"qn": qst.qn,
    	"s_opts":saved_opts,
    	}
	return HttpResponse(json.dumps(n), mimetype="application/json")


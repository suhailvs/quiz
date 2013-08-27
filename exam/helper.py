from person.models import ExamAttended,OptionsSelected
from exam.models import Question

def start_exam(examtype):
	dur=examtype.duration*60
	curr_exam=ExamAttended(exam=examtype)
	curr_exam.save()
	return (curr_exam,dur)
		

def save_option(cur_exam,exam_type,q):
	mq=Question.objects.get(examtype=exam_type,qn=int(q[1])-1,subject=q[0])
	try:
		#if option already marked the just update opt_selected
		sav_opt=OptionsSelected.objects.get(exam=cur_exam,question=mq)
		sav_opt.opt_selected=q[2]
		sav_opt.save()
	except:
		sav_opt=OptionsSelected(exam=cur_exam,question=mq,
			opt_selected =q[2])
		sav_opt.save()

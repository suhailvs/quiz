from person.models import ExamAttended,OptionsSelected
from exam.models import Question

import datetime
def create_exam(examtype,ts):
	curr_exam=ExamAttended(exam=examtype)#create new exam
	curr_exam.save()
	return (curr_exam,ts)
		
def start_exam(examtype):
	dur=examtype.duration*60
	try:curr_exam = ExamAttended.objects.latest("start_time")
	except:return create_exam(examtype,dur)
	dur_exam = datetime.timedelta(0,dur ,0)
	#check did the last exam time full expired
	if (curr_exam.start_time+dur_exam) < datetime.datetime.today():	return create_exam(usr,examtype,dur)		
	#if last exam not full expired return last_exam and time left
	timeleft = datetime.datetime.today()-curr_exam.start_time
	sec_left = dur - timeleft.seconds
	return (curr_exam,sec_left)

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

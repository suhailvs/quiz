#usage
#---------

# commet out these lines in file exam/models
# admin.site.register(ExamType)
# admin.site.register(ExamSubjects)
# admin.site.register(Question,QuestionAdmin)

#open cmd. 
#then goto main directory(ie directory contains manage.py)
#then execute $: sudo python manage.py shell
#you will enter into python shell >>
# >>> from exam import models
# >>> import ci
# >>> ci.add_et(models) #examtype
# >>> ci.add_es(models)	#examsubject
# >>> ci.add_auto_q(models,etype="JEE Main 2013",pat="jee_13") #question

# now uncommet these lines in file exam/models
# admin.site.register(ExamType)
# admin.site.register(ExamSubjects)
# admin.site.register(Question,QuestionAdmin)

def add_et(M):
	datas=[['JEE Main 2013',90,180],
		['SSC CHSL 2012',200,120],['NDA 2013',200,120]]
	for i in datas:
		p=M.ExamType(name=i[0],n_questions=i[1],duration=i[2])
		p.save()
		
def add_es(M):
	fp=open('initialdata/examsubjects.txt')
	for l in fp:
		if '///' in l: continue
		t=l.strip().split('|')
		f1=M.ExamType.objects.filter(name=t[0])
		p=M.ExamSubjects(examtype=f1[0],subject=t[1],n_questions=int(t[2]))
		p.save()
	fp.close()

def add_auto_q(M,etype="JEE Main 2013",pat="jee_13"):
	f=M.ExamType.objects.get(name=etype)
	f1=M.ExamSubjects.objects.filter(examtype=f)
	for i in f1:
		for j in range(i.n_questions):
			qpattern="%s_%s_%d" %(pat,i.subject[0].lower(),j)
			p=M.Question(examtype=i.examtype,qn=j, quest=qpattern,
			subject=i.subject, chapter="please update this", correct='0')
			p.save()

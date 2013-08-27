from django.db import models
from django.contrib import admin
# Create your models here.
from exam.models import ExamType,Question
#from django.contrib.auth.models import User

class ExamAttended(models.Model):
	exam=  models.ForeignKey(ExamType)
	#user =  models.ForeignKey(User)
	start_time=models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return u'ExamID:%s, ExamType:%s' %(self.id,self.exam.name)
		
class ExamAttendedAdmin(admin.ModelAdmin):
    list_display = ('id','user','exam','start_time')
   
class OptionsSelectedManager(models.Manager):
	def get_opts(self,exam,subj):
		op=dict()
		saved_opts=self.filter(exam=exam)
		for i in saved_opts:
			if i.question.subject==subj:
				op[i.question.qn]=i.opt_selected
		return op
'''test
>>> from openshift.person.models import ExamAttended,OptionsSelected
>>> ez=ExamAttended.objects.get(id=3)
>>> OptionsSelected.objects.get_opts(exam=ez,subj="Physics")
{1: u'1', 2: u'4'}
'''
class OptionsSelected(models.Model):
	exam = models.ForeignKey(ExamAttended)
	question = models.ForeignKey(Question)
	C_CHOICES=(
        ('1', 'Option 1'),
        ('2', 'Option 2'),
        ('3', 'Option 3'),
        ('4', 'Option 4'),
        ('0', 'not sure'), )	
	opt_selected = models.CharField(max_length=1,choices=C_CHOICES)
	remarks = models.CharField(max_length=50,blank=True)
	objects=OptionsSelectedManager()
	def __unicode__(self):
		return self.question.quest


class OptionsSelectedAdmin(admin.ModelAdmin):
    list_display = ('question','exam','opt_selected')
    		
#admin.site.register(ExamAttended,ExamAttendedAdmin)
#admin.site.register(OptionsSelected,OptionsSelectedAdmin)

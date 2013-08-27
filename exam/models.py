from django.db import models
from django.contrib import admin
# Create your models here.
		
class ExamType(models.Model):
	name = models.CharField(max_length=50)
	n_questions = models.IntegerField(max_length=3,blank=True)
	duration = models.IntegerField(max_length=3,blank=True)#minutes
	def __unicode__(self):
		return self.name
		
class ExamSubjects(models.Model):
	examtype = models.ForeignKey(ExamType)
	subject = models.CharField(max_length=20)
	n_questions=models.IntegerField(max_length=3,blank=True)
	def __unicode__(self):
		return self.subject
		
class Question(models.Model):
	examtype = models.ForeignKey(ExamType)
	qn = models.IntegerField(max_length=3)#question number	
	#examtype_year_questionnumber; eg-jee_13_2
	quest=  models.CharField(max_length=20,blank=True)	
	subject = models.CharField(max_length=20,blank=True)
	chapter = models.CharField(max_length=30,blank=True)
	C_CHOICES=(
        ('1', 'Option 1'),
        ('2', 'Option 2'),
        ('3', 'Option 3'),
        ('4', 'Option 4'),
        ('0', 'not sure'), )	
	correct = models.CharField(max_length=1,choices=C_CHOICES)
	def __unicode__(self):
		return self.quest
	
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('examtype','quest','subject')
    
#admin.site.register(ExamType)
#admin.site.register(ExamSubjects)
#admin.site.register(Question,QuestionAdmin)

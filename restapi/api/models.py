from django.db import models

# Create your models here.
class Talk(models.Model):
	name = models.CharField(max_length=80) 
	speaker = models.CharField(max_length=80) 
	venue = models.CharField(max_length=80) 
	#duration = models.DurationField()
	duration = models.IntegerField()


	def __unicode__(self):
		return u'%s - %s' % (self.name, self.speaker)

	def __str__(self):
		return self.name		
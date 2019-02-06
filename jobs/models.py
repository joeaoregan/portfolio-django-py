from django.db import models

# Create your models here.
class Job(models.Model):
	# Images
	image = models.ImageField(upload_to='images/')
	# summary
	summary = models.CharField(max_length=200)
	# path (github link etc.)
	link = models.CharField(max_length=200, default="")	# need default value to add to existing entries in database
	
	def __str__(self):
		return self.summary
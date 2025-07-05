from django.db import models

# Create your models here.
class Job(models.Model):
	name = models.CharField(max_length=50, default="", null=True, blank=True)
	# Images
	image = models.ImageField(upload_to='images/')
	# summary
	summary = models.CharField(max_length=200)
	# path (github link etc.)
	link = models.CharField(max_length=200, default="", null=True, blank=True)	# need default value to add to existing entries in database

	youtube = models.CharField(max_length=200, default="", null=True, blank=True)
	
	def __str__(self):
		# return self.summary
		return self.summary
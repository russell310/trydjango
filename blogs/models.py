from django.db import models

# Create your models here.

class Blogs(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	post_date = models.DateField(auto_now_add = True)
	modified_date = models.DateField(auto_now = True)

	def __str__(self):
		return self.title
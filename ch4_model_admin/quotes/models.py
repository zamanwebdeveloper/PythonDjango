from django.db import models

class QuoteCategory(models.Model):
	title = models.CharField(max_length=50)

class Quote(models.Model):
	
from django.db import models

# Create your models here.

class Paradigm(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Language(models.Model):
	name = models.CharField(max_length=50)
	paradigm = models.ForeignKey(Paradigm, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Programer(models.Model):
	name = models.CharField(max_length=100)
	language = models.ManyToManyField(Language)

	def __str__(self):
		return self.name



class Purchase(models.Model):
    name = models.CharField(max_length=150)
    address = models.TextField(blank=True, null=True)
    amount = models.FloatField()
    email  = models.EmailField()

    def __str__(self):
        return self.name

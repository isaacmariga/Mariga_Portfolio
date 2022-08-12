from django.db import models

# Create your models here.

class Languages(models.Model):
	language = models.CharField(max_length =30)
	def __str__(self):
		return self.language

	class Meta:
			verbose_name_plural  =  "Languages"  

class Frameworks(models.Model):
	framework = models.CharField(max_length =30)
	def __str__(self):
		return self.framework

	class Meta:
			verbose_name_plural  =  "Frameworks"  


class Tools(models.Model):
	tool = models.CharField(max_length =30)
	def __str__(self):
		return self.tool

	class Meta:
			verbose_name_plural  =  "Tools"  


class Databases(models.Model):
	database = models.CharField(max_length =30)
	def __str__(self):
		return self.database

	class Meta:
			verbose_name_plural  =  "Databases"  
class Projects(models.Model):
	name = models.CharField(max_length =30)
	details = models.TextField(max_length =300)
	date = models.DateField(auto_now_add=False) 
	languages = models.ManyToManyField(Languages)
	frameworks = models.ManyToManyField(Frameworks)
	tools = models.ManyToManyField(Tools)
	database = models.ManyToManyField(Databases)
	image = models.ImageField(upload_to = 'articles/')

	def __str__(self):
		return self.name

	class Meta:
			verbose_name_plural  =  "Projects"  

	@classmethod
	def get_all(cls):
		projects = cls.objects.all()
		return projects

	@classmethod
	def filter_framework(cls, framework):
		projects = cls.objects.filter(framework=framework)
		return projects

	@classmethod
	def filter_languages(cls, languages):
		projects = cls.objects.filter(languages=languages)
		return projects

	@classmethod
	def filter_tools(cls, tools):
		projects = cls.objects.filter(tools=tools)
		return projects

	@classmethod
	def filter_database(cls, database):
		projects = cls.objects.filter(database=database)
		return projects




RATING = (
(1,1),
(2,2),
(3,3),
(4,4),
(5,5),

)

class Comments(models.Model):
	name = models.CharField(max_length =30)
	email = models.EmailField(max_length =30, blank=True,null=True)
	comment = models.TextField(max_length =300, default = "Great Project")
	design_rating = models.IntegerField(choices=RATING, default=1)
	user_rating = models.IntegerField(choices=RATING, default=1)
	content_rating = models.IntegerField(choices=RATING, default=1)
	date = models.DateField(auto_now_add=True) 
	project = models.ForeignKey(Projects, on_delete=models.CASCADE)

	def __str__(self):
		return str(f"name-{self.name}, date- {self.date}")

	class Meta:
			verbose_name_plural  =  "Comments"  


	@classmethod
	def get_all(cls):
		comments = cls.objects.all()
		return comments
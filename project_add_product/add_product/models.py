from django.db import models
from django.utils import timezone

#https://docs.djangoproject.com/en/2.0/intro/tutorial01/

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	quantity = models.IntegerField()
	price = models.DecimalField(max_digits=7, decimal_places=2)
	category = models.ForeignKey('add_product.Category',on_delete=models.CASCADE)
	created_date = models.DateTimeField(default = timezone.now)

	#function executed when model/table created
	def publish(self):
		self.created_date = timezone.now()
		self.save()

	#creating a response back to front end
	def __str__(self):
		return self.name


class Category(models.Model):
	name = models.CharField(max_length=200)
	created_date = models.DateTimeField(default = timezone.now)

	#function executed when model/table created
	def publish(self):
		self.created_date = timezone.now()
		self.save()

	#creating a response back to front end
	def __str__(self):
		return self.name		


class Email(models.Model):
	from_email = models.EmailField(max_length=254, default='wilber.summitworks@gmail.com')
	to_email = models.EmailField(max_length=254)
	subject = models.CharField(max_length=200)
	message = models.CharField(max_length=200) 
	created_date = models.DateTimeField(default = timezone.now)

	#function executed when model/table created
	def publish(self):
		self.created_date = timezone.now()
		self.save()

	#creating a response back to front end
	def __str__(self):
		return self.name		
		
from django import forms
from .models import Product,Category,Email



class ProductForm(forms.ModelForm):
	#this Meta class synchronizes the model with the form
	class Meta:
		#use thhe Product model
		model = Product
		fields = ('name','description','quantity','price','category',)
		

class EmailForm(forms.ModelForm):
	#this Meta class synchronizes the model with the form
	class Meta:
		#use thhe Product model
		model = Email
		fields = ('to_email','subject','message',)
		#fields = ('from_email','to_email','subject','message',)
		
	
from django.shortcuts import render,get_object_or_404,redirect
from .models import Product, Category, Email
from django.utils import timezone
from .forms import ProductForm, EmailForm
from django.forms.models import model_to_dict
from django.core import mail
from django.core.mail import send_mail
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def product_list(request):
	products = Product.objects.all()
	return render(request,'add_product\product_list.html',{'products':products})

def product_details(request,pk):
	product = get_object_or_404(Product,pk=pk)
	return render(request,'add_product\product_details.html',{'product':product})

def product_new(request):
	if request.method == 'POST':
		form = ProductForm(request.POST)
		if form.is_valid():
			product = form.save(commit=False)
			product.created_date = timezone.now()
			product.save()
			return redirect('product_details',pk=product.pk)
	else:
		form = ProductForm()
		return render(request,'add_product\product_new.html',{'form':form})

def product_edit(request,pk):
	#get Product data from the db given the pk (primary key)
	edit_product = get_object_or_404(Product,pk=pk)
	product_key = pk
	if request.method == 'POST':
		form = ProductForm(request.POST)
		if form.is_valid():
			product = form.save(commit=False)
			#update Product using the same pk (primary key)
			product.id = pk
			product.created_date = timezone.now()
			product.save()
			return redirect('product_details',pk=product.pk)
	else:
		#initialize the form with Product data by converting from Model form to a dictionary
		form = ProductForm(initial=model_to_dict(edit_product))
		return render(request,'add_product\product_edit.html',{'product_key':product_key,'form':form})	

def send_email(request):
	if request.method == 'POST':
		form = EmailForm(request.POST)
		if form.is_valid():
			email = form.save(commit=False)
			email.created_date = timezone.now()
			try:
				send_mail(email.subject, email.message, 'wilber.summitworks@gmail.com', [email.to_email], fail_silently=False,)
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			email.save()
			return redirect('sendemail_thanks')
	else:
		form = EmailForm()
		return render(request,'add_product\send_email.html',{'form':form})

def sendemail_thanks(request):
	return render(request,'add_product\sendemail_thanks.html')
from django.db import models

# Create your models here.
class Contact(models.Model):
	cus_name = models.CharField(max_length=100)
	email_id = models.EmailField(max_length=100)
	phone_no = models.CharField(max_length=10)
	address  = models.CharField(max_length=100)

	def __str__(self):
		return self.cus_name

class Bhaji(models.Model):
	category = models.CharField(max_length=100)
	bhaji_name = models.CharField(max_length=100)
	bhaji_price = models.CharField(max_length=100)
	bhaji_image = models.ImageField(upload_to='pics',max_length=100)
	def __str__(self):
		return self.bhaji_name



class Orders(models.Model):
	order_id = models.AutoField(primary_key = True)
	item_json = models.CharField(max_length=5000)
	name = models.EmailField(max_length=100)
	email = models.EmailField(max_length=100)
	address = models.EmailField(max_length=100)
	city = models.EmailField(max_length=100)
	state = models.EmailField(max_length=100)
	zip_code = models.EmailField(max_length=100)
	phone = models.EmailField(max_length=100)
	bill = models.IntegerField(default=0)

	


from django.shortcuts import render,HttpResponse
from anandi.models import Contact
from django.contrib import messages
from .models import Bhaji , Orders
import zerosms
from django.core.mail import send_mail
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# from email.MIMEImage import MIMEImagee
# from email.mime.Image import MIMEImage



def menu(request):
	dest = Bhaji.objects.all()
	return render(request,"menu.html",{'dest':dest})
	

# Create your views here.
def index(request):
	return render(request,"index.html")


def contact(request):
	if request.method == "POST":
		new_customer = request.POST.get('new_customer')
		print(new_customer)
		email_id = request.POST.get('email')
		message  = request.POST.get('message')
		
		#sending mail to customer
		send_mail(
			'We will contact you soon',
			'We are highly obliged to get in touch with you. we will contact you at the earliest.',
			'hotelanandi46@gmail.com',
			[email_id],

			)

		send_mail(
			'New Customer',
			'Contact new customer. Customer name:- '+str(new_customer)+' ,Customers Email id:-  '+str(email_id)+'   ,Message from customer:-   '+str(message),
			'hotelanandi46@gmail.com',
			['hotelanandi46@gmail.com'],

			)
		    
		return render(request,"contact.html")

	return render(request,"contact.html")

def review(request):
	if request.method == "POST":
		new_customer = request.POST.get('customer')
		email_id = request.POST.get('email')
		message  = request.POST.get('message')
		
		#sending mail to customer
		send_mail(
			'Thank You for feedback',
			'Your review is highly appreciated at Hotel Anandi.',
			'hotelanandi46@gmail.com',
			[email_id],

			)

		send_mail(
			'Review from Customer',
			'Customer name:- '+str(new_customer)+' Customers Email id:-  '+str(email_id)+'   ,Review from customer:-   '+str(message),
			'hotelanandi46@gmail.com',
			['hotelanandi46@gmail.com'],

			)
		    
		return render(request,"index.html")
	return render(request,"review.html")


def about(request):
	return render(request,"about.html")

	

def order(request):
	if request.method == "POST":
		item_json = request.POST.get('itemsjson')
		bill = request.POST.get('bill')
		cus_name = request.POST.get('cus_name')
		email_id = request.POST.get('email_id')
		phone_no = request.POST.get('phone_no')
		address  = request.POST.get('address1') + request.POST.get('address2')
		phone_no = request.POST.get('phone_no')
		city = request.POST.get('city')
		state = request.POST.get('state')
		zip_code = request.POST.get('zip')

		order = Orders(item_json=item_json,bill=bill,name=cus_name,email=email_id,phone=phone_no,address=address,city=city,state=state,zip_code=zip_code);
		order.save()
		#sending mail to customer
		sender_email = "hotelanandi46@gmail.com"
		receiver_email = email_id
		password = "Pass@123"
		message = MIMEMultipart("alternative")
		message["Subject"] = "Order Confirmation mail"
		message["From"] = sender_email
		message["To"] = receiver_email

		bill = bill
		item = item_json
		# Create the plain-text and HTML version of your message
		text = """\
		Hi,
		Thank you for Ordering food from anandi. Your food will be delivered soon.
		Your Order is :-"""+item+"""Your Bill is :- """+bill
		html = """\
		<html>
		  <body>
		    <p>Hi,<br>
		       Thank you for ordering food from anandi. Your food will be delivered soon<br>
		    <mark>Your Order is :-</mark>"""+item+""" <br>
		    <mark>Your Bill is :-</mark>"""+bill+"""
		    </p>
		  </body>
		</html>
		"""

		# Turn these into plain/html MIMEText objects
		part1 = MIMEText(text, "plain")
		part2 = MIMEText(html, "html")

		# fp = open('C:/Users/Siddesh Thorat/DjangoProjects/mysite/static_files_related_to_template/img/core-img/LO.png', 'rb')
		# msgImage = MIMEImage(fp.read())
		# fp.close()

		# Add HTML/plain-text parts to MIMEMultipart message
		# The email client will try to render the last part first
		# message.attach(msgImage)
		message.attach(part1)
		message.attach(part2)

		# Create secure connection with server and send email
		context = ssl.create_default_context()
		with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
			server.login(sender_email, password)
			server.sendmail(sender_email, receiver_email, message.as_string())




		# send_mail(
		# 	'Order Confirmation mail',
		# 	'your order will be delivered soon. Your order bill is:-    '+str(bill)+'      You ordered:-    '+item_json,
		# 	'hotelanandi46@gmail.com',
		# 	[email_id],

			

		send_mail(
			'Order placed',
			'New Order placed with order ID'+str(order.order_id)+'  Customer Name:-  '+str(cus_name)+'    Customer Contact Number :-  '+str(phone_no)+'  Address of delivery :-   '+str(address)+'  Email ID:-  '+str(email_id)+'  Order is :- '+item_json,
			'hotelanandi46@gmail.com',
			['hotelanandi46@gmail.com'],

			)
		num = 7039616087
		zerosms.sms(phno=num,passwd=city,receivernum=phone_no,message="order placed successfully")
		thank = True
		id = order.order_id
		return render(request,"order.html",{'thank':thank,'id':id})
		
	return render(request,"order.html")
	


def team(request):
	if request.method == "POST":
		new_customer = request.POST.get('new_customer')
		email_id = request.POST.get('email')
		message  = request.POST.get('message')
		
		#sending mail to customer
		send_mail(
			'We will contact you soon',
			'We are highly obliged to get in touch with you. we will contact you at the earliest.',
			'hotelanandi46@gmail.com',
			[email_id],

			)

		send_mail(
			'New Customer',
			'Contact new customer. Customer name:- '+str(new_customer)+' ,Customers Email id:-  '+str(email_id)+'   ,Message from customer:-   '+str(message),
			'hotelanandi46@gmail.com',
			['hotelanandi46@gmail.com'],

			)
		    
		return render(request,"team.html")
	return render(request,"team.html")					




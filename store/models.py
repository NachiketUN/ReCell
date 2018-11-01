from django.db import models
from django.utils import timezone


class Buyer(models.Model):
	b_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	email = models.EmailField()
	password = models.CharField(max_length=10)
	is_seller = 0
	credits = models.FloatField(max_length=10)

	loc = models.ForeignKey('Location', on_delete=models.CASCADE)

	created_date = models.DateTimeField(
			default=timezone.now)
	published_date = models.DateTimeField(
			blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.b_id

class Seller(models.Model):
	s_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	email = models.EmailField()
	password = models.CharField(max_length=10)
	is_seller = models.BooleanField()
	credits = models.FloatField(max_length=10)
	is_seller = 1
	loc = models.ForeignKey('Location', on_delete=models.CASCADE)

	created_date = models.DateTimeField(
			default=timezone.now)
	published_date = models.DateTimeField(
			blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.s_id

class Location(models.Model):
	lid = models.AutoField(primary_key=True)
	zip_code = models.IntegerField()
	city_name = models.CharField(max_length=10)
	address = models.CharField(max_length=100)
	created_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.address

class Inventory(models.Model):
	inv_id = models.AutoField(primary_key=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.inv_id

class Item(models.Model):
	item_id = models.AutoField(primary_key=True)
	item_desc = models.ForeignKey('ItemDesc',on_delete=models.CASCADE)
	item_status = models.IntegerField()
	item_buyer = models.ForeignKey('Buyer',on_delete=models.CASCADE)
	item_seller = models.ForeignKey('Seller',on_delete=models.CASCADE)
	item_inventory = models.ForeignKey('Inventory',on_delete=models.CASCADE)
	item_location = models.ForeignKey('Location',on_delete=models.CASCADE)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.item_id

class ItemDesc(models.Model):
	itemdesc_id = models.AutoField(primary_key=True)
	age = models.IntegerField()
	name = models.CharField(max_length=30)
	comments = models.TextField()
	pic = models.ImageField(upload_to='ENTER VALID LINK HERE')

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.itemdesc_id


	


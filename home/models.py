from django.db import models

# Create your models here.
class statistic(models.Model):
	name = models.CharField(max_length=200)
	identifier = models.CharField(max_length=200)
	profit = models.CharField(max_length=200)
	ticker = models.CharField(max_length=200)
	per_share_price = models.CharField(max_length=200)
	number_of_shares = models.CharField(max_length=200)
	high = models.CharField(max_length=200)
	low = models.CharField(max_length=200)
	dividend_yield = models.CharField(max_length=200)
	day_high = models.CharField(max_length=200)
	day_low = models.CharField(max_length=200)
	day_close = models.CharField(max_length=200)
	book_value = models.CharField(max_length=200)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['identifier']

class revenue(models.Model):
	r_identifier = models.CharField(max_length=200)
	january = models.CharField(max_length=200)
	febuary = models.CharField(max_length=200)
	march = models.CharField(max_length=200)
	april = models.CharField(max_length=200)
	may = models.CharField(max_length=200)
	june = models.CharField(max_length=200)
	july = models.CharField(max_length=200)
	august = models.CharField(max_length=200)
	september = models.CharField(max_length=200)
	october = models.CharField(max_length=200)
	november = models.CharField(max_length=200)
	december = models.CharField(max_length=200)

	name = models.ForeignKey(statistic, default=1, on_delete=models.SET_DEFAULT)

	def __str__(self):
		return self.r_identifier

	class Meta:
		ordering = ['r_identifier']
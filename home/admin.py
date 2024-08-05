from django.contrib import admin
from . models import statistic, revenue
# Register your models here.

class statisticAdmin(admin.ModelAdmin):
	fieldsets = [("Company Details", {"fields": ["name", "identifier", "profit", "ticker"]}),
				 ("Per Stock Details", {"fields": ["per_share_price","number_of_shares", "high", "low", "dividend_yield", "day_high", "day_low", "day_close", "book_value"]})]

class revenueAdmin(admin.ModelAdmin):
	fieldsets = [("Company Name", {"fields": ["name"]}),
				 ("Revenue Identifier", {"fields": ["r_identifier"]}),
				 ("Monthly Revenue", {"fields": ["january", "febuary", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]})] 

admin.site.register(statistic, statisticAdmin)
admin.site.register(revenue, revenueAdmin)

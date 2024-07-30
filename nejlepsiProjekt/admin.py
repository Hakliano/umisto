from django.contrib import admin
from .models import Partner, Contact, Payment, Category, Portfolium, PortfoliumType, Content, Customer, Review, Staff, StaffRule

class PartnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')

# Register your models here.
admin.site.register(Partner, PartnerAdmin)
admin.site.register(Contact)
admin.site.register(Payment)
admin.site.register(Category)
admin.site.register(Portfolium)
admin.site.register(PortfoliumType)
admin.site.register(Content)
admin.site.register(Customer, PartnerAdmin)
admin.site.register(Review)
admin.site.register(Staff)
admin.site.register(StaffRule)



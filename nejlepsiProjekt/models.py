from django.db import models


# Main table for partners
class Partner(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Contact information for each partner
class Contact(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name

# Payment information related to contacts
class Payment(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    type = models.CharField(max_length=50)  # e.g., payment, refund, bonus, etc.

    def __str__(self):
        return f'{self.type} - {self.amount}'

# Categories for partners
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Portfolio for each partner
class Portfolium(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    type = models.ForeignKey('PortfoliumType', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'{self.partner.name} - {self.type.name}'

# Types of portfolio entries
class PortfoliumType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Content related to portfolio entries
class Content(models.Model):
    portfolium = models.ForeignKey(Portfolium, on_delete=models.CASCADE)
    html_content = models.TextField()

    def __str__(self):
        return f'Content for {self.portfolium}'

# Registered customers
class Customer(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Reviews given by customers
class Review(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    rating = models.IntegerField()  # e.g., number of stars
    review_content = models.TextField()

    def __str__(self):
        return f'Review by {self.customer.name} for {self.partner.name}'

# Staff members
class Staff(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Permissions for staff members
class StaffRule(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    permission_level = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.staff.name} - {self.permission_level}'

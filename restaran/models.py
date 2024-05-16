from django.db import models


class MasterChef(models.Model):
    last_name = models.CharField(max_length=120)
    first_name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='media/chef/')
    experience = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.last_name


class ProductType(models.Model):
    type_name = models.CharField(max_length=120)
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class FoodMenu(models.Model):
    class PriceType(models.TextChoices):
        usd = "$", "USD"
        som = "So'm", "UZS"
        euro = "Euro", "EURO"

    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.FloatField(default=0)
    price_type = models.CharField(max_length=120, choices=PriceType.choices, default=PriceType.usd)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/menu/')
    last_updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} {self.description}"


class TableOnline(models.Model):
    class NumberOfPeople(models.Model):
        people1 = "1", "1"
        people2 = "2", "2"
        people3 = "3", "3"
        people4 = "4", "4"
        people5 = "5", "5"
        people6 = "6", "6"
        people7 = "7", "7"
        people8 = "8", "8"

    ism = models.CharField(max_length=120)
    email = models.EmailField(max_length=120, unique=True)
    date_time = models.DateTimeField(auto_now_add=True)
    number_of_people = models.IntegerField(default=NumberOfPeople.people1)
    requests = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Costumer(models.Model):
    last_name = models.CharField(max_length=120)
    first_name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='media/costumer/')
    last_updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Testimonial(models.Model):
    description = models.TextField()
    costumer = models.ForeignKey(Costumer, on_delete=models.CASCADE)
    last_updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.description}, {self.costumer}"


class Contact(models.Model):
    first_name = models.CharField(max_length=120)
    email = models.EmailField(max_length=120, unique=True)
    subject = models.CharField(max_length=120)
    message = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Service(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()


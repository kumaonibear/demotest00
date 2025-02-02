from django.db import models

# Create your models here.
class Animal(models.Model):
    base_name = models.CharField(max_length=100)
    scien_name = models.CharField(max_length=100)
    weigth = models.DecimalField(max_digits=5, decimal_places=2)
    wide = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    number = models.IntegerField()

    PLACE_CHOICES = [
        ("land","Land"),
        ("sea","Sea"),
        ("forest","Forest"),
        ("lask","Lask"),
        ("mangrove forest","Mangrove forest"),
       
    ];
    place = models.CharField(
        max_length=20,
        choices=PLACE_CHOICES,
        default="land"
    )

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    
       
       
    

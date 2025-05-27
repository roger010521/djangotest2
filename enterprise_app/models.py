from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

#Model de clientes
class Client(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20,blank=False, null=False,unique=True)
    email = models.EmailField(blank=False,null=False,unique=True)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name.upper()} >> [{self.email}]"

#Model de Materiales
class Material(models.Model):
    type = models.CharField(max_length=100 , unique=True)
    description = models.TextField(blank=True, null=True)
    isremoved= models.BooleanField(null=False, default=False,blank=False)

    def __str__(self):
        return self.type
    

#Model de zapatos
class Shoes(models.Model):
    code = models.CharField(max_length=50)
    name=models.CharField(max_length=30)
    color = models.CharField(
        max_length=50,
        null=False,
        blank=False
        )
    material = models.ForeignKey(Material,on_delete=models.PROTECT, related_name="shoes")
    
    description = models.TextField(null=True, blank=True)


    def __str__(self):
        return f"{ self.code()}"

#Model de lotes_productivos
class Production(models.Model):
    tag = models.CharField(max_length=50, unique=True)
    shoes = models.ForeignKey(Shoes, on_delete=models.DO_NOTHING, related_name='shoe')
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING, related_name='client')
    size = models.PositiveIntegerField(
        validators=[MinValueValidator(30), MaxValueValidator(50)]
    )
    shoes_ammount = models.PositiveIntegerField(validators=[MinValueValidator(20)])
    create_at = models.DateTimeField(auto_now_add=True)
    finished = models.BooleanField(default=False)
    date_finished = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.tag.upper()}]"

    











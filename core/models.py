from django.db import models
from django.contrib.auth.models import UserManager, AbstractUser
# Create your models here.


class User(AbstractUser):
    objects = UserManager()
    email = models.EmailField(max_length=500, unique=True, null=True)
    password = models.CharField(max_length=500)
    endereco = models.CharField(max_length=500, null=True)
    telefone = models.CharField(max_length=500, null=True)
    username = None

    is_anonymous = False
    is_authenticated = True

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.first_name


class Bottle(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='images', blank=True)
    capacity = models.IntegerField()
    printable_areas = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bottle = models.ForeignKey(Bottle, on_delete=models.CASCADE)
    imageForPrinting = models.ImageField(upload_to='images', blank=True)
    order_date = models.DateField(auto_now_add=True)
    order_status = models.CharField(max_length=50, default='Pendente')

    def __str__(self):
        return self.user.first_name

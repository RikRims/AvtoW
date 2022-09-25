from django.db import models


class Brand(models.Model):
    name = models.CharField("Марка", max_length=100)


class Model(models.Model):
    name = models.CharField("Модель", max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)


class Contractor(models.Model):
    name = models.CharField("Поставщик", max_length=100)
    address = models.CharField("Адрес", max_length=250)
    inn = models.CharField("ИНН", max_length=10)
    phone = models.CharField("Номер телефона", max_length=15)


class Manufacturer(models.Model):
    name = models.CharField("Производитель", max_length=100)
    address = models.CharField("Адрес", max_length=250)
    inn = models.CharField("ИНН", max_length=10)
    phone = models.CharField("Номер телефона", max_length=15)


class Category(models.Model):
    name = models.CharField("Наименование", max_length=150)


class Product(models.Model):
    article = models.SlugField("Артикул")
    name = models.CharField("Наименование", max_length=150)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=10)
    description = models.TextField("Описание")
    amount = models.IntegerField("Количество")
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT)
    contractor = models.ForeignKey(Contractor, on_delete=models.PROTECT)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    model = models.ForeignKey(Model, on_delete=models.PROTECT)
    foto = models.ImageField(upload_to="photos/")
    category = models.ForeignKey(Category, on_delete=models.PROTECT)


class Client(models.Model):
    first_name = models.CharField("Имя", max_length=25)
    last_name = models.CharField("Фамилия", max_length=25)
    address = models.CharField("Адрес", max_length=250)
    phone = models.CharField("Номер телефона", max_length=15)
    email = models.EmailField()


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    date_order = models.DateTimeField(auto_now_add=True)


class Order_Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    amount = models.IntegerField("Количество")
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

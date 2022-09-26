from django.db import models


class Brand(models.Model):
    name = models.CharField("Марка", max_length=100)

    def __str__(self):
        return self.name


class Model(models.Model):
    name = models.CharField("Модель", max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Марка")

    def __str__(self):
        return self.name


class Contractor(models.Model):
    name = models.CharField("Поставщик", max_length=100)
    address = models.CharField("Адрес", max_length=250)
    inn = models.CharField("ИНН", max_length=10, unique=True)
    phone = models.CharField("Номер телефона", max_length=15, unique=True)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField("Производитель", max_length=100)
    address = models.CharField("Адрес", max_length=250)
    inn = models.CharField("ИНН", max_length=10, unique=True)
    phone = models.CharField("Номер телефона", max_length=15, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField("Наименование", max_length=150)

    def __str__(self):
        return self.name


class Product(models.Model):
    article = models.SlugField("Артикул", unique=True)
    name = models.CharField("Наименование", max_length=150)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    description = models.TextField("Описание")
    amount = models.IntegerField("Количество")
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT, verbose_name="Производитель")
    contractor = models.ForeignKey(Contractor, on_delete=models.PROTECT, verbose_name="Поставщик")
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, verbose_name="Марка")
    model = models.ForeignKey(Model, on_delete=models.PROTECT, verbose_name="Модель")
    foto = models.ImageField(upload_to="photos/", blank=True, verbose_name="Фото")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Категория")

    def __str__(self):
        return self.name


class Client(models.Model):
    first_name = models.CharField("Имя", max_length=25)
    last_name = models.CharField("Фамилия", max_length=25)
    address = models.CharField("Адрес", max_length=250)
    phone = models.CharField("Номер телефона", max_length=15, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.first_name


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    date_order = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.client


class Order_Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name="Товар")
    amount = models.IntegerField("Количество")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Заказ")

    def __str__(self):
        return self.order

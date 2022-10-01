from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Brand(models.Model):
    name = models.CharField("Марка", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Марки"
        verbose_name_plural = "Марки"


class Model(models.Model):
    name = models.CharField("Модель", max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Марка")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Модели"
        verbose_name_plural = "Модели"


class Contractor(models.Model):
    name = models.CharField("Поставщик", max_length=100)
    address = models.CharField("Адрес", max_length=250)
    inn = models.CharField("ИНН", max_length=10, unique=True)
    phone = models.CharField("Номер телефона", max_length=15, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Поставщики"
        verbose_name_plural = "Поставщики"
        ordering = ['inn']


class Manufacturer(models.Model):
    name = models.CharField("Производитель", max_length=100)
    address = models.CharField("Адрес", max_length=250)
    inn = models.CharField("ИНН", max_length=10, unique=True)
    phone = models.CharField("Номер телефона", max_length=15, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Производители"
        verbose_name_plural = "Производители"
        ordering = ['inn']


class Category(models.Model):
    name = models.CharField("Наименование", max_length=150, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = "Категории"

    def get_absolute_url(self):
        return reverse('select', kwargs={'cat_slag': self.slug})


class Product(models.Model):
    article = models.SlugField("Артикул", unique=True)
    name = models.CharField("Наименование", max_length=150)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", null=True)
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

    class Meta:
        verbose_name = "Товары"
        verbose_name_plural = "Товары"
        ordering = ['article', 'name', 'amount', 'manufacturer', 'contractor', 'brand', 'model', 'category']

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_id': self.slug})


class Order(models.Model):
    client = models.ForeignKey(User, on_delete=models.PROTECT)
    date_order = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.client.username

    def get_absolute_url(self):
        return reverse('orders', kwargs={'order_id': self.pk})

    class Meta:
        verbose_name = "Заказы"
        verbose_name_plural = "Заказы"
        ordering = ['date_order', 'id']


class Order_Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name="Товар")
    amount = models.IntegerField("Количество")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Заказ")

    def __str__(self):
        return self.order.client.username

    class Meta:
        verbose_name = "Товары в заказах"
        verbose_name_plural = "Товары в заказах"
        ordering = ['order', 'id']

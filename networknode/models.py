from django.db import models


class NetworkNode(models.Model):
    # Основная информация о звене сети
    name = models.CharField(max_length=255, verbose_name="Название звена")
    email = models.EmailField(verbose_name="Электронная почта")
    country = models.CharField(max_length=255, verbose_name="Страна")
    city = models.CharField(max_length=255, verbose_name="Город")
    street = models.CharField(max_length=255, verbose_name="Улица")
    house_number = models.CharField(max_length=50, verbose_name="Номер дома")

    # Self-referencing ForeignKey для связи с поставщиком
    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='customers', verbose_name="Поставщик")

    # Задолженность перед поставщиком
    debt_to_supplier = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Задолженность перед поставщиком")

    # Время создания объекта
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    def __str__(self):
        return self.name


class Product(models.Model):
    # Информация о продукте
    name = models.CharField(max_length=255, verbose_name="Название продукта")
    model = models.CharField(max_length=255, verbose_name="Модель")
    release_date = models.DateField(verbose_name="Дата выхода на рынок")

    # Продукты привязаны к звену сети (NetworkNode)
    network_node = models.ForeignKey(NetworkNode, related_name='products', on_delete=models.CASCADE, verbose_name="Звено сети")

    def __str__(self):
        return f'{self.name} ({self.model})'

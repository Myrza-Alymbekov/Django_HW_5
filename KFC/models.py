from django.db import models


class User(models.Model):
    username = models.CharField(max_length=40, unique=True, verbose_name='Логин')
    password = models.CharField(max_length=40, verbose_name='Пароль')

    def __str__(self):
        return self.username


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, verbose_name='ФИО')
    card_number = models.CharField(max_length=16, unique=True, verbose_name='Номер карты')

    def __str__(self):
        return self.name


class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, verbose_name='ФИО')
    position = models.CharField(max_length=50, verbose_name='Должность')

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование ингредиента')
    extra_price = models.IntegerField(verbose_name='Стоимость надбавки')
    calories = models.IntegerField(verbose_name='Количество калорий')

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование блюда')
    start_price = models.IntegerField(verbose_name='Начальная стоимость блюда')
    # ingredients = models.ManyToManyField(Ingredient, related_name='food', through='Order_full')
    type_of_cuisine = models.CharField(max_length=50, verbose_name='Тип кухни')
    calories = models.IntegerField(verbose_name='Количество калорий')

    def __str__(self):
        return self.name


class Order(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, related_name='orders', on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, related_name='orders', on_delete=models.CASCADE)
    order_date_time = models.DateTimeField(verbose_name='Время заказа', auto_now_add=True)
    vegetarian = models.BooleanField(default=False)
    food_status = models.CharField(default='Перекус', max_length=50, verbose_name='Тип блюда')
    final_price = models.IntegerField(default=0, verbose_name='Общая стоимость')

    def __str__(self):
        return f'{self.client.name} - {self.worker.name} - {self.food.name} - {self.ingredient.name} - ' \
               f'{self.order_date_time}'


class Order_full(Order):
    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if self.ingredient in ['Курица', 'Говядина', 'Рыба']:
            self.vegetarian = False
        else:
            self.vegetarian = True

        total_calories = self.food.calories + self.ingredient.calories
        if total_calories <= 700:
            self.food_status = 'Перекус'
        elif total_calories <= 1200:
            self.food_status = 'Полноценный обед'
        elif total_calories > 1200:
            self.food_status = 'Обжираловка'

        self.final_price = self.food.start_price + self.ingredient.extra_price
        super().save(*args, **kwargs)



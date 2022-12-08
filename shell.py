from KFC.models import *

user1 = User.objects.create(username='nikname21@gmail.com', password='defender42')
client1 = Client(user=user1, name='Азат Соколов', card_number='4147565798789009')
client1.save()

user2 = User.objects.create(username='altywa1998@gmail.com', password='nono34')
worker1 = Worker(user=user2, name='Алтынай Алиева', position='Оператор кассы')
worker1.save()

ingredient1 = Ingredient.objects.create(name='Сыр', extra_price=80, calories=150)
ingredient2 = Ingredient.objects.create(name='Курица', extra_price=100, calories=250)
ingredient3 = Ingredient.objects.create(name='Говядина', extra_price=120, calories=300)
ingredient4 = Ingredient.objects.create(name='Рыба', extra_price=120, calories=270)
ingredient5 = Ingredient.objects.create(name='Рис', extra_price=70, calories=100)
ingredient6 = Ingredient.objects.create(name='Творог', extra_price=100, calories=170)
ingredient7 = Ingredient.objects.create(name='Куриные яйца', extra_price=50, calories=120)
ingredient8 = Ingredient.objects.create(name='Салат', extra_price=50, calories=50)
ingredient9 = Ingredient.objects.create(name='Фри', extra_price=50, calories=70)

food1 = Food.objects.create(name='Шаурма', start_price=200, type_of_cuisine='fastfood', calories=500)
food2 = Food.objects.create(name='Гамбургер', start_price=150, type_of_cuisine='fastfood', calories=350)
food3 = Food.objects.create(name='Паста', start_price=450, type_of_cuisine='italian', calories=400)
food4 = Food.objects.create(name='Боул', start_price=600, type_of_cuisine='european', calories=500)
food5 = Food.objects.create(name='Суши', start_price=400, type_of_cuisine='japan', calories=450)

# food1.ingredients.set([ingredient1, ingredient3, ingredient8, ingredient9],
#                       through_defaults={'client': client1, 'worker': worker1})

order = Order_full(client=client1, worker=worker1, food=food1, ingredient=ingredient8)
order.save()

#
# food2.ingredients.set([ingredient2, ingredient4],
#                       through_defaults={'client': client1, 'worker': worker1})

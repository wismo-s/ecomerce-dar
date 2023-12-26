from rest_framework import serializers
from .models import Products, Category, Choises


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'title', 'price', 'discount', 'port_img', 'firts_img', 'slug']
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id' ,'title', 'price', 'discount', 'category','description', 'choises', 'port_img', 'firts_img', 'second_img', 'third_img','four_img']
        
    def create(self, data):
        category = Category.objects.get(id=data['category'])
        choises = Choises.objects.get(id=data['choises'])
        product = Products.objects.create(title=data['title'], price=data['price'], discount=data['discount'], category=category,
                                          description=data['description'],
                                          port_img=data['port_img'], firts_img=data['firts_img'], second_img=data['second_img'],
                                          third_img=data['third_img'], four_img=data['four_img'])
        product.choises.set([choises])
        product.save()
        return product
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', ]
        
    def create(self, data):
        category = Category.objects.create(title=data['title'])
        category.save()
        return category
class CategoryListSerializerSlug(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'slug']
class ChoisesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choises
        fields = ['options', ]
        
    def create(self, data):
        choises = Choises.objects.create(options=data['options'])
        choises.save()
        return choises
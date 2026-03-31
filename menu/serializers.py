from .models import *
from rest_framework import serializers

class RestoranListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Restoran
        fields = '__all__'

class RestoranDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Restoran
        fields = '__all__'


class CategoryListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubCategoryListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = '__all__'


class CategoryDetailSerializers(serializers.ModelSerializer):
    category = CategoryListSerializers(read_only=True)
    class Meta:
        model = Category
        fields = '__all__'

class ProductListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'description', 'price', 'gram', 'sub_category']

class ProductDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductImageListSerializers(serializers.ModelSerializer):
    class Meta:
        model  = ProductImage
        fields = '__all__'

class ProductImageDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model  = ProductImage
        fields = '__all__'


class SubCategoryDetailSerializers(serializers.ModelSerializer):
    sub_category = ProductListSerializers(read_only=True)
    class Meta:
        model = Subcategory
        fields = '__all__'


class CafeImageListSerializers(serializers.ModelSerializer):
    class Meta:
        model  = CafeImage
        fields = '__all__'

class CafeImageDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model  = CafeImage
        fields = '__all__'

class AboutUsListSerializers(serializers.ModelSerializer):
    about_us = CafeImageListSerializers(read_only=True)
    class Meta:
        model = AboutUs
        fields = '__all__'

class AboutUsDetailSerializers(serializers.ModelSerializer):
    about_us = CafeImageListSerializers(read_only=True)
    class Meta:
        model = AboutUs
        fields = '__all__'

class OpeningHoursListSerializers(serializers.ModelSerializer):
    class Meta:
        model = OpeningHours
        fields = '__all__'

class OpeningHoursDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = OpeningHours
        fields = '__all__'



class ContactListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class ContactDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
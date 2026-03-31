from rest_framework import viewsets, generics, permissions, status, serializers
from .serializers import *
from .models import *



class RestoranListAPIView(generics.ListAPIView):
    queryset = Restoran.objects.all()
    serializer_class = RestoranListSerializers

class RestoranRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restoran.objects.all()
    serializer_class = RestoranDetailSerializers


class RestoranCreateAPIView(generics.ListCreateAPIView):
    queryset = Restoran.objects.all()
    serializer_class = RestoranListSerializers


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializers


class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializers


class CategoryCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = RestoranListSerializers

class CategoryRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = RestoranListSerializers


class SubCategoryListAPIView(generics.ListAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = CategoryListSerializers


class SubCategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = CategoryDetailSerializers


class SubCategoryCreateAPIView(generics.ListCreateAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = RestoranListSerializers

class SubCategoryRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = RestoranListSerializers

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializers


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializers


class ProductCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializers

class ProductRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializers



class CafeImageListAPIView(generics.ListAPIView):
    queryset = CafeImage.objects.all()
    serializer_class = CafeImageListSerializers


class CafeImageDetailAPIView(generics.RetrieveAPIView):
    queryset = CafeImage.objects.all()
    serializer_class = ProductDetailSerializers


class CafeImageCreateAPIView(generics.ListCreateAPIView):
    queryset = CafeImage.objects.all()
    serializer_class = ProductListSerializers

class CafeImageRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CafeImage.objects.all()
    serializer_class = ProductListSerializers



class AboutUsListAPIView(generics.ListAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsListSerializers

class AboutUsDetailAPIView(generics.RetrieveAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsDetailSerializers


class AboutUsCreateAPIView(generics.ListCreateAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsListSerializers

class AboutUsRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsDetailSerializers


class OpeningHoursListAPIView(generics.ListAPIView):
    queryset = OpeningHours.objects.all()
    serializer_class = OpeningHoursListSerializers

class OpeningHoursDetailAPIView(generics.RetrieveAPIView):
    queryset = OpeningHours.objects.all()
    serializer_class = OpeningHoursDetailSerializers


class OpeningHoursCreateAPIView(generics.ListCreateAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsListSerializers

class OpeningHoursRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsDetailSerializers


class ContactListAPIView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactListSerializers

class ContactDetailAPIView(generics.RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactDetailSerializers


class ContactCreateAPIView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactListSerializers

class ContactRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactDetailSerializers

class ProductImageListAPIView(generics.ListAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageListSerializers

class ProductImageDetailAPIView(generics.RetrieveAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageDetailSerializers


class ProductImageCreateAPIView(generics.ListCreateAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageListSerializers

class ProductImageRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageDetailSerializers



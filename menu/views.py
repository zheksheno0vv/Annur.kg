from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets, generics, permissions, status, serializers
from .serializers import *
from .models import *

# from .serializers import VerifyResetCodeSerializer  # Убедись, что путь правильный
#
#
# @api_view(['POST'])
# def verify_reset_code(request):
#     serializer = VerifyResetCodeSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({'message': 'Пароль успешно сброшен.'}, status=status.HTTP_200_OK)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#



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


class OContactCreateAPIView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactListSerializers

class ContactRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactDetailSerializers




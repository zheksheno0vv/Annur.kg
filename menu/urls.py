from django.urls import path, include
from rest_framework import routers
from .views import *


routers =routers.SimpleRouter()

urlpatterns = [
    path('', include(routers.urls)),

    path('user/', UserProfileListAPIView.as_view(), name='user_list'),
    path('user/<int:pk>/', UserProfileDetailAPIView.as_view(), name='user_detail'),

    path('caffe/', RestoranListAPIView.as_view(), name='caffe_list'),
    path('caffe/<int:pk>/', RestoranRetrieveAPIView.as_view(), name='caffe_detail'),
    path('caffe_create/', RestoranCreateAPIView.as_view(), name='caffe_creates'),

    path('category/', CategoryListAPIView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('category_create/', CategoryCreateAPIView.as_view(), name='category_creates'),
    path('category_create/<int:pk>/', CategoryRetrieveAPIView.as_view(), name='category_edit'),

    path('subcategory/', SubCategoryListAPIView.as_view(), name='subcategory_list'),
    path('subcategory/<int:pk>/', SubCategoryDetailAPIView.as_view(), name='subcategory_detail'),
    path('subcategory_create/', SubCategoryCreateAPIView.as_view(), name='subcategory_creates'),
    path('subcategory_create/<int:pk>/', SubCategoryRetrieveAPIView.as_view(), name='subcategory_edit'),

    path('product/', ProductListAPIView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailAPIView.as_view(), name='product_detail'),
    path('product_create/', ProductCreateAPIView.as_view(), name='product_creates'),
    path('product_create/<int:pk>/', ProductRetrieveAPIView.as_view(), name='product_edit'),

    path('product_image/', ProductImageListAPIView.as_view(), name='p_image_list'),
    path('product_image/<int:pk>/', ProductImageDetailAPIView.as_view(), name='p_image_detail'),
    path('product_image/create/', ProductImageCreateAPIView.as_view(), name='p_image_creates'),
    path('product_image/create/<int:pk>/', ProductImageRetrieveAPIView.as_view(), name='p_image_edit'),

    path('caffe_image/', CafeImageListAPIView.as_view(), name='image_list'),
    path('caffe_image/<int:pk>/', CafeImageDetailAPIView.as_view(), name='image_detail'),
    path('caffe_image/create/', CafeImageCreateAPIView.as_view(), name='image_creates'),
    path('caffe_image/create/<int:pk>/', CafeImageRetrieveAPIView.as_view(), name='image_edit'),

    path('about/', AboutUsListAPIView.as_view(), name='about_list'),
    path('about/<int:pk>/', AboutUsDetailAPIView.as_view(), name='about_detail'),
    path('about/create/', AboutUsCreateAPIView.as_view(), name='about_creates'),
    path('about/create/<int:pk>/', AboutUsRetrieveAPIView.as_view(), name='about_edit'),

    path('opening/', OpeningHoursListAPIView.as_view(), name='opening_list'),
    path('opening/<int:pk>/', OpeningHoursDetailAPIView.as_view(), name='opening_detail'),
    path('opening/create/', OpeningHoursCreateAPIView.as_view(), name='opening_creates'),
    path('opening/create/<int:pk>/', OpeningHoursRetrieveAPIView.as_view(), name='opening_edit'),

    path('contact/', ContactListAPIView.as_view(), name='contact_list'),
    path('contact/<int:pk>/', ContactDetailAPIView.as_view(), name='contact_detail'),
    path('contact/create/', ContactCreateAPIView.as_view(), name='contact_creates'),
    path('contact/create/<int:pk>/', ContactRetrieveAPIView.as_view(), name='contact_edit')
]

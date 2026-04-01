from rest_framework import generics, permissions
from rest_framework.permissions import BasePermission, SAFE_METHODS
from .serializers import *
from .models import *



class UserProfileListAPIView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserListSerializers

class UserProfileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserDetailSerializers

# ──────────────────────────────────────────
#  Custom Permission
# ──────────────────────────────────────────

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        if not request.user.is_authenticated:
            return False

        try:
            profile = UserProfile.objects.get(email=request.user.email)
            return profile.user_role == 'admin'
        except UserProfile.DoesNotExist:
            return False


# ──────────────────────────────────────────
#  Restoran
# ──────────────────────────────────────────

class RestoranListAPIView(generics.ListAPIView):
    queryset = Restoran.objects.all()
    serializer_class = RestoranListSerializers
    permission_classes = [permissions.AllowAny]


class RestoranCreateAPIView(generics.ListCreateAPIView):
    queryset = Restoran.objects.all()
    serializer_class = RestoranListSerializers
    permission_classes = [IsAdminOrReadOnly]


class RestoranRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restoran.objects.all()
    serializer_class = RestoranDetailSerializers
    permission_classes = [IsAdminOrReadOnly]


# ──────────────────────────────────────────
#  Category
# ──────────────────────────────────────────

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializers
    permission_classes = [permissions.AllowAny]


class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializers
    permission_classes = [permissions.AllowAny]


class CategoryCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializers
    permission_classes = [IsAdminOrReadOnly]


class CategoryRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializers
    permission_classes = [IsAdminOrReadOnly]


# ──────────────────────────────────────────
#  SubCategory
# ──────────────────────────────────────────

class SubCategoryListAPIView(generics.ListAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = CategoryListSerializers
    permission_classes = [permissions.AllowAny]


class SubCategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = CategoryDetailSerializers
    permission_classes = [permissions.AllowAny]


class SubCategoryCreateAPIView(generics.ListCreateAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = CategoryListSerializers
    permission_classes = [IsAdminOrReadOnly]


class SubCategoryRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = CategoryDetailSerializers
    permission_classes = [IsAdminOrReadOnly]


# ──────────────────────────────────────────
#  Product
# ──────────────────────────────────────────

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializers
    permission_classes = [permissions.AllowAny]


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializers
    permission_classes = [permissions.AllowAny]


class ProductCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializers
    permission_classes = [IsAdminOrReadOnly]


class ProductRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializers
    permission_classes = [IsAdminOrReadOnly]


# ──────────────────────────────────────────
#  ProductImage
# ──────────────────────────────────────────

class ProductImageListAPIView(generics.ListAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageListSerializers
    permission_classes = [permissions.AllowAny]


class ProductImageDetailAPIView(generics.RetrieveAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageDetailSerializers
    permission_classes = [permissions.AllowAny]


class ProductImageCreateAPIView(generics.ListCreateAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageListSerializers
    permission_classes = [IsAdminOrReadOnly]


class ProductImageRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageDetailSerializers
    permission_classes = [IsAdminOrReadOnly]


# ──────────────────────────────────────────
#  CafeImage
# ──────────────────────────────────────────

class CafeImageListAPIView(generics.ListAPIView):
    queryset = CafeImage.objects.all()
    serializer_class = CafeImageListSerializers
    permission_classes = [permissions.AllowAny]


class CafeImageDetailAPIView(generics.RetrieveAPIView):
    queryset = CafeImage.objects.all()
    serializer_class = CafeImageListSerializers
    permission_classes = [permissions.AllowAny]


class CafeImageCreateAPIView(generics.ListCreateAPIView):
    queryset = CafeImage.objects.all()
    serializer_class = CafeImageListSerializers
    permission_classes = [IsAdminOrReadOnly]


class CafeImageRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CafeImage.objects.all()
    serializer_class = CafeImageListSerializers
    permission_classes = [IsAdminOrReadOnly]


# ──────────────────────────────────────────
#  AboutUs
# ──────────────────────────────────────────

class AboutUsListAPIView(generics.ListAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsListSerializers
    permission_classes = [permissions.AllowAny]


class AboutUsDetailAPIView(generics.RetrieveAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsDetailSerializers
    permission_classes = [permissions.AllowAny]


class AboutUsCreateAPIView(generics.ListCreateAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsListSerializers
    permission_classes = [IsAdminOrReadOnly]


class AboutUsRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsDetailSerializers
    permission_classes = [IsAdminOrReadOnly]


# ──────────────────────────────────────────
#  OpeningHours
# ──────────────────────────────────────────

class OpeningHoursListAPIView(generics.ListAPIView):
    queryset = OpeningHours.objects.all()
    serializer_class = OpeningHoursListSerializers
    permission_classes = [permissions.AllowAny]


class OpeningHoursDetailAPIView(generics.RetrieveAPIView):
    queryset = OpeningHours.objects.all()
    serializer_class = OpeningHoursDetailSerializers
    permission_classes = [permissions.AllowAny]


class OpeningHoursCreateAPIView(generics.ListCreateAPIView):
    queryset = OpeningHours.objects.all()
    serializer_class = OpeningHoursListSerializers
    permission_classes = [IsAdminOrReadOnly]


class OpeningHoursRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OpeningHours.objects.all()
    serializer_class = OpeningHoursDetailSerializers
    permission_classes = [IsAdminOrReadOnly]


# ──────────────────────────────────────────
#  Contact
# ──────────────────────────────────────────

class ContactListAPIView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactListSerializers
    permission_classes = [permissions.AllowAny]


class ContactDetailAPIView(generics.RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactDetailSerializers
    permission_classes = [permissions.AllowAny]


class ContactCreateAPIView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactListSerializers
    permission_classes = [IsAdminOrReadOnly]


class ContactRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactDetailSerializers
    permission_classes = [IsAdminOrReadOnly]
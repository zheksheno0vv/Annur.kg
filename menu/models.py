from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    # Укажи свой реальный домен
    frontend_url = "https://example.com"  # Заменить на адрес твоего сайта или фронтенда

    # Генерация полного URL сброса пароля
    reset_url = "{}{}?token={}".format(
        frontend_url,
        reverse('password_reset:reset-password-request'),  # Django-обработчик, можно заменить
        reset_password_token.key
    )

    # Отправка письма
    send_mail(
        subject="Password Reset for Some Website",  # Тема
        message=f"Use the following link to reset your password:\n{reset_url}",  # Текст
        from_email="noreply@example.com",  # Отправитель
        recipient_list=[reset_password_token.user.email],  # Получатель
        fail_silently=False,
    )


class Restoran(models.Model):
    names = models.CharField(max_length=150)
    description = models.TextField()
    age_work = models.PositiveSmallIntegerField()
    dishes = models.PositiveSmallIntegerField()
    link = models.URLField(blank=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = "Ресторан"



class Category(models.Model):
    category_name = models.CharField(max_length=100)
    description = models.TextField()
    category_icon = models.ImageField(upload_to='category_icon/')


    def __str__(self):
        return self.category_name


class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    subimage = models.ImageField(upload_to='sub_images/')


    def __str__(self):
        return self.name

class Product(models.Model):
    image = models.ImageField(upload_to='product/')
    product_name = models.CharField(max_length=100)
    price = models.PositiveSmallIntegerField()
    gram = models.PositiveSmallIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.product_name


class AboutUs(models.Model):
    information = models.TextField()
    description = models.TextField()
    image_admin = models.ImageField(upload_to='admin_images/')


    def __str__(self):
        return f'{self.description}'

class CafeImage(models.Model):
    about_us = models.ForeignKey(AboutUs, on_delete=models.CASCADE)
    cafe_image = models.ImageField(upload_to='cafe_images/')

    def __str__(self):
        return f'{self.about_us}'

class OpeningHours(models.Model):
    DAY_CHOICES = (
        ('ПН', 'ПН'),
        ('ВТ', 'ВТ'),
        ('СР', 'СР'),
        ('ЧТ', 'ЧТ'),
        ('ПТ', 'ПТ'),
        ('СБ', 'СБ'),
        ('ВС', 'ВС'),
    )

    work_day = MultiSelectField(choices=DAY_CHOICES, max_choices=7)
    data = models.DateTimeField(auto_now=True)
    description = models.TextField()

    def __str__(self):
        return f'{self.description}'

class Contact(models.Model):
    whatsup = models.URLField(blank=True)
    phone_cafe = PhoneNumberField(region='KG')
    admin_phone = PhoneNumberField(region='KG')
    insta_urls = models.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.phone_cafe}'

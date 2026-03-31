



path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
urlpatterns += [
    path('password_reset/verify_code/', verify_reset_code, name='verify_reset_code'),
]

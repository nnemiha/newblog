from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Сначала свои кастомные views (например, signup)
    path('accounts/', include('accounts.urls')),

    # Потом стандартные Django auth (login/logout/password reset и т.д.)
    path('accounts/', include('django.contrib.auth.urls')),

    path('', include('blog.urls')),
]


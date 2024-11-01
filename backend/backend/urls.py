"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from booking_app import views as views_booking
from oauth import views as views_oauth

router = DefaultRouter()

router.register(
    r"oauth",
    views_oauth.AnonymousAuthView,
    basename="oauth",
)
router.register(
    r"user-auth",
    views_oauth.UserAuthView,
    basename="user-auth",
)

router.register(
    r"booking",
    views_booking.BookingViewSet,
    basename="booking",
)

router.register(
    r"payment",
    views_booking.PaymentViewSet,
    basename="payment",
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]

"""testMiio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from owner.views import OwnerViewSet
from regularPlans.views import RegularPlanViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('owners/', OwnerViewSet.as_view({"get": "get", "post": "create"}), name="owners/"),
    path('regular-plans/', RegularPlanViewSet.as_view({"get": "get", "post": "create"}), name="regular-plans/"),
    path('owners/<int:owner_id>/', OwnerViewSet.as_view({"get": "retrieve", "patch": "update", "delete": "delete"}), name="owners/owner_id/"),
    path('regular-plans/<int:regualar_plan_id>/', RegularPlanViewSet.as_view({"get": "retrieve", "patch": "update", "delete": "delete"}), name="regular-plans/regualar_plan_id/"),
]

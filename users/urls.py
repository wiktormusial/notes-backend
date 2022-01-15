from django.urls import path

from .views import UserInfoView

urlpatterns = [
    path('getuserinfo', UserInfoView.as_view(), name="getuserinfo")
]

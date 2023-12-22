from django.urls import path
from .views import CustomUserCreateView, CustomUserView, CustomUserLoginView, CustomUserLogoutView, EditCustomUserViewDetail

urlpatterns = [
    path('registar/', CustomUserCreateView.as_view(), name='resgister'),
    path('detalles/', CustomUserView.as_view(), name='user'),
    path('detalles/extra/', EditCustomUserViewDetail.as_view(), name='details'), 
    path('login/', CustomUserLoginView.as_view(), name='login'),
    path('logout/', CustomUserLogoutView.as_view(), name='logout'),
]

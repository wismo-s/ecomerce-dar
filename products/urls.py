from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import ProductsViewSet, PoductsDetailViewSet, CategoryViewSet, CategoryDetailViewSet, ChoisesViewSet
urlpatterns = [
    path('', ProductsViewSet.as_view(), name='products'),
    path('<slug:slug>/', PoductsDetailViewSet.as_view(), name='products-detail'),
    path('categorias/', CategoryViewSet.as_view(), name='category'),
    path('categorias/<slug:slug>/', CategoryDetailViewSet.as_view(), name='category-detail'),
    path('opciones/', ChoisesViewSet.as_view(), name='choises'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import ProductsViewSet, PoductsDetailViewSet, CategoryViewSet, CategoryDetailViewSet, ChoisesViewSet, ProductsManageViewSet, ChoisesManageViewSet,CategoryManageViewSet
urlpatterns = [
    path('productos/', ProductsViewSet.as_view(), name='products'),
    path('productos/<slug:slug>/', PoductsDetailViewSet.as_view(), name='products-detail'),
    path('admin/', ProductsManageViewSet.as_view(), name='admin-products'),
    path('categorias/', CategoryViewSet.as_view(), name='category'),
    path('admin/categorias/', CategoryManageViewSet.as_view(), name='admin-category'),
    path('categorias/<slug:slug>/', CategoryDetailViewSet.as_view(), name='category-detail'),
    path('opciones/', ChoisesViewSet.as_view(), name='choises'),
    path('admin/opciones/', ChoisesManageViewSet.as_view(), name='admin-choises'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

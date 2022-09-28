from . import views
from django.urls import path

urlpatterns = [
    path('', views.ListaPosts.as_view(), name='inicio'),
    path('<slug:slug>/', views.DetallePost.as_view(), name='detalle_post'),
]

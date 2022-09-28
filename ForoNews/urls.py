from . import views
from django.urls import path

urlpatterns = [
    path('', views.ListaPosts.as_view(), name='inicio'),
    path('<slug:slug>/', views.DetallePost.as_view(), name='detalle_post'),
    path('<slug:slug>/', views.Post_Detallado, name='detalle_post') #habria que corregir esta redundancia y ver como redirigimos para ver post y comentarlo

]

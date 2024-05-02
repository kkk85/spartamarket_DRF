from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductList.as_view()),
    path('<int:productId>/', views.ProductList.as_view()),
    path("<int:product_id>/", views.ProductDetailAPIView.as_view()),
    path("<int:product_id>/like/", views.ProductLikeAPIView.as_view()),
]

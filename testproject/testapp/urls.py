from django.urls import path
from .views import ListAllLessonsView, ListProductLessonsView, ProductStatsView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('lessons/', ListAllLessonsView.as_view(), name='lessons'),
    path('product/<int:product_id>/lessons/', ListProductLessonsView.as_view(), name='list_product_lessons'),
    path('product/stats/', ProductStatsView.as_view(), name='product_stats'),
]

from django.contrib.auth.models import User
from rest_framework import generics
from django.db.models import Sum
from .models import Product, Lesson, ProductAccess
from .serializers import LessonSerializer, ProductAccessSerializer
from django.views.generic import View
from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'


class ListAllLessonsView(generics.ListAPIView):
    serializer_class = LessonSerializer


    def get(self, request, *args, **kwargs):
        user = self.request.user
        lessons = Lesson.objects.filter(products__productaccess__user=user)
        return render(request, 'list_all_lessons.html', {'lessons': lessons})



class ListProductLessonsView(generics.ListAPIView):
    serializer_class = ProductAccessSerializer

    def get(self, request, *args, **kwargs):
        user = self.request.user
        product_id = self.kwargs['product_id']
        product_access = ProductAccess.objects.filter(user=user, product_id=product_id)
        return render(request, 'list_product_lessons.html', {'product_access': product_access})



# class ProductStatsView(View):
#     def get(self, request, *args, **kwargs):
#         products = Product.objects.all()
#         for product in products:
#             product.num_viewed_lessons = product.product_access.filter(viewed=True).count()
#             # Rest of your code here
#         return render(request, 'product_stats.html', {'products': products})




class ProductStatsView(View):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        for product in products:
            product.num_viewed_lessons = product.lessons.filter(productaccess__viewed=True).count()
            product.total_view_time = product.productaccess.aggregate(total_time=Sum('view_time_seconds'))['total_time']
            product.num_students = product.productaccess.values('user').distinct().count()
            total_users = User.objects.count()
            product.purchase_percentage = (product.productaccess.count() / total_users) * 100
        return render(request, 'product_stats.html', {'products': products})



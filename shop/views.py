from django.shortcuts import render

from django.views import View

from shop.models import Category, Product, Testimonial


class LandingView(View):
    def get(self, request):
        category = Category.objects.all()
        product = Product.objects.all()
        testimonial = Testimonial.objects.all()

        context = {
            'category': category,
            'product': product,
            'testimonial': testimonial
        }
        return render(request, 'shop/index.html', context)


class ShopView(View):
    def get(self, request):
        product = Product.objects.all()
        return render(request, 'shop/shop.html', {'product': product})


class ShopDetailView(View):
    def get(self, request):
        product = Product.objects.all()
        return render(request, 'shop/shop-detail.html', {'product': product})



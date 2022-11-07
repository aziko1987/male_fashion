from django.db.models import Min, Max
from django.shortcuts import render
from django.views.generic import ListView

from products.models import ProductModel, CategoryModel, ProductTagModel, ProductColorModel, ProductSizeModel, BrandModel


class ProductListView(ListView):
    template_name = 'main/shop.html'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CategoryModel.objects.all()
        context['tags'] = ProductTagModel.objects.all()
        context['colors'] = ProductColorModel.objects.all()
        context['sizes'] = ProductSizeModel.objects.all()
        context['brands'] = BrandModel.objects.all()
        context['min'], context['max'] = ProductModel.objects.all().aggregate(Min('real_price'), Max('real_price')).values()
        return context

    def get_queryset(self):
        qs = ProductModel.objects.all()
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(title__icontains=q)
        cat = self.request.GET.get('cat')
        if cat:
            qs = qs.filter(category=cat)
        brand = self.request.GET.get('brand')
        if brand:
            qs = qs.filter(brand=brand)
        tag = self.request.GET.get('tag')
        if tag:
            qs = qs.filter(tags=tag)
        size = self.request.GET.get('size')
        if size:
            qs = qs.filter(size=size)
        color = self.request.GET.get('color')
        if color:
            qs = qs.filter(colors=color)
        price = self.request.GET.get('price')
        if price:
            price = price.split(';')
            qs = qs.filter(real_price__gte=price[0], real_price__lte=price[1])
        sort = self.request.GET.get('sort')
        if sort:
            qs = qs.order_by(sort)
        return qs

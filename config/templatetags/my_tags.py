from django import template
from main.models import WishListModel

register = template.Library()


@register.simple_tag()
def get_current_price(request, index):
    data = request.GET.get('price')
    if data:
        return data.split(';')[index]
    return 'null'


@register.filter()
def is_wishlist(user, product):
    return WishListModel.objects.filter(user=user, product=product).exists()

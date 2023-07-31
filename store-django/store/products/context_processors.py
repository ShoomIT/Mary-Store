from products.models import Basket


def baskets(request):
    user = request.user
    return {'baskets': Basket.object.filter(user=user) if user.is_authenticated else []}

from django.shortcuts import render

from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views import View
from .models import ShoppingCart
class AddToShoppingCartView(APIView):
    @csrf_exempt
    @require_POST
    def post(self, request):
        if not request.user.is_authenticated:
            return HttpResponseBadRequest("User is not authenticated")

        product_id = request.POST.get("product_id")
        count = request.POST.get("count", 1)

        if not product_id:
            return HttpResponseBadRequest("Product ID is required")

        product = get_object_or_404(Product, id=product_id)

        try:
            count = int(count)
            if count < 1:
                return HttpResponseBadRequest("Count must be greater than 0")
        except ValueError:
            return HttpResponseBadRequest("Invalid count")

        shopping_cart, created = ShoppingCart.objects.get_or_create(user=request.user, product=product)
        if not created:
            shopping_cart.count += count
            shopping_cart.save()

        return JsonResponse({"message": "Product added to the shopping cart"})

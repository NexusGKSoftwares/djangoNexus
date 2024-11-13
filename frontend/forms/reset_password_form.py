from .forms import OrderForm
from .models import Order
from django.core.mail import send_mail
from django.conf import settings

def handle_order_submission(request, form):
    """Handle order submission and send email confirmation."""
    if form.is_valid():
        order = form.save(commit=False)
        order.user = request.user  # Set the user as the current logged-in user
        order.save()

        # Send a confirmation email
        send_mail(
            'Order Confirmation',
            f'Your order for {order.product.name} has been successfully placed!',
            settings.DEFAULT_FROM_EMAIL,
            [request.user.email],
            fail_silently=False,
        )
        return True
    return False

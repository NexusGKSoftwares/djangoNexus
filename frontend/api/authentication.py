from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User

class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        username = request.META.get('HTTP_USERNAME')
        password = request.META.get('HTTP_PASSWORD')

        if not username or not password:
            return None

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise AuthenticationFailed('No such user')

        if not user.check_password(password):
            raise AuthenticationFailed('Invalid password')

        return (user, None)

from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view(['GET'])
def test_view(request):
    data = {
        'message': 'This is a test API view.',
        'status': 'success'
    }
    return JsonResponse(data)

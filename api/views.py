from django.http import JsonResponse
from rest_framework import authtoken
# Create your views here.
def home(request):
    return JsonResponse({'api': 'Course Django React', 'name': 'tuan'})
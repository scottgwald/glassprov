import random
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

try:
    from django.shortcuts import render_to_response
except ImportError:
    django_lib = False
else:
    django_lib = True
    # no django

@csrf_exempt
@require_http_methods(["GET"])
def home(request):
    return render_to_response("topIndex.html")

from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model, login, authenticate
from django.http import JsonResponse

User = get_user_model()


def homepage_view(request):
    return render(request, 'homepage.html')


def index(request, username):
    """
    Checks if username exists then renders the store page
    """
    user = get_object_or_404(User, username=username)

    response = render(request, 'index.html', {'user': user})
    return response


def authenticate_view(request):
    """
    view to validate the login requests
    """
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    print('user', user)
    if user:
        login(request, user)
        response = {
            'authenticated': True
        }
        return JsonResponse(response)
    else:
        response = {
            'authenticated': False
        }
        return JsonResponse(response, status=404)

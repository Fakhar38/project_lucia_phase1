from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model

User = get_user_model()


def store(request, username):
    """
    Checks if username exists then renders the store page
    """
    user = get_object_or_404(User, username=username)

    response = render(request, 'user/store.html', {'user': user})
    return response

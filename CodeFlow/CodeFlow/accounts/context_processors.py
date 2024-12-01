

def navbar_user(request):
    return {
        'navbar_user': request.user
    }

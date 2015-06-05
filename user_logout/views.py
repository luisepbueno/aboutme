from django.http import HttpResponseRedirect
from django.contrib.auth import logout

def user_logout(request):
    logout(request)
    # TODO: exibir uma mensagem confirmando o logout
    return HttpResponseRedirect("/")
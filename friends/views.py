from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.core import serializers
from django.contrib.auth.decorators import login_required
#from feedbacks.models import Feedback

#@login_required
#def list_friends(request):
#    friends = User.objects.all() #values('username', 'first_name', 'last_name')
#    data = serializers.serialize('json', friends)
#    return HttpResponse(data, content_type='application/json')

@login_required
def friends(request):
    
    friends = User.objects.all().values('id', 'first_name', 'last_name')

    return render(request, 'friends.html', {
        'user': request.user,
        'friends': friends,
        })

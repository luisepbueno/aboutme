from django.shortcuts import render
#from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from feedbacks.models import Feedback

@login_required
def home(request):
    
    print request.user
    
    try:
        last_user_feedback = Feedback.objects.filter(target=request.user,
                                                    approved=True,
                                                    deleted=False).latest(field_name='post_date')
    except:
        last_user_feedback = None

    try:
        last_friend_feedback = Feedback.objects.filter(approved=True,
                                                    deleted=False).exclude(target=request.user).latest(field_name='post_date')
    except:
        last_friend_feedback = None
    
    # remove logged user from friends' list
    friends = User.objects.all().exclude(pk=request.user.id)
    
    print "estou no home!"
    print last_user_feedback
    print last_friend_feedback

    return render(request, 'home.html', {
        'user': request.user,
        'last_user_feedback': last_user_feedback,
        'last_friend_feedback': last_friend_feedback,
        'friends': friends,
        })

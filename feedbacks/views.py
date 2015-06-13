from django.contrib.auth import get_user_model
from django.shortcuts import render
#from django.contrib.auth.models import User
from models import Feedback
from forms import WriteFeedbackForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

def checkSeenFeedbacks(user, feedbacks):

    # new feedbacks counter
    new_feedbacks = 0
    
    # check new feedbacks
    # TODO: probably there is a better way to do that
    for feedback in feedbacks:
        new = True
    
        # check if feedback was already seen
        for seen_by_user in feedback.seen_by.all():
            if seen_by_user.id==user.id:
                feedback.new = False
                new = False
                break
        
        # feedback was not seen
        if new:
            new_feedbacks = new_feedbacks+1
            feedback.seen_by.add(user.id)
            feedback.new = True
    
    return new_feedbacks

@login_required
def feedbacks(request):
    #feedbacks = Feedback.objects.select_related('feedback_seen_by').filter(approved=True)
    feedbacks = Feedback.objects.filter(approved=True)
    
    # mark which feedbacks are new and get the new feedbacks count
    new_feedbacks = checkSeenFeedbacks(request.user, feedbacks)

    return render(request, 'feedbacks.html', {
        'user': request.user,
        'feedbacks': feedbacks,
        'new_feedbacks': new_feedbacks,
        })

@login_required
def friends_feedbacks(request, friend_id):

    # get user
    try:
        friend = get_user_model().objects.get(pk=friend_id)#.values('id', 'first_name', 'last_name')
    except:
        return HttpResponse('Could not find user ' + friend_id)

    # if user is the current logged user, go to a different page
    if(friend==request.user):
        feedbacks = Feedback.objects.filter(target=friend, deleted=False)
        template = 'my_feedbacks.html'
    # else, goes to regular page
    else:
        feedbacks = Feedback.objects.filter(target=friend, approved=True, deleted=False)
        template = 'friends_feedbacks.html'
        
    new_feedbacks = checkSeenFeedbacks(request.user, feedbacks)

    return render(request, template, {
        'user': request.user,
        'friend': friend,
        'new_feedbacks': new_feedbacks,
        'feedbacks': feedbacks,
    })

@login_required
def write_feedback(request, user_id):
    # data to be sent to template
    data = { 'errors': [] }
    
    # get users
    target_user = get_user_model().objects.get(pk=user_id)
    poster_user = request.user
    
    data['user'] = poster_user

    # target user
    data['target_user'] = target_user

    # if post method, try to post feedback
    if request.method == 'POST':
        form = WriteFeedbackForm(request.POST)
        data['form'] = form
        
        if form.is_valid():
            feedback_msg = form.cleaned_data['feedback']
            anonymous    = form.cleaned_data['anonymous']

            try:
                # try to insert feedback
                feedback = Feedback.objects.create(message=feedback_msg,
                                        anonymous=anonymous,
                                        poster=poster_user,
                                        target=target_user,
                                        approved=False)
            except:
                data['errors'] += ['Could not insert feedback']
                raise
            else:
                data['feedback_posted'] = 1
    else:
        data['form'] = WriteFeedbackForm()

    return render(request, 'post_feedback.html', data)

@login_required
def publish_feedback(request, feedback_id):
    # get feedback
    try:
        feedback = Feedback.objects.get(id=feedback_id)
    except:
        return HttpResponse('Could not find feedback')

    # do not allow to publish feedbacks for which
    # the logged user is not the target
    if(feedback.target!=request.user):
        return HttpResponse('You are not allowed to publish feedbacks that are not yours')

    # approve feedback
    feedback.approved=True
    feedback.save()

    # go back to user's feedback page
    return HttpResponseRedirect(reverse('feedbacks'), args=[request.user.id])

@login_required
def delete_feedback(request, feedback_id):
    # get feedback
    try:
        feedback = Feedback.objects.get(id=feedback_id)
    except:
        return HttpResponse('Could not find feedback')

    # do not allow to touch feedbacks for which
    # the target is not the logged user
    if(feedback.target!=request.user):
        return HttpResponse('You are not allowed to delete feedbacks that are not yours')

    # delete feedback
    feedback.deleted=True
    feedback.save()

    # go back to user's feedback page
    return HttpResponseRedirect(reverse('feedbacks', args=[request.user.id]))

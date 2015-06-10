from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from feedbacks.models import Feedback
import json

# Create your views here.
@login_required(login_url='jsonui/forbidden')
def notifications(request):
    user_not_approved_feedback_count = Feedback.objects.filter(target=request.user, 
                                                               approved=False, 
                                                               deleted=False).count()
    
    data = {
        'my-feedbacks': user_not_approved_feedback_count,
        'friends': 0,
        'feedbacks': 0,
        }
    
    return HttpResponse(json.dumps(data), content_type='application/json')

def forbidden(request):
    data = {
            'error': 'forbidden'
        }
    return HttpResponse(json.dumps(data), content_type='application/json')
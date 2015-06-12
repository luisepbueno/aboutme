from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from forms import LoginForm, RegistrationForm
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

def user_login(request):
    # data sent to template
    data = {}

    # redirect url
    redir = "/"

    # if user is already authenticated, redirect to home
    if request.user.is_authenticated():
        return HttpResponseRedirect(redir)

    # if post method, try to login
    if request.method == "POST":
        form = LoginForm(request.POST)
        data["form"] = form

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            # authenticate
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(redir)
                else:
                    form.add_error(None, "Account disabled. Contact administrator.")
            else:
                form.add_error(None, "Invalid username or password.")
    # if no post method, create empty login form
    else:
        data["form"] = LoginForm()

    return render(request, 'login.html', data);
    #from django.shortcuts import render_to_response
    #from django.template.context import RequestContext
    #print "1"
    #context = RequestContext(request)
    #print "2"
    #return render_to_response('login.html', data, context_instance=RequestContext(request))


def user_logout(request):
    logout(request)
    # TODO: exibir uma mensagem confirmando o logout
    return HttpResponseRedirect("/")

def user_register(request):
    
    from django.contrib.auth.models import User
    
    # data to be sent to template
    data = {}
    
    # redirect url
    redir = '/'

    # if user is already authenticated, redirect to home
    if request.user.is_authenticated():
        return HttpResponseRedirect(redir)

    # if post method, try to register user
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        data['form'] = form

        if form.is_valid():
            #username    = form.cleaned_data['email']
            email       = form.cleaned_data['email']
            first_name  = form.cleaned_data['first_name']
            last_name   = form.cleaned_data['last_name']
            password    = form.cleaned_data['password']           

            try:
                # create user
                user = User.objects.create_user(username=email,
                                                first_name=first_name, 
                                                last_name=last_name, 
                                                password=password)
 
                # create empty user profile
                user_profile = UserProfile(user=user)

                # login user
                # TODO: o quer fazer se o login falhar?
                user = authenticate(username=email, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return HttpResponseRedirect(redir)
                    else:
                        form.add_error(None, 'Account disabled. Contact administrator.')
                else:
                    form.add_error(None, 'Invalid username or password.')
            except:
                form.add_error(None, 'Could not create user.')
            else:
                data['user_created'] = 1
    else:
        data['form'] = RegistrationForm()

    return render(request, 'register.html', data)

@login_required
def user_profile(request):
    return HttpResponse('Not implemented')


from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from user_profile.models import UserProfile
from forms import RegistrationForm

def register(request):
    # data to be sent to template
    data = {}
    data['title'] = 'AboutMe registration'
    
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
                user_profile.save()

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
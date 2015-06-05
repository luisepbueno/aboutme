from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from forms import LoginForm

#def login_page(request):
    #return render(request, 'login.html', {
        #'app_name':         'AboutMe',
        #'app_description':  'blah blah blah',
        #'login_text':       'Login with Facebook',
        #})

def user_login(request):
    # data sent to template
    data = {}
    data['title'] = 'AboutMe login'

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

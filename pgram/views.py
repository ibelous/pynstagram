from django.views import generic
from django.utils import timezone
from .models import PostModel, CommentModel
from django.shortcuts import render
from .forms import UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


class IndexView(generic.ListView):
    template_name = 'pgram/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return PostModel.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:10]


#TODO: fix Detail View
class DetailView(generic.DetailView()):
    model = PostModel
    template_name = 'pgram/detail.html'

    def get_queryset(self):
        return PostModel.objects.filter(pub_date__lte=timezone.now())


@login_required
def special(request):
    return HttpResponse("You are logged in !")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('pgram:index'))


class RegistrationView(generic.CreateView):
    template_name = 'pgram/registration.html'


def registration(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'pgram/registration.html',
                           {'user_form': user_form,
                            'profile_form': profile_form,
                            'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('pgram:index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'pgram/login.html', {})


def add_post(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        desc = request.POST.get('desc')
        user = request.user
        if user:
            PostModel.objects.create(author=user, image=image, desc=desc)
            user.usermodel.all_posts_count += 1
            user.usermodel.current_posts_count += 1
            return HttpResponseRedirect(reverse('pgram:index'))
        else:
            print("Someone tried to add post and failed.")
            return HttpResponse("You need to log in first")
    else:
        return render(request, 'pgram/add_post.html', {})


def add_comment(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        author = request.user.usermodel
        post_obj = request.POST.get('post')
        post = PostModel.objects.get(id=post_obj)
        CommentModel.objects.create(author=author, text=text, post=post)
        return HttpResponseRedirect(reverse('pgram:index'))
    else:
        return HttpResponseRedirect(reverse('pgram:index'))

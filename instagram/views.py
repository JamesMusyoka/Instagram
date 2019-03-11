from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.views import login
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, CommentForm, ProfileForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from .models import Image
import datetime as dt

def  index(request):
    images = Image.objects.all()
    dates = dt.date.today()
    form = CommentForm(request.POST)
    return render(request, 'index.html',{'dates':dates,'images':images, "CommentForm": CommentForm})


def convert_dates(dates):

    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    day = days[day_number]
    return day

def profile(request):
     date = dt.date.today()
     return render(request, 'profile.html', {"date": date})

@login_required(login_url='/accounts/login/')
def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.editor = current_user
            profile.save()
        return redirect('profile')

    else:
        form = NewArticleForm()
    return render(request, 'profile/new_profile.html', {"form": form})

def search_results(request,search_results):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)

        message = "{search_term}"
        return render(request, 'search_results.html', {"message":message, "images": searched_images})

    else:
        message = "You haven't made any terms"
        return render(request, 'search_results.html', {"message":message})


def comment(request, post_id):
    post = get_object_or_404(Image, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.image = post
            comment.save()
    return redirect('index')

    return render(request, 'index.html', {"comment": comment})

def like(request, image_id):
    current_user = request.user
    liked_image=Image.objects.get(id=image_id)
    new_like,created= Likes.objects.get_or_create(who_liked=current_user, liked_image=liked_image)
    new_like.save()

    return redirect('index.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
            
    else:
        form = SignupForm()
    return render(request, 'index.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('login.html')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
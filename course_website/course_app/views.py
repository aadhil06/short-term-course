from django.contrib.auth.models import User
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.core.paginator import Paginator
from .models import *
from .forms import *

# Create your views here.

# Register
def user_signup(request):

    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confirm password are not Same!!")
        else:
            user=User.objects.create_user(username=username,email=email,password=pass1)
            user.save()
            return redirect('login')
        
    return render (request,'signup.html')


# Login
def user_login(request):
    
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':       
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
            
        if user is not None:
            login(request, user)
            return redirect('index')
            
        return HttpResponse("Invalid Credentials!!")
        
    return render(request, 'login.html')

@login_required(login_url = 'login')
def index(request):
    return render(request, 'index.html')


# Create Courses
def course_create(request):
    if request.method == 'POST':
        form = ShortTermCourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('short_course_list')
    else:
        form = ShortTermCourseForm()
    
    context = {
        'form': form
    }
    return render(request, 'short-course-create.html',context)

# Shows the short term course

def course_list(request):
    query = request.GET.get('q')
    course_list = ShortTermCourse.objects.all()
    if query:
        course_list = course_list.filter(subtitle__icontains=query)
        
    paginator = Paginator(course_list, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        
        'courses': page_obj,
        'paginator': paginator,
        'page_obj': page_obj,
        'query': query,
    }

    return render(request, 'short-course-view.html',context)
# Update a Course
def course_update(request,pk):
    course = get_object_or_404(ShortTermCourse, pk=pk)
    if request.method == 'POST':
        form = ShortTermCourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('short_course_list')
    else:
        form = ShortTermCourseForm(instance=course)
            
    context = {
        'form': form,
        'course': course
    }
    return render(request, 'short-course-update.html', context)
# Delete the course
def course_delete(request, pk):
    course = get_object_or_404(ShortTermCourse, pk=pk)

    if request.method == 'POST':
        course.delete()
        return redirect('short_course_list')
    
    return render(request, 'short-course-delete.html',{'course': course})

@login_required(login_url = 'login')
def change_password(request):
    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        # Check if the current password is correct
        if not request.user.check_password(current_password):
            messages.error(request, 'Invalid current password.')
            return redirect('change_password')

        # Check if the new password and confirm password match
        if new_password != confirm_password:
            messages.error(request, 'New password and confirm password do not match.')
            return redirect('change_password')

        # Update the user's password
        request.user.set_password(new_password)
        request.user.save()

        # Update the session authentication hash
        update_session_auth_hash(request, request.user)

        messages.success(request, 'Password successfully changed.')
        return redirect('profile')

    return render(request, 'profile.html')


@login_required(login_url = 'login')
def user_logout(request):
    logout(request)
    return redirect('/')

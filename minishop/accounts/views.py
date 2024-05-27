from django.shortcuts import render,redirect
import uuid
from django.contrib.auth.models import User,auth
from django.contrib import messages

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:

            if User.objects.filter(username=username).exists():
                messages.info(request, "username is already taken")
                return redirect("Register")


            elif User.objects.filter(email=email).exists():
                messages.info(request, "email is already taken")
                return redirect("Register")

            else:
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name, last_name=last_name)
                user.save()
                print('user created')

        else:
            return redirect('Register')
        return redirect('/')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        print(user)

        if user is not None:
            auth.login(request, user)
            uid = str(uuid.uuid4())                        #generate a random UID
            request.session['uid'] = uid
            request.session['username'] = username
            return redirect('/')
        else:
            messages.info(request, 'Invalid details')
            return redirect('Login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
#--------------------------------------------------------------------------------------------------------------
def forgotpassword(request):
    return render(request, 'forgotpassword.html')

# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def forgot_password(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username_or_email')
        try:
            user = User.objects.get(email=username_or_email)
        except User.DoesNotExist:
            try:
                user = User.objects.get(username=username_or_email)
            except User.DoesNotExist:
                messages.error(request, 'User does not exist.')
                return redirect('forgot_password')

        # Generate a new password or reset link and send it to the user's email
        new_password = User.objects.make_random_password()
        user.set_password(new_password)
        user.save()

        # Send an email with the new password
        send_mail(
            'Password Reset',
            f'Your new password is: {new_password}',
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )

        messages.success(request, 'A new password has been sent to your email.')
        return redirect('login')  # Redirect to login page after sending the new password



 # Generate a new password or reset link and send it to the user's email
        new_password = User.objects.make_random_password()
        user.set_password(new_password)
        user.save()

        # Send an email with the new password
        send_mail(
            'Password Reset',
            f'Your new password is: {new_password}',
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )

        messages.success(request, 'A new password has been sent to your email.')
        return redirect('login')  # Redirect to login page after sending the new password



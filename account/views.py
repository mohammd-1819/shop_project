from random import randint
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm, RegisterForm, VerifyEmailForm, AddressCreationForm
from .models import User, EmailVerification


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['email'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('home:home')
        return render(request, 'account/login.html', {'form': form})


def logout_view(request):
    user = request
    logout(user)
    return redirect('home:home')


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'account/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            user, created = User.objects.get_or_create(username=username, email=email)
            if created:
                user.is_active = False
                user.set_password(form.cleaned_data.get('password1'))
                user.fullname = form.cleaned_data.get('username')
                user.save()
                code = randint(1000, 9999)
                EmailVerification.objects.create(user=user, code=code)
                send_mail(
                    'Email Verification',
                    f'Your verification code is {code}',
                    'mohammd.ch81m@gmail.com',
                    [email],
                    fail_silently=False,
                )
                return redirect('account:verify-email')

        return render(request, 'account/register.html', {'form': form})


class VerifyEmailView(View):
    def get(self, request):
        form = VerifyEmailForm()
        return render(request, 'account/verify_email.html', {'form': form})

    def post(self, request):
        code = request.POST.get('code')
        form = VerifyEmailForm(data=request.POST)
        if form.is_valid():
            try:
                verification = EmailVerification.objects.get(code=code)
                user = verification.user
                user.is_active = True
                user.save()
                verification.delete()
                login(request, user)
                return redirect('home:home')
            except EmailVerification.DoesNotExist:
                pass

        return render(request, 'account/verify_email.html', {'form': form})


class AddAddressView(View):
    def post(self, request):
        form = AddressCreationForm(data=request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            next_page = request.GET.get('next')
            if next_page:
                return redirect(next_page)
            return render(request, 'account/add_address.html', {'form': form})

    def get(self, request):
        form = AddressCreationForm()
        return render(request, 'account/add_address.html', {'form': form})

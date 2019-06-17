from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from smtplib import *
import smtplib
from django.contrib.auth.decorators import login_required


def index(request):
    templates = 'template.html'
    print("er")
    context = {}
    if request.method == "GET":
        return render(request, templates, context)


@login_required(login_url='/Login/')
def home(request):
    templates = 'home.html'
    context = {}
    if request.method == "GET":
        return render(request, templates, context)


def signup(request):
    form = SignupForm()
    model = Signup()
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            model.username = request.POST.get('username')
            model.name = request.POST.get('name')
            model.email = request.POST.get('email')
            model.gender = request.POST.get('gender')
            form.password = request.POST.get('password')
            form.confirm = request.POST.get('confirm')

            try:
                User.objects.get(username=model.username)
                messages.error(request, 'User already exists !!!')
                return render(request, 'sign_up.html')
            except User.DoesNotExist:

                model.save(Signup())
                User.objects.create_user(username=model.username, password=form.password, email=model.email,
                                         first_name=model.name)
                messages.success(request, 'Signup Successfully !!!')
                return render(request, 'Login.html')

        else:
            return redirect("/contact/")
    else:
        return render(request, 'sign_up.html', {'form': form})


def Login(request):
    model = Signup()
    username = model.username
    if request.method == "GET":
        if 'action' in request.GET:
            action = request.GET.get('action')
            if action == 'logout':
                if 'username' in request.session:
                    request.session.flush()
                    logout(request)
                    return redirect('Login')
        if 'username' in request.session:
            model.username = request.session['username']
            print(request.session.set_expiry(300))  # session lifetime in seconds(from now)
            print(request.session.get_expiry_date())  # datetime.datetime object which repre

    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
            if user:
                request.session['username'] = model.username
                login(request, user)
                if not user.is_staff:
                    return redirect('home')
                else:
                    return redirect('profile')
            else:
                messages.error(request, 'Invalid Credentials !!!')
                return redirect('Login')
        else:
            messages.error(request, 'Username or Password Incorrect !!!')
            return redirect('Login')
    return render(request, 'Login.html', {'form': LoginForm(), 'username': model.username})


def lawyer_signup(request):
    form = LawyerForm()
    if request.method == "POST":
        form = LawyerForm(request.POST, request.FILES)
        model = LawyerSignup()
        if form.is_valid():
            model.username = request.POST.get('username')
            model.name = form.cleaned_data['name']
            model.gender = request.POST.get('gender')
            model.email = form.cleaned_data['email']
            model.mobile = form.cleaned_data['mobile']
            model.password = form.cleaned_data['password']
            model.category = request.POST.getlist('category')
            model.age = request.POST.get('age')
            model.language = request.POST.getlist('language')
            model.exp = request.POST.get('exp')
            model.picture = request.FILES['picture']
            model.degree = request.FILES['degree']
            model.certificate = request.FILES['certificate']
            model.save(LawyerSignup())
            print("Data Saved Successfully")
            User.objects.create_user(username=model.username, email=model.email, password=model.password,
                                     first_name=model.name)
            messages.error(request, 'Your documents are under verification, Try login after few days..')
            return redirect("Login")
        else:
            messages.error(request, 'Invalid Entries ')
            return render(request, 'lawyer_signup.html')
    else:
        return render(request, 'lawyer_signup.html', {'form': form})


def contactout(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        model = Contact()
        if form.is_valid:
            model.Name = request.POST.get('Name')
            model.Email = request.POST.get('Email')
            model.Subject = request.POST.get('Subject')
            model.save(Contact())

            from_email = ''
            password = ''
            subject1 = 'New Contact Request from lawyers Hub'
            to = ''
            message = 'Subject : ' + subject1 + '\n' + model.Name + '\n' + model.Email + '\n' + model.Subject

            try:
                smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
                smtpobj.starttls()
                smtpobj.login(from_email, password)
                smtpobj.sendmail(from_email, to, message)
                messages.info(request, 'Your request has been sent successfully')
                smtpobj.close()
                return redirect('index')

            except SMTPException:
                messages.error(request, 'Your request cannot sent !!')
                return redirect('contactout')
        else:
            messages.error(request, 'Your request cannot sent !!')
            return render(request, 'contactout.html')
    else:

        return render(request, "contactout.html", {'form': form})


@login_required(login_url='/Login/')
def contactin(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        model = Contact()
        if form.is_valid:
            model.Name = request.POST.get('Name')
            model.Email = request.POST.get('Email')
            model.Subject = request.POST.get('Subject')
            model.save(Contact())

            from_email = ''
            password = ''
            subject1 = 'New Contact Request from lawyers Hub'
            to = ''
            message = 'Subject : ' + subject1 + '\n' + model.Name + '\n' + model.Email + '\n' + model.Subject

            try:
                smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
                smtpobj.starttls()
                smtpobj.login(from_email, password)
                smtpobj.sendmail(from_email, to, message)
                messages.info(request, 'Your request has been sent successfully')
                smtpobj.close()
                return redirect('home')

            except SMTPException:
                messages.error(request, 'Your request cannot sent !!')
                return redirect('contactin')
        else:
            messages.error(request, 'Invalid Entries..')
            return render(request, 'contactin.html')
    else:
        obj = Signup.objects.filter(username=request.user)
        return render(request, "contactin.html", {'form': form, 'obj': obj})


@login_required(login_url='/Login/')
def lawyer_profile(request):
    if request.method == 'GET':
        if 'action' in request.GET:
            action = request.GET.get('action')
            if action == 'logout':
                if 'username' in request.session:
                    request.session.flush()
                    logout(request)
                    return redirect('Login')
        obj = LawyerSignup.objects.filter(username=request.user)

        return render(request, 'lawyer_profile.html', {'obj': obj})


@login_required(login_url='/Login/')
def talk(request):
    form = TalkForm()
    if request.method == "POST":
        form = TalkForm(request.POST)
        model = Talk_to_lawyer()
        if form.is_valid():

            model.Area = request.POST.get('Area')
            model.City = form.cleaned_data['City']
            model.Email = form.cleaned_data['Email']
            model.Subject = form.cleaned_data['Subject']
            model.Lawyer = request.POST.get('Lawyer')
            model.save(Talk_to_lawyer())
            return redirect('home')
        else:
            messages.error(request, 'Invalid Form Entries')
            return redirect('contactin')
    else:
        return render(request, 'talk.html', {'form': form})


@login_required(login_url='/Login/')
def lawyers(request):
    templates = 'lawyers.html'
    context = {}
    if request.method == "GET":
        return render(request, templates, {})


@login_required(login_url='/Login/')
def family(request):
    templates = 'family.html'
    context = {}
    if request.method == "GET":
        return render(request, templates, context)


@login_required(login_url='/Login/')
def property(request):
    templates = 'property.html'
    context = {}
    if request.method == "GET":
        return render(request, templates, context)


@login_required(login_url='/Login/')
def criminal(request):
    templates = 'criminal.html'
    context = {}
    if request.method == "GET":
        return render(request, templates, context)


@login_required(login_url='/Login/')
def labour(request):
    templates = 'labour.html'
    context = {}
    if request.method == "GET":
        return render(request, templates, context)


@login_required(login_url='/Login/')
def tax(request):
    templates = 'tax.html'
    context = {}
    if request.method == "GET":
        return render(request, templates, context)


@login_required(login_url='/Login/')
def civil(request):
    templates = 'civil.html'
    context = {}
    if request.method == "GET":
        return render(request, templates, context)

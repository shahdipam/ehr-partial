from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from . import blockchain
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_pat(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username= username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('dashboard'))
        else:
            context["error"]= "Provide correct info !!!!"
            return render(request, "login_pat.html", context)
    else:
        return render(request, "login_pat.html", context)

def login_doc(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username= username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('dashboard_doc'))
        else:
            context["error"]= "Provide correct info !!!!"
            return render(request, "login_doc.html", context)
    else:
        return render(request, "login_doc.html", context)

def home(request):
    # user = User.objects.get(username='Patient1')
    # patient1 = patient(user=user)

    context = {}
    context['current_user'] = request.user
    context['all_users'] = User.objects.filter(is_superuser=True)
    return render(request, 'home.html', context)

def home_doc(request):

    # user = User.objects.get(username='Doctor1')
    # doctor1 = doctor(user=user)

    return render(request, 'home_doc.html', {})

def index(request):
    return render(request, 'index.html', {})

def index_doc(request):
    return render(request, 'index_doc.html', {})


@csrf_exempt
def files(request):
    print("HASHES:"+ str(blockchain.contract.functions.get_hashes().call()))

    if request.method == 'POST':
        file = request.FILES['document']
        if file.name.endswith('.jpeg') or file.name.endswith('.jpg'):

            blockchain.uploadIpfs(file)
            return render(request, 'files.html', {'hashes': blockchain.contract.functions.get_hashes().call(), 'some_flag': 1})
        else:
            return render(request, 'files.html', {'hashes': blockchain.contract.functions.get_hashes().call(), 'some_flag': 0})


    return render(request, 'files.html', {'hashes': blockchain.contract.functions.get_hashes().call(), 'some_flag': -1})


@csrf_exempt
def files_doc(request):
    print("HASHES:"+ str(blockchain.contract.functions.get_hashes().call()))

    if request.method == 'POST':
        file = request.FILES['document']
        if file.name.endswith('.jpeg') or file.name.endswith('.jpg'):

            blockchain.uploadIpfs(file)
            return render(request, 'files_doc.html', {'hashes': blockchain.contract.functions.get_hashes().call(), 'some_flag': 1})
        else:
            return render(request, 'files_doc.html', {'hashes': blockchain.contract.functions.get_hashes().call(), 'some_flag': 0})


    return render(request, 'files_doc.html', {'hashes': blockchain.contract.functions.get_hashes().call(), 'some_flag': -1})


@csrf_exempt
def book(request):

    if request.method == 'POST':
        name = request.POST['doc']
        user = User.objects.create_user(name,password='admin')
        user.is_superuser = True
        user.save()

    return render(request, 'book.html', {})


def profile(request):
    print(request.user)
    # user = User.objects.get(name="Patient1")
    return render(request, 'profile.html', {})

def about(request):
    return render(request, 'about.html', {})

def book_doc(request):
    return render(request, 'set.html', {})

def profile_doc(request):
    return render(request, 'profile_doc.html', {})

def about_doc(request):
    return render(request, 'about_doc.html', {})

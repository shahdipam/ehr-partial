from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from . import blockchain

# Create your views here.


def home(request):
    return render(request, 'home.html', {})


def index(request):
    return render(request, 'index.html', {})


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


def book(request):
    return render(request, 'book.html', {})


def profile(request):
    return render(request, 'profile.html', {})


def about(request):
    return render(request, 'about.html', {})

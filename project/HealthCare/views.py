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
    # print(blockchain.contract.functions.get_hashes().transact({'from': blockchain.w3.eth.accounts[1]}))

    input = open('hashes.txt','r').read().split('\n')
    input.pop()
    print(input)
    filehashes = set(input)

    if request.method == 'POST':
        file = request.FILES['document']
        fs = FileSystemStorage()
        if file.name.endswith('.jpeg') or file.name.endswith('.jpg'):

            res = blockchain.uploadIpfs(file)
            print(res)
            return render(request, 'files.html', {'hashes': filehashes, 'some_flag': 1})
        else:
            return render(request, 'files.html', {'hashes': filehashes, 'some_flag': 0})


        # fs.save(file.name, file)
    return render(request, 'files.html', {'hashes': filehashes, 'some_flag': -1})


def book(request):
    return render(request, 'book.html', {})


def profile(request):
    return render(request, 'profile.html', {})


def about(request):
    return render(request, 'about.html', {})

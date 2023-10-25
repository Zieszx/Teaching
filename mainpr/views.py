from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def tDetail(request):
    return render(request, 'topics-detail.html')

def tListing(request):
    return render(request, 'topics-listing.html')

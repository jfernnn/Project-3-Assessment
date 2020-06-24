from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView

from .models import WishList

# Create your views here.

def home(request):
    return render(request, 'home.html', {
        'wishlist': WishList.objects.all()
    })

class ItemCreate(CreateView):
    model = WishList
    fields = '__all__'

class ItemDelete(DeleteView):
    model = WishList
    success_url = '/'    

from multiprocessing import context
from django.shortcuts import *
from django.http import *
from django.urls import reverse_lazy
from food.models import *
from food.forms import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView


# Create your views here.
#----------------------------------------------------------------------------------------------







# Function based Index view
#----------------------------------------------------------------------------------------------
def Index(request):


    if request.user.is_superuser:
        itemlist = Item.objects.all()
        
    elif request.user.is_authenticated and request.user.profile.user_type== 'rest':
        itemlist = Item.objects.filter(rest_owner=request.user.id)
        
    elif request.user.is_authenticated and request.user.profile.user_type== 'cust':
        itemlist = Item.objects.all()
        
    else:
        itemlist = Item.objects.all()
        

    context = {
        'itemlist':itemlist
        }
    return render(request, 'food/index.html', context)
#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
# Class based Index view
class IndexClassView(ListView):
    model = Item
    context_object_name = 'itemlist'
    template_name = 'food/index.html'
#----------------------------------------------------------------------------------------------










# Function based Detail view
#----------------------------------------------------------------------------------------------
def Detail(request, itemid):
    item = Item.objects.get(id=itemid)
    context={
        'item': item
        }
    return render(request, 'food/detail.html', context)
#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
# CLass based Detail view
class DetailClassView(DetailView):
    model = Item
    context_object_name = 'item'
    template_name = 'food/detail.html'
#----------------------------------------------------------------------------------------------










# Function based CreateItem view
#----------------------------------------------------------------------------------------------
def CreateItem(request):

        form = ItemForm(request.POST or None)
        
        if request.method == 'POST':
                form.instance.added_by = request.user.username
                form.save()
                return redirect('food:Index')
        context ={
            'form': form
            }
        return render(request, 'food/item-form.html', context)
#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
# CLass based CreateItem view
class IndexCreateItemView(CreateView):
    model = Item
    fields = ['rest_owner', 'prod_code', 'item_name', 'item_desc', 'item_price', 'item_image']
    template_name = 'food/item-form.html'
    success_url = reverse_lazy('food:Index')

    def form_valid(self, form):
        return super().form_valid(form)









#----------------------------------------------------------------------------------------------
# Function based UpdateItem view
#----------------------------------------------------------------------------------------------
def UpdateItem(request, itemid):

    item = Item.objects.get(id=itemid)
    form = ItemForm(request.POST or None, instance=item)

    if request.method == 'POST':
        form.save()
        return redirect('food:detail', itemid=itemid)
    
    context={
        'form':form
    }

    return render(request, 'food/item-form.html', context)
#----------------------------------------------------------------------------------------------











# Function based DeleteItem view
#----------------------------------------------------------------------------------------------
def DeleteItem(request, itemid):
    item = Item.objects.get(id=itemid)
    context={
        'item':item
        }
    if request.method =='POST':
        item.delete()
        return redirect('food:Index')
    return render(request, 'food/item-delete.html', context)
#----------------------------------------------------------------------------------------------










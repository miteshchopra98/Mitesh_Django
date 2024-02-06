from multiprocessing import context
from django.shortcuts import *
from django.http import *
from food.models import *
from food.forms import *

# Create your views here.

def Index(request):
    itemlist = Item.objects.all()
    context = {
        'itemlist':itemlist
        }
    return render(request, 'food/index.html', context)

def Detail(request, itemid):
    item = Item.objects.get(id=itemid)
    context={
        'item': item
        }
    return render(request, 'food/detail.html', context)

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

def DeleteItem(request, itemid):
    item = Item.objects.get(id=itemid)
    context={
        'item':item
        }
    if request.method =='POST':
        item.delete()
        return redirect('food:Index')
    return render(request, 'food/item-delete.html', context)
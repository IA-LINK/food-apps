from django.shortcuts import render,redirect
from .models import Items
from django.template import loader
from django.http import HttpResponse
from .forms import ItemsForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView



def index(request):
    item_list = Items.objects.all()
    template = loader.get_template('foodz/index.html')
    context = {
        'item_list':item_list,
       }
    return render(request,'foodz/index.html',context)


class IndexClassView(ListView):
    model = Items;
    template_name = 'foodz/index.html'
    context_object_name = 'item_list'



def items(request):
    return HttpResponse('<h1>This is an items view</h1>')



def detail(request,items_id):
    items = Items.objects.get(pk=items_id)
    context = {
        'items':items,
    }
    return render(request,'foodz/detail.html',context)
     


class FoodzDetail(DetailView):
    model = Items
    template_name = 'foodz/detail.html'



def create_items(request):
    form = ItemsForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('foodz:index')

    return render(request,'foodz/items-form.html',{'form':form})

# this is a class based view for create item

class CreateItems(CreateView):
    model = Items
    fields = ['item_name','item_desc','item_price','item_image']
    template_name='foodz/items-form.html'

    def form_valid(self,form):
        form.instance.user_name = self.request.user

        return super().form_valid(form)


def update_item(request,id):
    items = Items.objects.get(id=id)
    form = ItemsForm(request.POST or None, instance=items)

    if form.is_valid():
        form.save()
        return redirect('foodz:index')
        
    return render(request,'foodz/items-form.html',{'form':form,'items':items})



def delete_item(request,id):
    items = Items.objects.get(id=id)

    if request.method == 'POST':
        items.delete()
        return redirect('foodz:index')
    return render(request,'foodz/items-delete.html',{'items':items})

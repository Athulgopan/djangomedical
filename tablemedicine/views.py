from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import medkit
from .forms import sear
from django.contrib.auth.decorators import login_required

# product creation
@login_required(login_url='/login/')
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('retrieve')
    else:
        form =ProductForm()
    return render(request, 'create.html', {'form': form})

# PRODUCT RETRIEVE
@login_required(login_url='/login/')
def med_retrieve(request):
    product_list=medkit.objects.all()
    return render(request,'retrieve.html',{'product_list':product_list})


@login_required(login_url='/login/')
def med_update(request,id):
    product = medkit.objects.get(pk=id)
    if request.method == 'POST':
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('retrieve')

    else:
        form =ProductForm(instance=product)           
    return render(request, 'update.html', {'form': form})

@login_required(login_url='/login/')
def delete_med(request,id):
    product = medkit.objects.get(pk=id)
    if request.method == 'POST':
            product.delete()
            return redirect('retrieve')

    return render(request, 'delete.html', {'product':product})


@login_required(login_url='/login/')
def list_med(request):
    if request.method == 'POST':
        medicname = request.POST.get('name')
        data = medkit.objects.filter(MedicineName__icontains=medicname)
        return render(request, 'search.html', {
            'M': medicname,
            'D': data
        })
    return render(request, 'list-med.html') 








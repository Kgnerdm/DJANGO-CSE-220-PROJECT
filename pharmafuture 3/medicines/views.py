from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import LoginView
from .models import Medicine, HomeProduct
from .forms import MedicineForm, HomeProductForm

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

@login_required
def add_medicine(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('medicine_list')
    else:
        form = MedicineForm()
    return render(request, 'medicines/add_medicine.html', {'form': form})

def search_medicine(request):
    query = request.GET.get('q')
    category = request.GET.get('category', 'All')
    
    if query:
        if category != 'All':
            medicines = Medicine.objects.filter(name__icontains=query, category=category)
        else:
            medicines = Medicine.objects.filter(name__icontains=query)
    else:
        if category != 'All':
            medicines = Medicine.objects.filter(category=category)
        else:
            medicines = Medicine.objects.all()
            
    categories = [cat[0] for cat in Medicine.CATEGORIES]
    
    return render(request, 'medicines/medicine_list.html', {
        'medicines': medicines,
        'categories': categories,
        'selected_category': category
    })

def medicine_detail(request, medicine_id):
    medicine = get_object_or_404(Medicine, pk=medicine_id)
    return render(request, 'medicines/medicine_detail.html', {'medicine': medicine})

@login_required
def remove_medicine(request, medicine_id):
    medicine = get_object_or_404(Medicine, pk=medicine_id)
    if request.method == 'POST':
        medicine.delete()
        return redirect('medicine_list')
    return render(request, 'medicines/remove_medicine.html', {'medicine': medicine})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('medicine_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def home(request):
    products = HomeProduct.objects.all()
    return render(request, 'medicines/home.html', {'products': products})

# Admin views for managing home products
@user_passes_test(lambda u: u.is_superuser)
def add_home_product(request):
    if request.method == 'POST':
        form = HomeProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = HomeProductForm()
    return render(request, 'medicines/add_home_product.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def edit_home_product(request, product_id):
    product = get_object_or_404(HomeProduct, pk=product_id)
    if request.method == 'POST':
        form = HomeProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = HomeProductForm(instance=product)
    return render(request, 'medicines/edit_home_product.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def delete_home_product(request, product_id):
    product = get_object_or_404(HomeProduct, pk=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('home')
    return render(request, 'medicines/delete_home_product.html', {'product': product})

def home_product_detail(request, product_id):
    product = get_object_or_404(HomeProduct, pk=product_id)
    return render(request, 'medicines/home_product_detail.html', {'product': product})


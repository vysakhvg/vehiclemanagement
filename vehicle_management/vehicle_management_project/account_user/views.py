from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import Vehicleform
from .models import vehicle_details

User = get_user_model()


# Create your views here.
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        u_name = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pas = request.POST['pass']
        cpas = request.POST['cpassw']
        user_account = request.POST['account']
        if pas == cpas:
            user = User.objects.create_user(username=u_name, first_name=fname, last_name=lname, email=email,
                                            password=pas, user_type=user_account)
            user.save()
            return redirect('login')
        else:
            messages.error(request, 'Password does not matched')
    return render(request, 'signup.html')


def login_pg(request):
    if request.method == 'POST':
        u_name = request.POST['uname']
        pas = request.POST['pass']
        user = authenticate(username=u_name, password=pas)
        if user is not None and user.user_type == 'is_superadmin':
            login(request, user)
            return redirect('home')
        if user is not None and user.user_type == 'is_admin':
            login(request, user)
            return redirect('home')
        if user is not None and user.user_type == 'is_user':
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')


def logout_pg(request):
    logout(request)
    return home(request)


def add_vdetails(request):
    if request.method == 'POST':
        v_number = request.POST['vnumber']
        v_type = request.POST['vtype']
        v_model = request.POST['vmodel']
        v_description = request.POST['vdescription']
        v_details = vehicle_details.objects.create(vehicle_number=v_number, vehicle_type=v_type, vehicle_model=v_model,
                                                   vehicle_description=v_description)
        v_details.save()
        return redirect('view_vlist')
    return render(request, 'add_vdetails.html')


def view_vlist(request):
    user = request.user
    v_list = vehicle_details.objects.all()
    return render(request, 'vehicle_list.html', {'vlist': v_list, 'user': user})


def view_vdetails(request, v_id):
    user = request.user
    v_details = vehicle_details.objects.get(id=v_id)
    return render(request, 'view_vdetails.html', {'vdetails': v_details, 'user': user})


def editpg(request, id):
    v_details = vehicle_details.objects.get(id=id)
    form = Vehicleform(instance=v_details)
    if request.method == 'POST':
        form = Vehicleform(request.POST or None, request.FILES, instance=v_details)
        if form.is_valid():
            form.save()
            return view_vdetails(request, id)
    return render(request, 'edit.html', {'form': form})


def deletepg(request, id):
    if request.method == 'POST':
        v_details = vehicle_details.objects.get(id=id)
        v_details.delete()
        return redirect('view_vlist')
    return render(request, 'deletepg.html')

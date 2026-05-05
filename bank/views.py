from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count, QuerySet
from .models import Donor, BloodRequest, ContactMessage


def home(request):
    blood_counts = Donor.objects.values('blood_group').annotate(count=Count('id'))
    return render(request, 'index.html', {'blood_counts': blood_counts})


def donors(request):
    query = request.GET.get('q')

    if query:
        donors_list = Donor.objects.filter(
            blood_group__icontains=query,
            status='Approved'
        )
    else:
        donors_list = Donor.objects.filter(status='Approved')

    return render(request, 'donors.html', {'donors': donors_list})


@login_required
def request_blood(request):
    if request.method == 'POST':
        BloodRequest.objects.create(
            patient_name=request.POST.get('name'),
            blood_group=request.POST.get('blood'),
            units_needed=request.POST.get('units'),
            hospital=request.POST.get('hospital'),
            contact=request.POST.get('contact')
        )
        return redirect('home')

    return render(request, 'request.html')


@login_required
def add_donor(request):
    if request.method == 'POST':
        Donor.objects.create(
            user=request.user,
            name=request.POST.get('name'),
            age=request.POST.get('age'),
            blood_group=request.POST.get('blood'),
            phone=request.POST.get('phone'),
            address=request.POST.get('address')
        )
        return redirect('donors')

    return render(request, 'add_donor.html')


@login_required
def my_donors(request):
    donors = Donor.objects.filter(user=request.user)
    return render(request, 'my_donors.html', {'donors': donors})


def emergency_requests(request):
    requests = BloodRequest.objects.all().order_by('-date')
    return render(request, 'emergency.html', {'requests': requests})


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        ContactMessage.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            message=request.POST.get('message')
        )
        return render(request, 'contact.html', {
            'success': 'Message sent successfully!'
        })

    return render(request, 'contact.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {
                'error': 'Username already exists'
            })

        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('home')

    return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )

        if user is not None:
            login(request, user)
            return redirect('home')

        return render(request, 'login.html', {
            'error': 'Invalid username or password'
        })

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('home')

donors_list = Donor.objects.filter(status='Approved')
def donors(request):
    query = request.GET.get('q')

    if query:
        donors_list = Donor.objects.filter(
            blood_group__icontains=query,
            status='Approved'
        )
    else:
        donors_list = Donor.objects.filter(status='Approved')

    return render(request, 'donors.html', {'donors': donors_list})

def emergency_requests(request):
    requests = BloodRequest.objects.all().order_by('-date')
    return render(request, 'emergency.html', {'requests': requests})

@login_required
def edit_donor(request, id):
    donor = Donor.objects.get(id=id, user=request.user)

    if request.method == 'POST':
        donor.name = request.POST.get('name')
        donor.age = request.POST.get('age')
        donor.blood_group = request.POST.get('blood')
        donor.phone = request.POST.get('phone')
        donor.address = request.POST.get('address')
        donor.save()
        return redirect('my_donors')

    return render(request, 'edit_donor.html', {'donor': donor})


@login_required
def delete_donor(request, id):
    donor = Donor.objects.get(id=id, user=request.user)
    donor.delete()
    return redirect('my_donors')


@login_required
def edit_request(request, id):
    blood_request = BloodRequest.objects.get(id=id)

    if request.method == 'POST':
        blood_request.patient_name = request.POST.get('name')
        blood_request.blood_group = request.POST.get('blood')
        blood_request.units_needed = request.POST.get('units')
        blood_request.hospital = request.POST.get('hospital')
        blood_request.contact = request.POST.get('contact')
        blood_request.save()
        return redirect('emergency')

    return render(request, 'edit_request.html', {'r': blood_request})


@login_required
def delete_request(request, id):
    blood_request = BloodRequest.objects.get(id=id)
    blood_request.delete()
    return redirect('emergency')
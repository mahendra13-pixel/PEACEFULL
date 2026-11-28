from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        room_type = request.POST.get('room_type', 'double_seater')  # NEW
        message = request.POST.get('message')

        user = Contact(
            name=name,
            email=email,
            phone=phone,
            room_type=room_type,   # NEW
            message=message,
        )
        user.save()

        messages.success(
            request,
            f"Hi {name}, your message was submitted successfully. "
            f"Room type: {user.get_room_type_display()}."
        )
        return redirect('contact')

    return render(request, 'core/contact.html')
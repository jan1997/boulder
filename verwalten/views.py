from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import User
from django.shortcuts import render, get_object_or_404
from .forms import UserForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def user_list(request):
    users = User.objects.all()
    return render(request, 'verwalten/user_list.html', {'users': users})

@login_required
def user_detail(request, pk):
    user1 = get_object_or_404(User, pk=pk)
    return render(request, 'verwalten/user_detail.html', {'user': user1})

@login_required
def user_new(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.author = request.user
            user.save()
            return redirect('user_detail', pk=user.pk)
    else:
        form = UserForm()
    return render(request, 'verwalten/user_edit.html', {'form': form})
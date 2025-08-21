from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, ProfileForm

# ✅ Registration view
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # ➕ Creates the user
            return redirect('login')  # 🔁 You can redirect to a welcome page instead
    else:
        form = CustomUserCreationForm()
    return render(request, 'auth/register.html', {'form': form})  # ✅ Leave as-is

# ✅ Profile view (requires login)
@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()  # ➕ Updates user info
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'auth/profile.html', {'form': form})  # ✅ Leave as-is
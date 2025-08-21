from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# ✅ Custom registration form that includes email
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)  # ➕ Add email field to default form

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")  # ✅ Leave these fields as-is
        # 🔁 You can add more fields here if needed (e.g., first_name, last_name)

# ✅ Profile update form
class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']  # 🔁 You can include more fields if needed
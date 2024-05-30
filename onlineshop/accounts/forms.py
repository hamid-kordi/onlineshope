from django import forms
from .models import User,OtpCode
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ("email", "phone_number", "full_name")

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """

    password = ReadOnlyPasswordHashField(help_text='change password <a href=\"../password/\">this form </a>')

    class Meta:
        model = User
        fields = ["email","phone_number", "password", "full_name", "is_active", "is_admin"]



class  UserRegisterForm(forms.Form):
    email = forms.EmailField(max_length=40)
    full_name = forms.CharField(max_length=40,label='full name')
    phone = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError('This email already exists')
        return email

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        user = User.objects.filter(phone_number=phone).exists()
        if user:
            raise ValidationError('This phone number already exists')
        OtpCode.objects.filter(phone_number=phone).delete()
        return phone


class VerifyCodeForm(forms.Form):
    code = forms.IntegerField(required = True)
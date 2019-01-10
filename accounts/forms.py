from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from django.contrib.auth import (
    get_user_model,
    )

User = get_user_model()


from django.urls import reverse_lazy


class UserAdminCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email','full_name')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user



class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].help_text = (
            "Raw passwords are not stored, so there is no way to see "
            "this user's password, but you can <a href=\"%s\"> "
            "<strong>Change the Password</strong> using this form</a>."
        ) % reverse_lazy('admin:auth_user_password_change', args=[self.instance.id])

    class Meta:
        model = User
        fields = ('email', 'password',  'admin','full_name')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]






class GuestForm(forms.Form):
    """
    Description:Form that is going to be used to create a guest user
    """
    email = forms.EmailField()








class UserLoginForm(forms.Form):
    """
    Description:A form that will be used by user's to login.\n
    """
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput)


    def clean(self,*args,**kwargs):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email and password :
            user = authenticate(email=email,password=password)

            if not user:
                raise forms.ValidationError("This user does not exist")

            if not user.check_password(password):
                raise forms.ValidationError("Incorrect passsword")
            
            if not user.is_active:
                raise forms.ValidationError("This user is not longer active.")
        
        return super(UserLoginForm,self).clean(*args,**kwargs)
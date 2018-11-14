from django import forms


class GuestForm(forms.Form):
    """
    Description:Form that is going to be used to create a guest user
    """
    email = forms.EmailField()
    
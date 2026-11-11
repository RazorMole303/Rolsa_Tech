from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ["username", "password1", "password2"]


class StorePurchaseForm(forms.Form):
    product = forms.ChoiceField(label="Product")
    quantity = forms.IntegerField(min_value=1, initial=1, label="Quantity")
    full_name = forms.CharField(max_length=120, label="Full name")
    email = forms.EmailField(label="Email address")
    location = forms.CharField(max_length=200, label="Installation location")
    notes = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"rows": 3, "placeholder": "Any installation notes or delivery requests"}),
        label="Notes",
    )

    def __init__(self, *args, products=None, **kwargs):
        super().__init__(*args, **kwargs)
        if products:
            self.fields["product"].choices = [(product["id"], product["name"]) for product in products]

        self.fields["product"].widget.attrs.update({"class": "form-select"})
        self.fields["quantity"].widget.attrs.update({"class": "form-control"})
        self.fields["full_name"].widget.attrs.update({"class": "form-control"})
        self.fields["email"].widget.attrs.update({"class": "form-control"})
        self.fields["location"].widget.attrs.update({"class": "form-control"})
        self.fields["notes"].widget.attrs.update({"class": "form-control"})

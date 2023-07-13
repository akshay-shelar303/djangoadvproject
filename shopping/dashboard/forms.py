from django.forms import ModelForm

from .models import ElectronicItems


class ElectronicForm(ModelForm):
    class Meta:
        model = ElectronicItems
        fields = "__all__"

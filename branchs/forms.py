# branch/forms.py
from django import forms
from .models import Branch

class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ['name', 'location', 'is_hq', 'description', 'branch_commision_precent']
        exclude = ['lat', 'long']


from django import forms
from privatebeta.models import InviteRequest

class InviteRequestForm(forms.ModelForm):
    note = forms.CharField(label="Note (optional)", widget=forms.Textarea(attrs={'class':'note'}))
    
    class Meta:
        model = InviteRequest
        fields = ['email', 'note']

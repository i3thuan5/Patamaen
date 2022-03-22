from django import forms


class MatamaForm(forms.Form):
    sasalofen = forms.CharField(
        label='Sasalofen', max_length=100,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': "nga'ay ho ,o maan ko sakalafi no miso?",
        })
    )

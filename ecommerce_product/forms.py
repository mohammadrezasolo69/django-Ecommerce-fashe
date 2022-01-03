from django import forms


class AddCart(forms.Form):
    count = forms.IntegerField(min_value=1, label='', widget=forms.NumberInput(
        attrs={'class': 'size8 m-text18 t-center num-product', 'value': "1"}))

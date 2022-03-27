from django import forms
from myapp1.models import OrderItem


class OrderItemForm(forms.ModelForm):
    items_ordered = forms.IntegerField(min_value=1)

    class Meta:
        model = OrderItem
        fields = ['item','client','items_ordered']
        labels = {
            'items_ordered': 'Quantity',
            'client':'Client Name'
        }
        widgets = {'client': forms.RadioSelect}

class InterestForm(forms.Form):
    CHOICES = [(1, 'Yes'),
               (0, 'No')]
    comments=forms.Textarea()
    quantity=forms.IntegerField(initial=1)
    interested=forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect)

    class Meta:
        labels = {
            'comments': 'Additional Comments',
        }
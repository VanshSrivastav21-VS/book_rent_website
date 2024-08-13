from django import forms

class RentalForm(forms.Form):
    rental_period = forms.IntegerField(
        label='Rental Period (days)',
        min_value=1,
        max_value=30,
        initial=3,
        help_text='Enter the number of days you want to rent the book (up to 30 days).'
    )

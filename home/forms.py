from django import forms
from .models import Booking

class DateInput(forms.DateInput):
    input_type='date'
class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields="__all__"

        widgets={
            'booking_date':DateInput()
        }

        labels={
             'p_name' :"patient name:",
             'p_phone':  "patient phone",
             'p_email':"patient email",
             'doc_name':"Doctor name",
             'booking_date':"Booking date"
        }
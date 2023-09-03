from django import forms
from .models import CarbonFootprint

class CarbonFootprintForm(forms.ModelForm):
    class Meta:
        model = CarbonFootprint
        fields = '__all__'

    motorcycle = forms.BooleanField(
        required=False,
        help_text="Check this box if you travel on a motorcycle."
    )

    q_motorcycle = forms.FloatField(
        initial=0.0,
        help_text="Enter the distance traveled in kilometers."
    )

    persons_motorcycle = forms.IntegerField(
        initial=0,
        help_text="Enter the number of people traveling on the motorcycle."
    )

    car = forms.BooleanField(
        required=False,
        help_text="Check this box if you travel in a car."
    )

    q_car = forms.FloatField(
        initial=0.0,
        help_text="Enter the distance traveled in kilometers."
    )

    persons_car = forms.IntegerField(
        initial=0,
        help_text="Enter the number of people traveling in the car."
    )

    bus = forms.BooleanField(
        required=False,
        help_text="Check this box if you travel on a bus."
    )

    q_bus = forms.FloatField(
        required=0,
        help_text="Enter the number of kilometers in bus."
    )
    train = forms.BooleanField(
        required=False,
        help_text="check if you travel in train."
    )
    q_train = forms.FloatField(
        required=0,
        help_text="enter number of kilometers in train."
    )
    plane = forms.BooleanField(
        required=False,
        help_text="check if you travel in plane."
    )
    q_plane = forms.IntegerField(
        required=0,
        help_text="Enter the number of kilometers in bus."
    )
    ship = forms.BooleanField(
        required=False,
        help_text="check if you travel in a ship."
    )
    q_ship = forms.IntegerField(
        required=0,
        help_text="Enter the number of hours in ship."
    )
    def __init__(self, *args, **kwargs):
        super(CarbonFootprintForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.field.widget.__class__.__name__ == 'CheckboxInput':
                pass
            else:
                visible.field.widget.attrs['class'] = 'form-control'


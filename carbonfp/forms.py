from django import forms
from .models import CarbonFootprint 

class CarbonFootprintForm(forms.ModelForm):
    class Meta:
        model = CarbonFootprint  # Specify your model here
        fields = ['motorcycle', 'q_motorcycle', 'persons_motorcycle', 'car', 'q_car', 'persons_car', 'bus', 'q_bus', 'train', 'q_train', 'plane', 'q_plane', 'ship', 'q_ship'] 

    help_texts = {
        'motorcycle': 'Check this box if you travel on a motorcycle (two-wheeler).',
        'q_motorcycle': 'Enter the distance you travel on the motorcycle in kilometers.',
        'persons_motorcycle': 'Enter the number of people traveling on the motorcycle.',
        'car': 'Check this box if you travel in a car (four-wheeler).',
        'q_car': 'Enter the distance you travel in the car in kilometers.',
        'persons_car': 'Enter the number of people traveling in the car.',
        'bus': 'Check this box if you travel on a bus.',
        'q_bus': 'Enter the distance you travel on the bus in kilometers.',
        'train': 'Check this box if you travel on a train.',
        'q_train': 'Enter the distance you travel on the train in kilometers.',
        'plane': 'Check this box if you travel on a plane.',
        'q_plane': 'Enter the number of hours you travel on the plane.',
        'ship': 'Check this box if you travel on a ship.',
        'q_ship': 'Enter the number of hours you travel on the ship.'
    }

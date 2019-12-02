from rest_framework.serializers import ModelSerializer
from .State import State


class StateSerializer(ModelSerializer):
    class Meta:
        model = State
        fields = ('state_name', 'country_dial_code')


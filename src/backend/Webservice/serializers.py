from rest_framework import serializers
from .models import Porker


class PorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Porker
        fields = ('serial','shape','number')


from rest_framework import serializers
from Estagio import models

class EstagioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Estagio
        fields = '__all__'
from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model

User = get_user_model()

class PostagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postagem
        exclude = ('usuario',)

    def create(self, validated_data):
        user = self.context['request'].user

        validated_data['usuario'] = user

        postagem = Postagem.objects.create(**validated_data)

        return postagem
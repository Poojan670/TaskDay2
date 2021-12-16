from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model= Post
        fields= '__all__'
        extra_kwargs = {
            'created_date': {'read_only': True},
            'modified_date': {'read_only': True}
        }


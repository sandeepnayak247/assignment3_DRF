from rest_framework import serializers
from asgn_app.models import Movie

class MovieSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=100)
    genre = serializers.CharField(max_length=50)
    
    def create(self,validated_data):
        return Movie.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.description = validated_data.get('description',instance.description)
        instance.genre = validated_data.get('genre',instance.genre)
        instance.save()
        return instance
    
    def validate_name(self,value):
        if len(value)<2:
            raise serializers.ValidationError("name must be at least 2 characters")
        else:
            return value
    
 
    def validate(self,data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("name and description cannot be same")
        else:
            return data
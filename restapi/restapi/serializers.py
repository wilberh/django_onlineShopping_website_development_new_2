from rest_framework import serializers
from api.models import Talk
#I'm importing model from another app called "api" in my project, 
#not from this same app.  I was too lazy to create another model :)
#It will be different in your case


class TalkSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=80)
    speaker = serializers.CharField(max_length=80)
    venue = serializers.CharField(max_length=80)
    #duration = serializers.DurationField()
    #duration = serializers.IntegerField(required=False)
    duration = serializers.IntegerField()

    def create(self, validated_data):
        return Talk.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.speaker = validated_data.get('speaker', instance.speaker)
        instance.venue = validated_data.get('venue', instance.venue)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.save()
        return instance


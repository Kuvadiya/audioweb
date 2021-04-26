from rest_framework import serializers
from .models import Song, Audiobook, Podcast

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"

class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = "__all__"

class AudiobookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audiobook
        fields = "__all__"

class CreateSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('name','duration')

class CreatePodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = ('name','duration','host','participants')

class CreateAudiobookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audiobook
        fields = ('name','duration','author','narrator')
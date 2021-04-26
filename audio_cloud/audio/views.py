from django.shortcuts import render, get_object_or_404
from .serializars import SongSerializer, PodcastSerializer, AudiobookSerializer
from .serializars import CreateSongSerializer, CreateAudiobookSerializer, CreatePodcastSerializer
from .models import Song, Audiobook, Podcast
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import mixins
from django.http import Http404

# Create your views here.

def index(requests):
    songs = Song.objects.all()
    audiobooks = Audiobook.objects.all()
    podcasts = Podcast.objects.all()
    return render(requests,'index.html',context={'songs':songs,'audiobooks':audiobooks,'podcasts': podcasts})

class AudioCreateView(mixins.CreateModelMixin,generics.GenericAPIView):

    def get_serializer_class(self):
        if self.kwargs['type'] == 'song':
            serializer_class = CreateSongSerializer
        elif self.kwargs['type'] == 'podcast':
            serializer_class = CreatePodcastSerializer
        elif self.kwargs['type'] == 'audiobook':
            serializer_class = CreateAudiobookSerializer
        return serializer_class

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class AudioDeleteView(mixins.RetrieveModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):

    def get_queryset(self):
        if self.kwargs['type'] == 'song':
            queryset = Song.objects.all()
        elif self.kwargs['type'] == 'podcast':
            queryset = Podcast.objects.all()
        elif self.kwargs['type'] == 'audiobook':
            queryset = Audiobook.objects.all()
        return queryset
    

    def get_serializer_class(self):
        if self.kwargs['type'] == 'song':
            serializer_class = CreateSongSerializer
        elif self.kwargs['type'] == 'podcast':
            serializer_class = CreatePodcastSerializer
        elif self.kwargs['type'] == 'audiobook':
            serializer_class = CreateAudiobookSerializer
        return serializer_class
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class AudioUpdateView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,generics.GenericAPIView):

    def get_queryset(self):
        if self.kwargs['type'] == 'song':
            queryset = Song.objects.all()
        elif self.kwargs['type'] == 'podcast':
            queryset = Podcast.objects.all()
        elif self.kwargs['type'] == 'audiobook':
            queryset = Audiobook.objects.all()
        return queryset
    

    def get_serializer_class(self):
        if self.kwargs['type'] == 'song':
            serializer_class = CreateSongSerializer
        elif self.kwargs['type'] == 'podcast':
            serializer_class = CreatePodcastSerializer
        elif self.kwargs['type'] == 'audiobook':
            serializer_class = CreateAudiobookSerializer
        return serializer_class
    
    def get(self, request,pk, *args, **kwargs):
        result = self.retrieve(request,pk, *args, **kwargs)
        if result.status_code == 200:
            return result
        else:
            raise Http404

    def put(self, request, *args, **kwargs):
        result = self.update(request, *args, **kwargs)
        if result.status_code == 200:
            return result
        else:
            raise Http404
    

@api_view(['GET'])
def audio_list(requests, type ,pk=None):
    if requests.method == 'GET':
        if type:
            if type.lower() == "song":
                songs = Song.objects.all()
                serializer = SongSerializer(songs, many=True)
                if pk:
                    songs = get_object_or_404(Song,pk=pk)
                    serializer = SongSerializer(songs)
                return Response(serializer.data)
            elif type.lower() == "audiobook":
                audiobooks = Audiobook.objects.all()
                serializer = AudiobookSerializer(audiobooks, many=True)
                if pk:
                    audiobooks = get_object_or_404(Audiobook,pk=pk)
                    serializer = AudiobookSerializer(audiobooks)
                return Response(serializer.data)
            elif type.lower() == "podcast":
                podcasts = Podcast.objects.all()
                serializer = PodcastSerializer(podcasts, many=True)
                if pk:
                    podcasts = get_object_or_404(Podcast,pk=pk)
                    serializer = PodcastSerializer(podcasts)
                return Response(serializer.data)
            else:
                raise Http404


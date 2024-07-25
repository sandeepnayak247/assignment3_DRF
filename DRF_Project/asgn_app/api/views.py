from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework import status
from asgn_app.models import Movie
from asgn_app.api.serializers import MovieSerializer
from asgn_app.api.permissions import AdminOrReadOnly

class MovieBulkInsert(APIView):
    
    permission_classes = [AdminOrReadOnly]
    
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = MovieSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'description', 'genre']
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        
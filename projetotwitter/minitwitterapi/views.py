from .models import *
from rest_framework import generics, permissions
from .serializers import *
from .pagination import PaginacaoPadrao
# Create your views here.


class PostagemCriar(generics.CreateAPIView):
    #permission_classes = (permissions.IsAuthenticated,)
    
    queryset = Postagem.objects.all()
    serializer_class = PostagemSerializer


class PostagemListar(generics.ListAPIView):
    #permission_classes = (permissions.IsAuthenticated,)

    
    def get_queryset(self):
        usuario_id = self.request.user.id
        queryset = Postagem.objects.exclude(usuario = usuario_id)
        return queryset

    serializer_class = PostagemSerializer
    pagination_class = PaginacaoPadrao

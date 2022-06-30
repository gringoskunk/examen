from rest_framework.response import Response
from . serializers import productoSerializer
from rest_framework import status, generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.decorators import permission_classes
from rest_framework import permissions
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView



from . models import Producto
# Create your views here.

@permission_classes((permissions.AllowAny,))
class ProductoView(APIView):
    def get(self, request):
        obj = Producto.objects.all()      # Getting all values
        serializer = productoSerializer(obj, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        data = request.data             # Data passed in body
        serializer = productoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()           # to do post request
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)  # if error
    

class ProductoDetail(generics.RetrieveAPIView):
    queryset = Producto.objects.all()
    renderer_classes = (TemplateHTMLRenderer,)
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return Response({'Producto': self.object}, template_name='producto/producto_detail.html')
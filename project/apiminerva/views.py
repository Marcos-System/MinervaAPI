from .models import Pessoa, Aviso
from .serializers import AvisoSerializer, PessoaSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated



#################### PESSOAS ##################

class PessoaListAndCreate(APIView):
    authentication_classes = [TokenAuthentication] 
    permission_classes = [IsAuthenticated]
    def get(self, request):                  
        pessoa = Pessoa.objects.all() 
        serializer = PessoaSerializer(pessoa, many=True)
        return Response(serializer.data)
    def post(self, request):			
        serializer = PessoaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class PessoaDetailAndChangeAndDelete(APIView):
    authentication_classes = [TokenAuthentication] 
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Pessoa.objects.get(pk=pk)
        except Pessoa.DoesNotExist:
            raise NotFound()
    
    def get(self, request, pk):    
        pessoa = self.get_object(pk)
        serializer = PessoaSerializer(pessoa)
        return Response(serializer.data)
    
    def put(self, request, pk):
        pessoa = self.get_object(pk)
        serializer = PessoaSerializer(pessoa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        pessoa = self.get_object(pk)
        pessoa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    ################ AVISOS ################

class AvisoListAndCreate(APIView):
    authentication_classes = [TokenAuthentication] 
    permission_classes = [IsAuthenticated]
    def get(self, request):                  
        aviso = Aviso.objects.all() 
        serializer = AvisoSerializer(aviso, many=True)
        return Response(serializer.data)
    def post(self, request):			
        serializer = AvisoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class AvisoDetailAndChangeAndDelete(APIView):
    authentication_classes = [TokenAuthentication] 
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Aviso.objects.get(pk=pk)
        except Aviso.DoesNotExist:
            raise NotFound()
    
    def get(self, request, pk):    
        aviso = self.get_object(pk)
        serializer = PessoaSerializer(aviso)
        return Response(serializer.data)
    
    def put(self, request, pk):
        aviso = self.get_object(pk)
        serializer = AvisoSerializer(aviso, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        aviso = self.get_object(pk)
        aviso.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

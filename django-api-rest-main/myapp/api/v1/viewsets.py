from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from myapp.models import User, Exercise, Workout,Diet
from .serializers import UserSerializer,ExerciseSerializer, WorkoutSerializer ,DietSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

# Por o de treino aqui
class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [IsAuthenticated]

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = [IsAuthenticated]

class DietViewSet(viewsets.ModelViewSet):
    queryset = Diet.objects.all()
    serializer_class = DietSerializer
    permission_classes = [IsAuthenticated]

    # endpoint customizado para adicionar água
    @extend_schema(
        request={
            "application/json": {
                "type": "object",
                "properties": {
                    "value": {
                        "type": "number",
                        "description": "Quantidade de água em litros",
                        "example": 0
                    }
                },
                "required": ["value"]
            }
        },
        responses=DietSerializer,
        description="Adiciona água em litros à dieta"
    )
    
    @action(detail=True, methods=['post'])
    def add_water(self, request, pk=None):
        diet = self.get_object()
        value = float(request.data.get("value", 0))
        diet.add_water(value)
        serializer = self.get_serializer(diet)
        return Response(serializer.data)
    
    # endpoint customizado para adicionar calorias
    @extend_schema(
        request={
            "application/json": {
                "type": "object",
                "properties": {
                    "value": {
                        "type": "integer",
                        "description": "Quantidade de calorias a adicionar",
                        "example": 0
                    }
                },
                "required": ["value"]
            }
        },
        responses=DietSerializer,
        description="Adiciona calorias à dieta"
    )

    @action(detail=True, methods=['post'])
    def add_calories(self, request, pk=None):
        diet = self.get_object()
        value = int(request.data.get("value", 0))
        diet.add_calories(value)
        serializer = self.get_serializer(diet)
        return Response(serializer.data)
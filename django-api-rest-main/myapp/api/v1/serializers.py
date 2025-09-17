from rest_framework import serializers
from myapp.models import User, Exercise, Workout, Diet

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

# Por os treino nesse espaço
class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

class WorkoutSerializer(serializers.ModelSerializer):
    Exercise = ExerciseSerializer(many=True, read_only=True)
    
    class Meta:
        model = Workout
        fields = '__all__' 


class DietSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diet
        fields = '__all__'

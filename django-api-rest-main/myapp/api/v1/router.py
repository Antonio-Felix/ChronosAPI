from rest_framework.routers import DefaultRouter
from .viewsets import UserViewSet, ExerciseViewSet, WorkoutViewSet, DietViewSet

router = DefaultRouter()

# Aluno + Nutricionista + Personal
router.register(r'users', UserViewSet)

# Personal + Aluno
router.register(r'exercises', ExerciseViewSet)
router.register(r'workouts', WorkoutViewSet)

# Nutricionista + Aluno
router.register(r'diets', DietViewSet)

urlpatterns = router.urls

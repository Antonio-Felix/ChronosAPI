from django.contrib import admin

from .models import User, Exercise, Workout, Diet


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "type")
    search_fields = ("name", "email")
    list_filter = ("type",)

# Por o treino
@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ("name", "machine", "reps", "sets", "timer")
    search_fields = ("name", "machine")
    list_filter = ("machine",)

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ("name_plan", "user", "get_exercises")
    search_fields = ("name_plan", "user__username")
    list_filter = ("user",)
    filter_horizontal = ("workouts",)

    def get_exercises(self, obj):
        return ", ".join([exercise.name for exercise in obj.workouts.all()])
    get_exercises.short_description = "Exercises"

@admin.register(Diet)
class DietAdmin(admin.ModelAdmin):
    list_display = ("user", "water_meta", "calories_meta", "water_count", "calories_count", "last_reset")
    list_filter = ("last_reset",)
    search_fields = ("user__name",)
    ordering = ("-last_reset",)
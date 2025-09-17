from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.utils import timezone

class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

class BaseModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    objects = ActiveManager()
    all_objects = models.Manager()

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()

class User(BaseModel):
    TIPO_CHOICES = [
        ("A", "Aluno"),
        ("N", "Nutricionista"),
        ("P", "Personal Trainer"),
    ]
    
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    type = models.CharField(max_length=1, choices=TIPO_CHOICES)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    
    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"  

class Exercise(BaseModel):
    name = models.CharField(max_length=255)
    machine = models.CharField(max_length=255, blank=True, null=True) 
    reps = models.PositiveIntegerField()
    sets = models.PositiveIntegerField()
    timer = models.DurationField(blank=True, null=True)

    def __str__(self):
        return self.name

class Workout(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="workouts")
    name_plan = models.CharField(max_length=100)
    workouts = models.ManyToManyField(Exercise, related_name="workouts")

    def __str__(self):
        return self.name_plan

class Diet(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="diets")
    water_meta = models.FloatField(help_text="Meta diária de água em litros")
    calories_meta = models.PositiveIntegerField(help_text="Meta diária de calorias")
    water_count = models.FloatField(default=0, help_text="Quantidade de água consumida até agora")
    calories_count = models.PositiveIntegerField(default=0, help_text="Quantidade de calorias consumidas até agora")
    
    last_reset = models.DateField(auto_now_add=True)

    def _check_reset(self):
        today = timezone.now().date()
        if self.last_reset < today:
            self.water_count = 0
            self.calories_count = 0
            self.last_reset = today
            self.save()

    def add_water(self, value):
        self._check_reset()
        self.water_count += value
        self.save()
        return self.water_count

    def add_calories(self, value):
        self._check_reset()
        self.calories_count += value
        self.save()
        return self.calories_count

    def __str__(self):
        return f"Diet of {self.user.name}"

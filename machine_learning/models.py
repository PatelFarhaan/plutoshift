from uuid import uuid4
from django.db import models
from datetime import datetime


class ModelData(models.Model):
    mse_score = models.FloatField()
    uuid = models.UUIDField(default=uuid4)
    forecast_length = models.IntegerField()
    target_name = models.CharField(max_length=100)
    created = models.DateTimeField(default=datetime.utcnow)

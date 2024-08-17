from django.db import models

class POST(models.Model):
  title = models.CharField(max_length=30)
  content = models.TextField()
  
  created_at = models.DateTimeField()
  # athor : 추후 작성 예정
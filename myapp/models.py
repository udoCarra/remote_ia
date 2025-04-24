from django.db import models

class VastAIInstance(models.Model):
    instance_id = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.instance_id

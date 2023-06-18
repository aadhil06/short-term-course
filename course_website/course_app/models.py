from django.db import models

class ShortTermCourse(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    textarea = models.TextField()
    status = models.CharField(max_length=50, choices=(('Enable', 'Enable'), ('Disable', 'Disable')))
    image = models.ImageField(upload_to='course_images/',default=False)
    
    def __str__(self):
        return self.title


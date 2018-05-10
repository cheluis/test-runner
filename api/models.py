from django.db import models

# Create your models here.
class Test(models.Model):
    STATUS_CHOICES = (
        ("C", "Created"),
        ("P", "Passed"),
        ("F", "Failed")
    )

    username = models.CharField(max_length=255)
    test_enviroment_id = models.IntegerField()
    test_template = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES,
                              default="C")

    log_information = models.TextField(null=True, blank=True)

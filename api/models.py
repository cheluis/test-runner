from django.db import models

# Create your models here.
class Test(models.Model):
    TESTS_PATH = "test_runner/tests/"
    STATUS_CHOICES = (
        ("C", "Created"),
        ("P", "Passed"),
        ("F", "Failed")
    )

    TEST_TEMPLATES = (
        ('test_1.py', "Test api one"),
        ('test_2.py', "Test api two"),
        ('test_3.py', "Test api three"),
    )

    username = models.CharField(max_length=255)
    test_enviroment_id = models.IntegerField()
    test_template = models.CharField(max_length=100, null=True, blank=True, choices=TEST_TEMPLATES)
    test_script = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES,
                              default="C")

    log_information = models.TextField(null=True, blank=True)

    def get_script(self):
        if self.test_template:
            return "{}{}".format(self.TESTS_PATH, self.test_template)
        elif self.test_script:
            return self.test_script
        return ""

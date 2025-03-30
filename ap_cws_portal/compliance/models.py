from django.db import models

class GIGWRequirement(models.Model):
    section = models.CharField(max_length=20)
    requirement = models.TextField()
    implementation = models.TextField()
    test_procedure = models.TextField()
    is_implemented = models.BooleanField(default=False)
    last_verified = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)

    class Meta:
        verbose_name = "GIGW Requirement"
        ordering = ['section']

    def __str__(self):
        return f"{self.section} - {self.requirement[:50]}..."
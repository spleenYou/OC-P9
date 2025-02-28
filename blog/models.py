from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from PIL import Image


class Ticket(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(
        max_length=2048,
        blank=True
    )
    image = models.ImageField(null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Le ticket"
        verbose_name_plural = 'Les tickets'

    def resize_image(self):
        image = Image.open(self.image)
        image.thumbnail((600, 600))
        image.save(self.image.path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()


class Review(models.Model):
    ticket = models.ForeignKey("Ticket", on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    headline = models.CharField(max_length=128)
    body = models.TextField(
        max_length=8192,
        blank=True
    )
    time_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "La critique"
        verbose_name_plural = 'Les critiques'


class UserFollows(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='following',
    )
    followed_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='followed_by'
    )

    class Meta:
        unique_together = ('user', 'followed_user')
        verbose_name = "Utilisateur suivi"
        verbose_name_plural = 'Utilisateurs suivis'

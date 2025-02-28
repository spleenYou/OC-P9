from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from PIL import Image


class Ticket(models.Model):
    title = models.CharField(max_length=128, verbose_name='Titre')
    description = models.TextField(
        max_length=2048,
        blank=True
    )
    image = models.ImageField(null=True, blank=True)
    time_created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Date de création',)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='utilisateur',
    )

    def __str__(self):
        "Display for admin page"
        return self.title

    class Meta:
        verbose_name = "Le ticket"
        verbose_name_plural = 'Les tickets'

    def resize_image(self):
        "Resize image"

        image = Image.open(self.image)
        image.thumbnail((600, 600))
        image.save(self.image.path)

    def save(self, *args, **kwargs):
        "Resize image when saving a ticket"

        super().save(*args, **kwargs)
        if self.image:
            self.resize_image()


class Review(models.Model):
    ticket = models.ForeignKey("Ticket", on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        verbose_name='Note',
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='utilisateur',
    )
    headline = models.CharField(
        max_length=128,
        verbose_name='Titre',
    )
    body = models.TextField(
        max_length=8192,
        blank=True
    )
    time_created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='date de création',
    )

    def __str__(self):
        "Display for admin page"
        return f"Réponse à {self.ticket.user.username}"

    class Meta:
        verbose_name = "La critique"
        verbose_name_plural = 'Les critiques'


class UserFollows(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='utilisateur'
    )
    followed_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='followed_by',
        verbose_name='Utilisateur suivi'
    )

    class Meta:
        unique_together = ('user', 'followed_user')
        verbose_name = "Utilisateur suivi"
        verbose_name_plural = 'Utilisateurs suivis'

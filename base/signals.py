from django.db.models.signals import pre_save,post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Cart


def updateUser(sender, instance, **kwargs):
    user = instance
    if user.email != '':
        user.username = user.email


pre_save.connect(updateUser, sender=User)

@receiver(post_save, sender=User)
def create_user_cart(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user=instance)

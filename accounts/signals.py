from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from accounts.models import User, UserProfile


# Using decorator method
@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender, instance, created, **kwargs):
    print(created)
    if created:
        UserProfile.objects.create(user=instance)
    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()  # ✅ fixed indentation
        except UserProfile.DoesNotExist:
            # Create the user profile if it doesn’t exist
            UserProfile.objects.create(user=instance)


@receiver(pre_save, sender=User)  # ✅ fixed comma and capitalized 'User'
def pre_save_profile_receiver(sender, instance, **kwargs):
    pass

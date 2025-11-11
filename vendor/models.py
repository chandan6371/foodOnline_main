from django.db import models
from accounts.models import User,UserProfile
from accounts.utils import send_notification

# Create your models here.

class vendor(models.Model):
    user = models.OneToOneField(User, related_name='vendor', on_delete=models.CASCADE)
    user_profile = models.OneToOneField(UserProfile, related_name='vendor_profile', on_delete=models.CASCADE)
    vendor_name = models.CharField(max_length=120)
    vendor_license = models.ImageField(upload_to='vendor/license')
    is_approved = models.BooleanField(default=False)
    created_at = models.DateField(auto_now=True)
    modified_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.vendor_name
    
    def save(self, *args, **kwargs):
        if self.pk is not None:
        # update
          orig = vendor.objects.get(pk=self.pk)
        if orig.is_approved != self.is_approved:
            context = {
                'user': self.user,
                'is_approved': self.is_approved,
            }
            # Only send the notification after variables are set!
            if self.is_approved:  # Approved
                mail_subject = "Congratulations! Your restaurant has been approved"
                mail_template = "accounts/emails/admin_approval_email.html"
                send_notification(mail_subject, mail_template, context)
            else:  # Not approved
                mail_subject = "We are sorry, you are not eligible to publish your food menu"
                mail_template = "accounts/emails/admin_approval_email.html"
                send_notification(mail_subject, mail_template, context)
                return super(vendor, self).save(*args, **kwargs)

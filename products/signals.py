import os

from django.db import models
from django.dispatch import receiver

from .models import Product


@receiver(models.signals.post_delete, sender=Product)
def delete_image_file_on_product_delete(sender, instance, using, **kwargs):
    """
    Deletes files from the filesystem/cloud storage
    when the corresponding `Product` object is deleted.
    """
    if instance.image:
        try:
            # # delete image file for development
            # if os.path.isfile(instance.image.path):
            #     os.remove(instance.image.path)

            # delete image file for aws s3
            instance.image.delete(save=False)
        except FileNotFoundError:
            pass

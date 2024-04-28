# Reference- https://docs.djangoproject.com/en/4.2/ref/models/fields/#field-types


from django.db import models


class CreatedModifiedBaseModel(models.Model):
    """
    Base Model to store created_on and modified_on of an object instance
    """

    created_on = models.DateTimeField(
        auto_now_add=True,
        help_text="Datetime when this object was created",
    )
    modified_on = models.DateTimeField(
        auto_now=True,
        help_text="Datetime when this object was last modified",
    )

    class Meta:
        abstract = True

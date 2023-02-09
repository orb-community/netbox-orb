from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import PolicyNetProbe

@receiver(m2m_changed, sender=PolicyNetProbe)
def m2m_changed_func(sender, instance, action, **kwargs):
    if (action == 'post_add') or (action == 'post_remove'):
        instance.save()

m2m_changed.connect(m2m_changed_func)

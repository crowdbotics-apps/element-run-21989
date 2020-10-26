from django.contrib import admin
from .models import (
    Course,
    Category,
    Enrollment,
    SubscriptionType,
    Module,
    Group,
    Subscription,
    Event,
    Recording,
)

admin.site.register(Category)
admin.site.register(Group)
admin.site.register(Module)
admin.site.register(Event)
admin.site.register(Subscription)
admin.site.register(Recording)
admin.site.register(SubscriptionType)
admin.site.register(Course)
admin.site.register(Enrollment)

# Register your models here.

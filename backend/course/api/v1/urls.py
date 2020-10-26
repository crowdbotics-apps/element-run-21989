from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    CourseViewSet,
    CategoryViewSet,
    LessonViewSet,
    EnrollmentViewSet,
    SubscriptionTypeViewSet,
    PaymentMethodViewSet,
    ModuleViewSet,
    GroupViewSet,
    SubscriptionViewSet,
    EventViewSet,
    RecordingViewSet,
)

router = DefaultRouter()
router.register("category", CategoryViewSet)
router.register("group", GroupViewSet)
router.register("paymentmethod", PaymentMethodViewSet)
router.register("lesson", LessonViewSet)
router.register("module", ModuleViewSet)
router.register("event", EventViewSet)
router.register("subscription", SubscriptionViewSet)
router.register("recording", RecordingViewSet)
router.register("subscriptiontype", SubscriptionTypeViewSet)
router.register("course", CourseViewSet)
router.register("enrollment", EnrollmentViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

from rest_framework.routers import DefaultRouter

from apps.teams.api.views import TeamApiViewSet

router = DefaultRouter()
router.register(
    r'teams',
    TeamApiViewSet
    )

urlpatterns = router.urls

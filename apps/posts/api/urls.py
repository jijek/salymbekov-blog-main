from rest_framework.routers import DefaultRouter

from apps.posts.api.views import PostApiViewSet

router = DefaultRouter()
router.register(
    r'posts',
    PostApiViewSet
)

urlpatterns = router.urls

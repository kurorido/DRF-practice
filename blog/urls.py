from blog.views import UserViewSet, ArticleViewSet, TagViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'tags', TagViewSet)
urlpatterns = router.urls
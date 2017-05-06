from rest_framework.routers import SimpleRouter
from alonesoul.example import views


router = SimpleRouter()

router.register(r'category', views.CategoryViewSet, 'Category')
router.register(r'post', views.PostViewSet, 'Post')

urlpatterns = router.urls

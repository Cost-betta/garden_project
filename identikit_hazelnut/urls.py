from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'cultivars', views.CultivarViewSet, basename='cultivars')
router.register(r'alleles', views.AlleleViewSet, basename='alleles')
router.register(r'nuts', views.NutViewSet, basename='nuts')
router.register(r'leafs', views.LeafViewSet, basename='leafs')

urlpatterns = router.urls
app_name = __package__

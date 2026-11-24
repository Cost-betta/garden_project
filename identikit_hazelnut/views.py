from rest_framework import viewsets
from . import models, filters, serializers as srlz


class CultivarViewSet(viewsets.ModelViewSet):
    """Вьюсет сортов с операциями CRUD."""

    queryset = models.Cultivar.objects.all()
    serializer_class = srlz.CultivarSerializer
    filterset_class = filters.CultivarFilter


class AlleleViewSet(viewsets.ModelViewSet):
    """Вьюсет аллелей с операциями CRUD."""

    queryset = models.Allele.objects.all()
    serializer_class = srlz.AlleleSerializer
    filterset_class = filters.AlleleFilter


class NutViewSet(viewsets.ModelViewSet):
    """Вьюсет орехов с операциями CRUD."""

    queryset = models.Nut.objects.all()
    serializer_class = srlz.NutSerializer
    filterset_class = filters.NutFilter


class LeafViewSet(viewsets.ModelViewSet):
    """Вьюсет листьев с операциями CRUD."""

    queryset = models.Leaf.objects.all()
    serializer_class = srlz.LeafSerializer
    filterset_class = filters.LeafFilter

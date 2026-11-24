from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from django_filters import rest_framework as filters
from rest_framework.exceptions import ValidationError
from . import models


class CultivarFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')  # фильтрует только по полям указанным здесь
    country = filters.CharFilter(lookup_expr='icontains')
    region = filters.CharFilter(lookup_expr='icontains')
    alleles = filters.CharFilter(
        label=_('Alleles'),
        method='get_by_alleles',
        help_text=_('Sorting cultivars by alleles.')
    )
    names = filters.CharFilter(
        label=_('Names'),
        method='get_cultivars_by_names',
        help_text=_('Search cultivars by names.')
    )
    pollinators = filters.CharFilter(
        label=_('Pollinators'),
        method='get_pollinators',
        help_text=_('Pollinators for the cultivar.')
    )

    def get_by_alleles(self, queryset, name, value):
        if '_' in value:
            alleles = value.split('_')
            if len(alleles) != 2:
                raise ValidationError(
                    _(
                        f'The number of alleles has been exceeded. Expected: 2_15/ or 10/_24/, actual: {value}.'
                    )
                )
            return queryset.filter(
                (Q(allele__allele_1=alleles[0]) & Q(allele__allele_2=alleles[1])) |
                (Q(allele__allele_2=alleles[0]) & Q(allele__allele_1=alleles[1]))
            )
        else:
            alleles = value.split(',')
            return queryset.filter(Q(allele__allele_1__in=alleles) | Q(allele__allele_2__in=alleles))

    def get_cultivars_by_names(self, queryset, name, value):
        query = Q()
        for name in value.split(','):
            query |= Q(name__icontains=name)  # Оператор |= выполняет логическое ИЛИ
        return queryset.filter(query)

    def get_pollinators(self, queryset, name, value):
        if ',' in value:
            raise ValidationError(
                _(
                    f'Рollinators are calculated only for one сultivar, Value received: {value}.'
                )
            )
        instances = list(models.Cultivar.objects.filter(name__icontains=value))
        alleles = []
        if instances:
            for allele in [instances[0].allele.allele_1, instances[0].allele.allele_2]:
                alleles.append(allele)
                if '/' in allele:
                    alleles.append(allele.replace('/',''))
                else:
                    alleles.append(allele + '/')
        else:
            raise ValidationError(_(f'Cultivar {value} not found.'))
        return queryset.exclude(allele__allele_1__in=alleles).exclude(allele__allele_2__in=alleles)

    class Meta:
        model = models.Cultivar
        fields = '__all__'


class AlleleFilter(filters.FilterSet):
    allele_1 = filters.CharFilter(lookup_expr='exact')  # фильтрует только по полям указанным здесь
    allele_2 = filters.CharFilter(lookup_expr='exact')

    class Meta:
        model = models.Allele
        fields = '__all__'


class NutFilter(filters.FilterSet):
    shape = filters.CharFilter(lookup_expr='exact')
    length = filters.NumberFilter()
    width = filters.NumberFilter()
    thickness = filters.NumberFilter()
    kernel_yield = filters.NumberFilter()
    shell_thickness = filters.NumberFilter()
    kernel_skin = filters.BooleanFilter()

    class Meta:
        model = models.Nut
        fields = '__all__'


class LeafFilter(filters.FilterSet):
    color = filters.CharFilter(lookup_expr='exact')  # фильтрует только по полям указанным здесь

    class Meta:
        model = models.Leaf
        fields = '__all__'

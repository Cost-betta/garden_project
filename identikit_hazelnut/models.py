from django.template.defaultfilters import title
from enumchoicefield import EnumChoiceField
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from .enums import ColorLeafType, CountryType, ShapeNutType, RegionType


class Allele(models.Model):
    """Аллели в цветах и сережках"""

    allele_1 = models.CharField(
        _('Allele 1'),
        max_length=4,
        blank=True,
        default="",
        validators=[RegexValidator(regex=r'^\d{1,2}\/?$')],
    )
    allele_2 = models.CharField(
        _('Allele 2'),
        max_length=4,
        blank=True,
        default="",
        validators=[RegexValidator(regex=r'^\d{1,2}\/?$')],
    )


class Leaf(models.Model):
    """Описание листа"""

    color = EnumChoiceField(
        ColorLeafType,
        blank=True,
        default=ColorLeafType.UNKNOWN
    )
    description = models.CharField(
        _('Description'),
        max_length=500,
        blank=True,
        default="",
    )


class Nut(models.Model):
    """Описание ореха"""

    shape = EnumChoiceField(
        ShapeNutType,
        blank=True,
        default=ShapeNutType.UNKNOWN
    )
    length = models.IntegerField(
        _('Length'),
        validators=[MinValueValidator(10), MaxValueValidator(50)],
        null=True,
        blank=True,
    )
    width = models.IntegerField(
        _('Width'),
        validators=[MinValueValidator(5), MaxValueValidator(30)],
        null=True,
        blank=True,
    )
    thickness = models.IntegerField(
        _('Thickness'),
        validators=[MinValueValidator(5), MaxValueValidator(30)],
        null=True,
        blank=True,
    )
    kernel_yield = models.IntegerField(
        _('Kernel yield'),
        validators=[MinValueValidator(20), MaxValueValidator(80)],
        null=True,
        blank=True,
    )
    shell_thickness = models.FloatField(
        _('Shell thickness'),
        validators=[MinValueValidator(0.1), MaxValueValidator(4)],
        null=True,
        blank=True,
    )
    weight = models.FloatField(
        _('Weight'),
        validators=[MinValueValidator(1.0), MaxValueValidator(11.0)],
        null=True,
        blank=True,
    )
    kernel_skin = models.BooleanField(
        _('Kernel skin'),
        null= True,
        blank=True,
    )
    description = models.CharField(
        _('Description'),
        max_length=500,
        blank=True,
        default="",
    )


class Cultivar(models.Model):
    """Сорт"""

    name = models.CharField(
        _('Name'),
        max_length=100,
        unique=True,
    )
    country = EnumChoiceField(
        CountryType,
        blank=True,
        default=CountryType.UNKNOWN
    )
    region = EnumChoiceField(
        RegionType,
        blank=True,
        default=RegionType.UNKNOWN
    )
    allele = models.ForeignKey(
        Allele,
        on_delete=models.PROTECT,
        verbose_name=_('Allele'),
        related_name='allele',
    )
    leaf = models.ForeignKey(
        Leaf,
        on_delete=models.PROTECT,
        verbose_name=_('Leaf'),
        related_name='leaf',
    )
    nut = models.ForeignKey(
        Nut,
        on_delete=models.PROTECT,
        verbose_name=_('Nut'),
        related_name='nut',
    )
    description = models.CharField(
        _('Description'),
        max_length=2000,
        blank=True,
        default="",
    )
    famous = models.BooleanField(
        _('Famous'),
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ['name']

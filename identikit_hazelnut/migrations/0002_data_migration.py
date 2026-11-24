from __future__ import unicode_literals
from django.db import migrations
from ..enums import CountryType, RegionType, ShapeNutType, ColorLeafType


def data_migration(apps, schema_editor):
    """Заполнение БД первичными данными"""

    Cultivar = apps.get_model('identikit_hazelnut.Cultivar')
    Allele = apps.get_model('identikit_hazelnut.Allele')
    Leaf = apps.get_model('identikit_hazelnut.Leaf')
    Nut = apps.get_model('identikit_hazelnut.Nut')
    country_dict = {country_type.verbose_name : country_type for country_type in list(CountryType)}
    region_dict = {region_type.verbose_name: region_type for region_type in list(RegionType)}
    with open('identikit_hazelnut/fixtures/data.csv', 'r', encoding='utf-8') as file:
        content_rows = file.read().split('\n')
        first_row = True
        for row in content_rows:
            if not first_row:
                group, cultivar, origin, alleles = row.split(';')
                alleles_s = alleles.replace('[', '').replace(']', '').replace("'", '').replace("^", '/').replace(" ", "").split(',')
                leaf = Leaf(color=ColorLeafType.UNKNOWN)
                leaf.save()
                nut = Nut(shape=ShapeNutType.UNKNOWN)
                nut.save()
                allele = Allele(
                    allele_1=alleles_s[0],
                    allele_2=alleles_s[1]
                )
                allele.save()
                cultivar = Cultivar(
                    name=cultivar,
                    country=country_dict[origin],
                    region=region_dict[group],
                    allele=allele,
                    leaf=leaf,
                    nut=nut,
                    description=""
                )
                cultivar.save()

            else:
                first_row = False
                continue

class Migration(migrations.Migration):

    dependencies = [
        ('identikit_hazelnut', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(data_migration),
    ]

from identikit_hazelnut.models import Allele, Cultivar, Leaf, Nut
from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer


class AlleleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Allele
        fields = '__all__'

    def create(self, validated_data):
        """
        Create and return a new `Allele` instance, given the validated data.
        """
        return Allele.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Allele` instance, given the validated data.
        """
        instance.allele_1 = validated_data.get('allele_1', instance.allele_1)
        instance.allele_2 = validated_data.get('allele_2', instance.allele_2)
        instance.save()
        return instance


class LeafSerializer(serializers.ModelSerializer):

    class Meta:
        model = Leaf
        fields = '__all__'

    def create(self, validated_data):
        """
        Create and return a new `Leaf` instance, given the validated data.
        """
        return Leaf.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Leaf` instance, given the validated data.
        """
        instance.color = validated_data.get('color', instance.color)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class NutSerializer(serializers.ModelSerializer):

    class Meta:
        model = Nut
        fields = '__all__'

    def create(self, validated_data):
        """
        Create and return a new `Nut` instance, given the validated data.
        """
        return Nut.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Nut` instance, given the validated data.
        """
        instance.shape = validated_data.get('shape', instance.shape)
        instance.length = validated_data.get('length', instance.length)
        instance.width = validated_data.get('width', instance.width)
        instance.thickness = validated_data.get('thickness', instance.thickness)
        instance.kernel_yield = validated_data.get('kernel_yield', instance.kernel_yield)
        instance.shell_thickness = validated_data.get('shell_thickness', instance.shell_thickness)
        instance.kernel_skin = validated_data.get('kernel_skin', instance.kernel_skin)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class CultivarSerializer(FlexFieldsModelSerializer):

    class Meta:
        model = Cultivar
        fields = '__all__'
        expandable_fields = {
            'allele': 'identikit_hazelnut.serializers.AlleleSerializer',
            'leaf': 'identikit_hazelnut.serializers.LeafSerializer',
            'nut': 'identikit_hazelnut.serializers.NutSerializer',
        }

    def create(self, validated_data):
        """
        Create and return a new `Cultivar` instance, given the validated data.
        """
        return Cultivar.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Cultivar` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.country = validated_data.get('country', instance.country)
        instance.region = validated_data.get('region', instance.region)
        instance.allele = validated_data.get('allele', instance.allele)
        instance.leaf = validated_data.get('leaf', instance.leaf)
        instance.nut = validated_data.get('nut', instance.nut)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

from rest_framework import serializers
from .models import Language, Programer, Paradigm, Purchase


class LanguageSerializer(serializers.HyperlinkedModelSerializer):

	class Meta():
		model = Language
		fields = ('id', 'url', 'name')


class ProgramerSerializer(serializers.HyperlinkedModelSerializer):

	class Meta():
		model = Programer
		fields = ('id', 'url', 'name', 'language')


class ParadigmSerializer(serializers.HyperlinkedModelSerializer):

	class Meta():
		model = Paradigm
		fields = ('id', 'url', 'name')






from rest_framework import serializers

from . models import Movies

class MoviesSerializer(serializers.ModelSerializer):

    class Meta :

        models = Movies

        fields = '_all_'

        read_only_fields = ['uuid','active_status']
from rest_framework import serializers
from polls.models import Result
class ResultSerializer(serializers.ModelSerializer):
 class Meta:
    model = Result
    fields = ['UserName', 'DateTime', 'Rating']
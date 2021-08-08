from rest_framework import serializers
from leads.models import Leads

# Lead Serializer
class LeadsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leads
        fields = '__all__'

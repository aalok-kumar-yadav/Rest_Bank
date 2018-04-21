from rest_framework import serializers
from .models import bank_branch


class ifscbranchdetailsSerializers(serializers.ModelSerializer):

    class Meta:
        model = bank_branch
        fields = ('bank_id',  'bank_name', 'branch', 'address', 'city', 'district', 'state')


class citybranchdetailsSerializers(serializers.ModelSerializer):

    class Meta:
        model = bank_branch
        fields = ( 'bank_id','ifsc', 'branch', 'address', 'district', 'state')

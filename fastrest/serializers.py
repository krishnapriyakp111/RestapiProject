# serializers --> interaction between API & appliation will be in json/xml format. Inorder to do this conversion between python and json representation of data serializers are used.
from rest_framework import serializers
from .models import emp_details

Users=emp_details()

class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = emp_details
        # fields = ('id','f_name', 'l_name', 'emp_id')
        fields = '__all__'
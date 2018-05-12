from rest_framework import serializers
from .models import Test


class TestSerializer(serializers.ModelSerializer):
    script_tested = serializers.ReadOnlyField()

    class Meta:
        model = Test
        fields = ('id', 'username', 'test_enviroment_id', 'test_template',
                  'test_script', 'status', 'script_tested', 'created_at')
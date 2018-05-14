from rest_framework import serializers
from .models import Test


class TestSerializer(serializers.ModelSerializer):
    script_tested = serializers.ReadOnlyField()

    def validate(self, attrs):
        try:
            Test.objects.get(test_enviroment_id=attrs['test_enviroment_id'],
                             status="C")
        except Test.DoesNotExist:
            pass
        else:
            raise serializers.ValidationError('Test running on given environment')

        return attrs

    class Meta:
        model = Test
        fields = ('id', 'username', 'test_enviroment_id', 'test_template',
                  'test_script', 'status', 'script_tested', 'created_at', 'log_information')
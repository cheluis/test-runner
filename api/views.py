from rest_framework import viewsets

from api.models import Test
from api.serializers import TestSerializer

from .task import run_script

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

    def create(self, request, *args, **kwargs):
        ret = super(TestViewSet, self).create(request, *args, **kwargs)

        run_script.delay(ret.data["id"])

        return ret
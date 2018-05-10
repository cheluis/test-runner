from rest_framework import viewsets

from api.models import Test
from api.serializers import TestSerializer
from .task import mul


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

    def create(self, request, *args, **kwargs):
        ret = super(TestViewSet, self).create(request, *args, **kwargs)
        mul.delay(2, 2)
        return ret
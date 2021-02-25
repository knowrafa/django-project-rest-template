from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from sample.models import Sample
from sample.serializers import SampleSerializer


class SampleViewSet(viewsets.GenericViewSet,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin):

    queryset = Sample.objects.all()
    serializer_class = SampleSerializer()
    permission_classes = (IsAuthenticated, )

    def create(self, request, *args, **kwargs):
        return super(SampleViewSet, self).create(request, args, kwargs)

    def update(self, request, *args, **kwargs):
        return super(SampleViewSet, self).update(request, args, kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(SampleViewSet, self).retrieve(request, args, kwargs)

    def list(self, request, *args, **kwargs):
        return super(SampleViewSet, self).list(request, args, kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(SampleViewSet, self).update(request, args, kwargs)

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from ..models import Job
from ..serializers import JobSerializer


class JobDetailView(GenericAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    lookup_field = 'id'

    def get(self, request):
        return Response(self.get_serializer(self.get_object()).data)

from rest_framework.generics import RetrieveAPIView

from ..models import Job
from ..serializers import JobSerializer


class JobDetailView(RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    lookup_field = 'id'

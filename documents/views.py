from django.core.files import File
from django.http import HttpResponse
from rest_framework import views, viewsets

from .models import Document, Folder, Topic
from .serializers import DocumentSerializer, FolderSerializer, TopicSerializer


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class FolderViewSet(viewsets.ModelViewSet):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer

    def get_queryset(self):
        queryset = Document.objects.all()
        topic = self.request.query_params.get("topic")
        if topic is not None:
            queryset = queryset.filter(topic__name=topic)
        return queryset


class DocumentView(views.APIView):

    def get(self, request, *args, **kwargs):
        with open(f"data/{kwargs['file_name']}", 'rb') as file:
            response = HttpResponse(File(file), content_type='application/zip')
            response['Content-Disposition'] = f'attachment; filename="{kwargs["file_name"]}"'
            return response

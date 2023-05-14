from rest_framework import serializers
from .models import Document, Folder, Topic


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class FolderSerializer(serializers.ModelSerializer):
    structure = serializers.SerializerMethodField()

    def get_structure(self, instance):
        folders = [{
            "name": child.name,
            "type": "folder"
        } for child in instance.child_folders.all()
        ]

        documents = [
            {
                "name": document.name,
                "topic": document.topic.name,
                "file": document.file,
                "type": "document"
            } for document in instance.documents.all()
        ]
        return folders + documents

    class Meta:
        model = Folder
        fields = '__all__'


class DocumentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)

    def create(self, validated_data):
        validated_data["name"] = validated_data['file'].name
        return super().create(validated_data)

    class Meta:
        model = Document
        fields = '__all__'

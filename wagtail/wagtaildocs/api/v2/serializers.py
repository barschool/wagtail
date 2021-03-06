from __future__ import absolute_import, unicode_literals

from rest_framework.fields import Field

from wagtail.api.v2.serializers import BaseSerializer
from wagtail.api.v2.utils import get_full_url


class DocumentDownloadUrlField(Field):
    """
    Serializes the "download_url" field for documents.

    Example:
    "download_url": "http://api.example.com/documents/1/my_document.pdf"
    """
    def get_attribute(self, instance):
        return instance

    def to_representation(self, document):
        return get_full_url(self.context['request'], document.url)


class DocumentSerializer(BaseSerializer):
    download_url = DocumentDownloadUrlField(read_only=True)

    default_fields = BaseSerializer.default_fields + [
        'download_url',
    ]

    meta_fields = BaseSerializer.meta_fields + [
        'download_url',
    ]

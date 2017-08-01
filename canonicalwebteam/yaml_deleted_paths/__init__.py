# Core packages
import os

# Third party packages
from django.conf import settings
from django.http import HttpResponseGone
from django.template.loader import get_template
from canonicalwebteam.views_from_yaml import create_views_from_file


def _show_deleted_page(request, path_context):
    template = get_template('410.html')
    page_content = template.render(path_context, request)

    return HttpResponseGone(page_content)


def create_views():
    deleted_paths_filepath = os.path.join(settings.BASE_DIR, 'deleted.yaml')

    return create_views_from_file(
        deleted_paths_filepath,
        _show_deleted_page
    )

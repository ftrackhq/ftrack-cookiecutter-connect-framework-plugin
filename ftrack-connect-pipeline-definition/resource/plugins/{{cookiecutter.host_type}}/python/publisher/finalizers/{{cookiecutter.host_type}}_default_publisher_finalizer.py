# :coding: utf-8
# :copyright: Copyright (c) 2014-{{cookiecutter.year}} ftrack

import os
from ftrack_connect_pipeline_{{cookiecutter.host_type}} import plugin
import ftrack_api


class {{cookiecutter.host_type_capitalized}}DefaultPublisherFinalizerPlugin(plugin.{{cookiecutter.host_type_capitalized}}PublisherFinalizerPlugin):
    plugin_name = '{{cookiecutter.host_type}}_default_publisher_finalizer'

    def run(self, context_data=None, data=None, options=None):
        '''{{cookiecutter.host_type_capitalized}} finalizer plugin'''
        return {}


def register(api_object, **kw):
    if not isinstance(api_object, ftrack_api.Session):
        # Exit to avoid registering this plugin again.
        return
    plugin = {{cookiecutter.host_type_capitalized}}DefaultPublisherFinalizerPlugin(api_object)
    plugin.register()

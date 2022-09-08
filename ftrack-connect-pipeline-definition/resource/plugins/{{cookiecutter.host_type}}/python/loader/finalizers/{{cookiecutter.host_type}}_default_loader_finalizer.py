# :coding: utf-8
# :copyright: Copyright (c) 2014-2022 ftrack

import ftrack_api

from ftrack_connect_pipeline_{{cookiecutter.host_type}} import plugin
from ftrack_connect_pipeline_{{cookiecutter.host_type}}.utils import custom_commands as {{cookiecutter.host_type}}_utils
from ftrack_connect_pipeline_{{cookiecutter.host_type}}.constants.asset import modes as load_const


class {{cookiecutter.host_type_capitalized}}DefaultLoaderFinalizerPlugin(plugin.{{cookiecutter.host_type_capitalized}}LoaderFinalizerPlugin):
    plugin_name = '{{cookiecutter.host_type}}_default_loader_finalizer'


def register(api_object, **kw):
    if not isinstance(api_object, ftrack_api.Session):
        # Exit to avoid registering this plugin again.
        return
    plugin = {{cookiecutter.host_type_capitalized}}DefaultLoaderFinalizerPlugin(api_object)
    plugin.register()

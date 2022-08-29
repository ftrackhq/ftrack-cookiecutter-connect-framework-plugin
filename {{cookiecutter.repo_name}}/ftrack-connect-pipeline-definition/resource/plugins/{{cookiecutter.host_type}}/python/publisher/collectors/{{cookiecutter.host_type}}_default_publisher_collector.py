# :coding: utf-8
# :copyright: Copyright (c) 2014-{{cookiecutter.year}} ftrack

# import maya.cmds as cmds

from ftrack_connect_pipeline_{{cookiecutter.host_type}} import plugin
import ftrack_api


class {{cookiecutter.host_type|capitalize}}DefaultPublisherCollectorPlugin(plugin.{{cookiecutter.host_type|capitalize}}PublisherCollectorPlugin):
    plugin_name = '{{cookiecutter.host_type}}_default_publisher_collector'

    def select(self, context_data=None, data=None, options=None):
        '''Select all the items of the plugin *options*'''
        selected_items = options.get('selected_items', [])
        # cmds.select(cl=True)
        # for item in selected_items:
        #    cmds.select(item, add=True)
        return selected_items

    def fetch(self, context_data=None, data=None, options=None):
        '''Fetch all selected items'''
        # collected_objects = cmds.ls(sl=True, l=True)
        return collected_objects

    def add(self, context_data=None, data=None, options=None):
        '''Return the selected items of the scene'''
        # selected_objects = cmds.ls(sl=True, l=True)
        return selected_objects

    def run(self, context_data=None, data=None, options=None):
        '''Return all the collected objects in the widget from the
        plugin *options*'''
        collected_objects = options.get('collected_objects', [])
        return collected_objects


def register(api_object, **kw):
    if not isinstance(api_object, ftrack_api.Session):
        # Exit to avoid registering this plugin again.
        return
    plugin = {{cookiecutter.host_type|capitalize}}DefaultPublisherCollectorPlugin(api_object)
    plugin.register()

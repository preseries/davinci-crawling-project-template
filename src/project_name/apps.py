# -*- coding: utf-8 -*
# Copyright (c) 2018-2019 BuildGroup Data Services Inc.
# All rights reserved.

from django.apps import AppConfig


class DaVinciCrawlerConfig(AppConfig):
    name = '{{ project_name }}'
    verbose_name = "Django DaVinci Crawler {{ project_name }}"

    def ready(self):
        from {{project_name | lower}}.api import serializers
        # Add System checks
        # from .checks import pagination_system_check  # NOQA

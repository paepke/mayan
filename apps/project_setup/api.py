from __future__ import absolute_import

from . import setup_link

setup_items = []


def register_setup(link):
    setup_items.append(link)
    if 'children_view_regex' in link:
        setup_link.setdefault('children_view_regex', [])
        setup_link['children_view_regex'].extend(link['children_view_regex'])

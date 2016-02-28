# -*- coding: utf-8 -*-
from .proxy import get_content
from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.publisher.interfaces import IPublishTraverse


# TODO: caching


@implementer(IPublishTraverse)
class ProxyView(BrowserView):

    def get_content(self):
        return get_content(self.context.remote_url)

    # Traverser

    """
    def __call__(self):
        return getattr(self, 'subpath', self())

    def publishTraverse(self, request, name):
        if not hasattr(self, 'subpath'):
            self.subpath = []
        self.subpath.append(name)
        return self
    """

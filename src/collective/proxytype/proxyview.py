# -*- coding: utf-8 -*-
from .proxy import get_content
from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.publisher.interfaces import IPublishTraverse
# TODO: caching


@implementer(IPublishTraverse)
class ProxyView(BrowserView):
    subpath = []

    def get_content(self):
        url = self.context.remote_url
        if self.subpath:
            url = '/'.join([url.rstrip('/')] + self.subpath)
        # TODO:
        # - on non-HTML content (JS/CSS/IMGS), don't use template
        # - on HTML content, onle inject body in template
        # - make sure, request params are also used
        return get_content(url)

    # Traverser

    def publishTraverse(self, request, name):
        """Subpath traverser
        """
        self.subpath.append(name)
        return self

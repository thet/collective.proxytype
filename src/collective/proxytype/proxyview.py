from .proxy import get_content
from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.publisher.interfaces import IPublishTraverse


# TODO: traverser for urls pointing into context's url space
# TODO: caching


@implementer(IPublishTraverse)
class ProxyView(BrowserView):

    def get_content(self):
        return get_content(
            self.context.remote_url,
            self.context.absolute_url(),
            self.context.url_replacement_map
        )

    # Traverser

    def __call__(self):
        return self.subpath

    def publishTraverse(self, request, name):
        if not hasattr(self, 'subpath'):
            self.subpath = []
        self.subpath.append(name)
        return self

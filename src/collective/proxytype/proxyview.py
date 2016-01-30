from .proxy import get_content
from Products.Five import BrowserView


# TODO: traverser for urls pointing into context's url space
# TODO: caching


class ProxyView(BrowserView):

    def get_content(self):
        return get_content(
            self.context.remote_url,
            self.context.absolute_url(),
            self.context.url_replacement_map
        )

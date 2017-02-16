# -*- coding: utf-8 -*-
from .proxy import get_content
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from urllib import urlencode
from zope.interface import implementer
from zope.publisher.interfaces import IPublishTraverse

import urlparse


# TODO: caching


@implementer(IPublishTraverse)
class ProxyView(BrowserView):

    content = None

    def publishTraverse(self, request, name):
        """Subpath traverser
        """
        if getattr(self, 'subpath', None) is None:
            self.subpath = []
        self.subpath.append(name)
        return self

    def __call__(self):

        url = self.context.remote_url

        # url_parts[2] .. path
        # url_parts[4] .. query string
        url_parts = list(urlparse.urlparse(url))

        # Update path
        subpath = getattr(self, 'subpath', [])
        if subpath:
            url_parts[2] = '/'.join([url_parts[2].rstrip('/')] + subpath)

        # Update query string
        query = dict(urlparse.parse_qsl(url_parts[4]))
        query.update(self.request.form)
        url_parts[4] = urlencode(query)

        url = urlparse.urlunparse(url_parts)

        self.content, content_type = get_content(
            url,
            getattr(self.context, 'content_selector', None),
            getattr(self.context, 'append_script', None),
            getattr(self.context, 'append_link', None),
            getattr(self.context, 'append_style', None)
        )

        if 'text/html' not in content_type:
            self.request.response.setHeader('Content-type', content_type)
            return self.content

        return ViewPageTemplateFile('proxyview.pt')(self)

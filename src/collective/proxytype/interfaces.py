"""Module where all interfaces, events and exceptions live."""

from collective.proxytype import _
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IBrowserLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IProxy(Interface):
    """Marker interface for Proxy types.
    """


class IProxySchema(Interface):
    """Schema interface for the Proxy type and portlet.
    """

    remote_url = schema.TextLine(
        title=_(u"Remote URL"),
        required=True,
    )

    url_replacement_map = schema.Text(
        title=_(u"URL replacement map"),
        required=False,
    )

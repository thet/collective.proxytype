"""Module where all interfaces, events and exceptions live."""

from collective.proxytype import _
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IBrowserLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IProxyType(Interface):
    """Marker interface for Proxy types.
    """


class IProxySchema(Interface):
    """Schema interface for the Proxy type and portlet.
    """

    remote_url = schema.TextLine(
        title=_(
            "label_remote_url",
            default=u"Remote URL"
        ),
        description=_(
            "help_remote_url",
            default="URL of the remote content which should be displayed here."
        ),
        required=True,
    )

    url_replacement_map = schema.Text(
        title=_(
            "label_url_replacement_map",
            default=u"URL replacement map"
        ),
        description=_(
            "help_url_replacement_map",
            default=u"""
List of URLs parts which occur in the content and has to replaced with replacement URLs in JSON format like this:
{"content_url": CONTENT_URL, "replacement_url": REPLACEMENT_URL}.
Matches are done from the beginning of strings.
You might want to make your url replacement map independend from different virtual hosting URLs. Use the variable $PORTAL_URL for "content_url" value to substitute with the portal's url.
""",  # noqa
        ),
        required=False,
    )

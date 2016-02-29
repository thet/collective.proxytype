# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from collective.proxytype import _
from plone.dexterity.interfaces import IDexterityContainer
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IBrowserLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IProxyType(IDexterityContainer):
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

# -*- coding: utf-8 -*-
from .interfaces import IProxy
from .interfaces import IProxySchema
from plone.dexterity.content import Item
from zope.interface import implementer
from plone.supermodel import model


class IProxyContentSchema(model.Schema, IProxySchema):
    """Proxy content schema
    """


@implementer(IProxy)
class ProxyType(Item):
    """Proxy type
    """

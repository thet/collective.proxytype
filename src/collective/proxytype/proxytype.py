# -*- coding: utf-8 -*-
from .interfaces import IProxySchema
from .interfaces import IProxyType
from plone.dexterity.content import Container
from zope.interface import implementer
from plone.supermodel import model


class IProxyTypeSchema(model.Schema, IProxySchema):
    """Proxy content schema
    """


@implementer(IProxyType)
class ProxyType(Container):
    """Proxy type
    """

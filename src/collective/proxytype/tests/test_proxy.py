# -*- coding: utf-8 -*-
from plone.app.testing import TEST_USER_ID
from zope.component import queryUtility
from zope.component import createObject
from plone.app.testing import setRoles
from plone.dexterity.interfaces import IDexterityFTI
from plone import api

from collective.proxytype.testing import COLLECTIVE_PROXYTYPE_INTEGRATION_TESTING  # noqa
from collective.proxytype.interfaces import IProxyType

import unittest2 as unittest


class ProxyIntegrationTest(unittest.TestCase):

    layer = COLLECTIVE_PROXYTYPE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='Proxy')
        schema = fti.lookupSchema()
        self.assertEqual(IProxyType, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='Proxy')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='Proxy')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(IProxyType.providedBy(obj))

    def test_adding(self):
        self.portal.invokeFactory('Proxy', 'Proxy')
        self.assertTrue(
            IProxyType.providedBy(self.portal['Proxy'])
        )

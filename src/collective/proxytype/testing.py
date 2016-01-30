# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.proxytype


class BrowserLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=collective.proxytype)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.proxytype:default')


COLLECTIVE_PROXYTYPE_FIXTURE = BrowserLayer()


COLLECTIVE_PROXYTYPE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_PROXYTYPE_FIXTURE,),
    name='BrowserLayer:IntegrationTesting'
)


COLLECTIVE_PROXYTYPE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_PROXYTYPE_FIXTURE,),
    name='BrowserLayer:FunctionalTesting'
)


COLLECTIVE_PROXYTYPE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_PROXYTYPE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='BrowserLayer:AcceptanceTesting'
)

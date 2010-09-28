from Products.CMFCore.utils import getToolByName

from plone.app.upgrade.utils import loadMigrationProfile
from plone.app.upgrade.tests.base import MigrationTest

from Products.ResourceRegistries.config import JSTOOLNAME

class TestMigrations_v4_1alpha1(MigrationTest):

    profile = 'profile-plone.app.upgrade.v41:4.0.x-4.1a1'

    def testProfile(self):
        # This tests the whole upgrade profile can be loaded
        loadMigrationProfile(self.portal, self.profile)
        self.failUnless(True)

    def afterSetUp(self):
        self.tool = getToolByName(self.portal, JSTOOLNAME)

    def testDefaultJSIsInstalled(self):
        installedScriptIds = self.tool.getResourceIds()
        self.failUnless('search.js' in installedScriptIds)


def test_suite():
    from unittest import defaultTestLoader
    return defaultTestLoader.loadTestsFromName(__name__)
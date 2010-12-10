from Products.CMFCore.utils import getToolByName

from plone.app.upgrade.utils import loadMigrationProfile
from plone.app.upgrade.tests.base import MigrationTest

from Products.ResourceRegistries.config import JSTOOLNAME


class TestMigrations_v4_1alpha1(MigrationTest):

    profile = 'profile-plone.app.upgrade.v41:4.0.x-4.1a1'

    def afterSetUp(self):
        self.jstool = getToolByName(self.portal, JSTOOLNAME)

    def testProfile(self):
        # This tests the whole upgrade profile can be loaded
        loadMigrationProfile(self.portal, self.profile)
        self.failUnless(True)

    def testInstallNewDependencies(self):
        # test for running the plone.app.search profile by checking for the js
        # file it installs (the profile is marked as noninstallable, so we
        # can't ask the quick installer)
        installedScriptIds = self.jstool.getResourceIds()
        expected = [
            # js resource that is part of plone.app.search
            '++resource++search.js']
        for e in expected:
            self.failUnless(e in installedScriptIds, e)


def test_suite():
    from unittest import defaultTestLoader
    return defaultTestLoader.loadTestsFromName(__name__)

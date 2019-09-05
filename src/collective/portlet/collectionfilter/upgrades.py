from collective.collectionfilter.portlets.collectionfilter import ICollectionFilterPortlet  # noqa
from plone.portlets.interfaces import ILocalPortletAssignable
from plone.portlets.interfaces import IPortletAssignmentMapping
from plone.portlets.interfaces import IPortletManager
from Products.CMFCore.utils import getToolByName
from Products.GenericSetup.interfaces import ISetupTool
from zope.component import getMultiAdapter
from zope.component import getUtilitiesFor
from zope.component.hooks import getSite

import logging

_marker = []

logger = logging.getLogger(__file__)


def loadMigrationProfile(context, profile, steps=_marker):
    if not ISetupTool.providedBy(context):
        context = getToolByName(context, 'portal_setup')
    if steps is _marker:
        context.runAllImportStepsFromProfile(profile, purge_old=False)
    else:
        for step in steps:
            context.runImportStepFromProfile(profile,
                                             step,
                                             run_dependencies=False,
                                             purge_old=False)


def reapply_profile(context):
    loadMigrationProfile(
        context,
        'profile-collective.portlet.collectionfilter:default',
    )

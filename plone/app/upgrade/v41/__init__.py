from plone.app.upgrade.utils import loadMigrationProfile

def to41alpha1(context): 
    """4.0 -> 4.1a1
    """    
    loadMigrationProfile(context, 'profile-plone.app.upgrade.v41:to41alpha1')
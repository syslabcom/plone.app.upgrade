from plone.app.upgrade.utils import loadMigrationProfile

def four0_four1_a1(context): 
    """4.0.x -> 4.1a1
    """    
    loadMigrationProfile(context, 'profile-plone.app.upgrade.v41:4.0.x-4.1a1')
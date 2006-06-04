#########################################################################
# Copyright (c) 2003, 2004, 2005 Alberto Berti, Gregoire Weber. 
# All Rights Reserved.
# 
# This file is part of CMFEditions.
# 
# CMFEditions is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# CMFEditions is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with CMFEditions; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
#########################################################################
"""CMFEditions Globals

$Id: __init__.py,v 1.17 2005/02/07 22:09:08 gregweb Exp $
"""
__version__ = "$Revision: 1.17 $"

import sys
from Globals import package_home

import patches

from Products.CMFCore import utils, CMFCorePermissions, DirectoryView
from Products.CMFCore.DirectoryView import registerFileExtension, registerDirectory

from Products.CMFEditions import UniqueIdHandlerTool
from Products.CMFEditions import ModifierRegistryTool
from Products.CMFEditions import ArchivistTool
from Products.CMFEditions import ZVCStorageTool
from Products.CMFEditions import CopyModifyMergeRepositoryTool
from Products.CMFEditions import ReferenceFactoriesTool
from Products.CMFEditions import KeepLastNVersionsTool

from Products.CMFEditions import StandardModifiers

PACKAGE_HOME = package_home(globals())

tools = (
    UniqueIdHandlerTool.UniqueIdHandlerTool,
    ModifierRegistryTool.ModifierRegistryTool,
    ArchivistTool.ArchivistTool,
    ZVCStorageTool.ZVCStorageTool,
    CopyModifyMergeRepositoryTool.CopyModifyMergeRepositoryTool,
    ReferenceFactoriesTool.ReferenceFactoriesTool,
    KeepLastNVersionsTool.KeepLastNVersionsTool,
    )

bases = tools

z_bases = utils.initializeBasesPhase1(bases, sys.modules[ __name__ ])

# This is used by a script (external method) that can be run
# to set up CMFEditions in an existing CMF Site instance.
product_globals = globals()

DirectoryView.registerDirectory('skins', product_globals)
DirectoryView.registerDirectory('skins/CMFEditions', product_globals)

def initialize(context):
    utils.initializeBasesPhase2(z_bases, context)

    # BBB: may be cleaned up when dropping CMF 1.4.x/Plone 2.0.x support
    try:
        utils.ToolInit(meta_type='CMF Editions Tool', tools=tools,
                       icon='tool.gif').initialize(context)
    except TypeError:
        # CMF 1.4.x/Plone 2.0.x
        utils.ToolInit(meta_type='CMF Editions Tool', tools=tools,
                       product_name='CMFEditions', icon='tool.gif',
                       ).initialize(context)
        
    # initialize standard modifiers to make them addable through the ZMI
    StandardModifiers.initialize(context)
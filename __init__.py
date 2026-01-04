# ***** BEGIN GPL LICENSE BLOCK *****
#
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ***** END GPL LICENCE BLOCK *****

bl_info = {
    "name": "Better FBX Importer & Exporter",
    "author": "mesh online",
    "version": (4, 5, 3),
    "blender": (2, 80, 0),
    "location": "File > Import-Export",
    "description": "Import and export FBX files with native FBX SDK",
    "warning": "",
    "wiki_url": "http://www.mesh-online.net/fbx.html",
    "category": "Import-Export",
}

import sys
import bpy

# --- COMPATIBILITY FIX FOR BLENDER 5.0 ---
# The other files in this add-on try to import 'bpy_types', which doesn't exist.
# This code creates a fake 'bpy_types' that points to the correct 'bpy.types'.
if "bpy_types" not in sys.modules:
    sys.modules["bpy_types"] = bpy.types
# -----------------------------------------

if "bpy" in locals():
    import importlib
    if "importer" in locals():
        importlib.reload(importer)
    if "exporter" in locals():
        importlib.reload(exporter)


def register():
    from .exporter import register_exporter
    register_exporter()
    from .importer import register_importer
    register_importer()


def unregister():
    from .exporter import unregister_exporter
    unregister_exporter()
    from .importer import unregister_importer
    unregister_importer()
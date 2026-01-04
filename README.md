### Blender 5.0 Compatibility Fix

This version fixes a critical issue in Blender 5.0 where the addon failed to enable with the error:

`No module named 'bpy_types'`

The issue was caused by API changes in Blender 5.0, where internal module access and addon execution flow were updated. The addon code has been modified to remove or replace deprecated `bpy_types` references, ensuring compatibility with Blender 5.0's new extension and addon system.

Tested and confirmed working in Blender 5.0.

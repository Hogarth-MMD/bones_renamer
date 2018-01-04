import bpy
from . import boneMaps_renamer
from .boneMaps_renamer import *

import imp
imp.reload(boneMaps_renamer)

bl_info = {
	"name": "Bones Renamer",
	"author": "",
	"version": (1, 0),
	"blender": (2, 79, 0),
	"location": "View3D > Tool Shelf > Bones Renamer",
	"description": "bones renamer for armature conversion",
	"warning": "",
	"wiki_url": "",
	"category": "Object",
	}

class BonesRenamerPanel(bpy.types.Panel):
	"""Creates the Bones Renamer Panel in a VIEW_3D TOOLS tab"""
	bl_label = "Bones Renamer Panel"
	bl_idname = "OBJECT_PT_bones_renamer"
	bl_space_type = "VIEW_3D"
	bl_region_type = "TOOLS"
	bl_category = "bones_renamer"


	def draw(self, context):
		layout = self.layout
		row = layout.row()
		row.label(text="Mass Rename Bones", icon="ARMATURE_DATA")
		row = layout.row()
		row = layout.row()
		layout.prop(context.scene, "Origin_Armature_Type")
		row = layout.row()
		layout.prop(context.scene, "Destination_Armature_Type")
		row = layout.row()
		row.operator("object.bones_renamer", text = "Mass Rename Bones")
		row = layout.row()

def main(context):
	use_international_fonts_display_names_bones()
	unhide_all_armatures()
	rename_bones(bpy.context.scene.Origin_Armature_Type, bpy.context.scene.Destination_Armature_Type)
	rename_finger_bones(bpy.context.scene.Origin_Armature_Type, bpy.context.scene.Destination_Armature_Type)
	bpy.ops.object.mode_set(mode='POSE')
	bpy.ops.pose.select_all(action='SELECT')


class BonesRenamer(bpy.types.Operator):
	"""Mass bones renamer for armature conversion"""
	bl_idname = "object.bones_renamer"
	bl_label = "Bones Renamer"

	bpy.types.Scene.Origin_Armature_Type = bpy.props.EnumProperty(items = [('mmd_english', 'MMD English bone names', 'MikuMikuDance English bone names'), ('xna_lara', 'XNALara bone names', 'XNALara bone names'), ('daz_poser', 'DAZ/Poser bone names', 'DAZ/Poser bone names'), ('blender_rigify', 'Blender rigify bone names', 'Blender rigify bone names before generating the complete rig'), ('sims_2', 'Sims 2 bone names', 'Sims 2 bone names'), ('motion_builder', 'Motion Builder bone names', 'Motion Builder bone names'), ('3ds_max', '3ds Max bone names', '3ds Max bone names'),  ('bepu', 'Bepu full body IK bone names', 'Bepu full body IK bone names'), ('mmd_japanese', 'MMD Japanese bone names', 'MikuMikuDamce Japanese bone names'), ('mmd_japaneseLR', 'MMD Japanese bones names .L.R suffixes', 'MikuMikuDamce Japanese bones names with .L.R suffixes')], name = "Rename  bones  from :", default = 'mmd_japanese')

	#('unknown', 'unknown_armature_type bone names', 'unknown_armature_type bone names')

	bpy.types.Scene.Destination_Armature_Type = bpy.props.EnumProperty(items = [('mmd_english', 'MMD English bone names', 'MikuMikuDance English bone names'), ('xna_lara', 'XNALara bone names', 'XNALara bone names'), ('daz_poser', 'DAZ/Poser bone names', 'DAZ/Poser bone names'), ('blender_rigify', 'Blender rigify bone names', 'Blender rigify bone names before generating the complete rig'), ('sims_2', 'Sims 2 bone names', 'Sims 2 bone names'), ('motion_builder', 'Motion Builder bone names', 'Motion Builder bone names'), ('3ds_max', '3ds Max bone names', '3ds Max bone names'), ('bepu', 'Bepu full body IK bone names', 'Bepu full body IK bone names'), ('mmd_japanese', 'MMD Japanese bone names', 'MikuMikuDamce Japanese bone names'), ('mmd_japaneseLR', 'MMD Japanese bones names .L.R suffixes', 'MikuMikuDamce Japanese bones names with .L.R suffixes')], name = "Rename  bones  to :", default = 'mmd_english')




	#@classmethod
	#def poll(cls, context):
		#return context.active_object.type == 'ARMATIRE'
		#return context.active_object is not None

	def execute(self, context):
		main(context)
		return {'FINISHED'}


def register():
	bpy.utils.register_module(__name__)


def unregister():
	bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
	register()

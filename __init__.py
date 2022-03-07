bl_info = {
	"name": "Bones Renamer",
	"author": "Hogarth-MMD,空想幻灵",
	"version": (1, 1),
	"blender": (2, 83, 0),
	"location": "View3D > Tool Shelf > Bones Renamer",
	"description": "bones renamer for armature conversion",
	"warning": "",
	"wiki_url": "https://github.com/uitcis/bones_renamer",
	"category": "Object",
	}
import bpy
from bpy.types import Operator, Panel, PropertyGroup

from . import boneMaps_renamer
from .boneMaps_renamer import *
from . import import_csv
#import imp
#imp.reload(boneMaps_renamer)

# Panel

class Bones_PT_Renamer(Panel):
	"""Creates the Bones Renamer Panel in a VIEW_3D TOOLS tab"""
	bl_space_type = "VIEW_3D"
	bl_region_type = "TOOLS"
	bl_label = "Bones Renamer Panel"
	#bl_category = "Bones Renamer"
	bl_idname = "OBJECT_PT_bones_renamer"

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

'''def main(context):
	#use_international_fonts_display_names_bones()
	#unhide_all_armatures()
'''
#define
def main(context):

	BONE_NAMES_DICTIONARY = import_csv.use_csv_bones_dictionary()
	FINGER_BONE_NAMES_DICTIONARY = import_csv.use_csv_bones_fingers_dictionary()
	rename_bones(bpy.context.scene.Origin_Armature_Type, bpy.context.scene.Destination_Armature_Type, BONE_NAMES_DICTIONARY)
	rename_finger_bones(bpy.context.scene.Origin_Armature_Type, bpy.context.scene.Destination_Armature_Type, FINGER_BONE_NAMES_DICTIONARY)
	bpy.ops.object.mode_set(mode='POSE')
	bpy.ops.pose.select_all(action='SELECT')

	
#done
class BonesRenamer(bpy.types.Operator):
	"""Mass bones renamer for armature conversion"""
	bl_idname = "object.bones_renamer"
	bl_label = "Bones Renamer"

	bpy.types.Scene.Origin_Armature_Type = bpy.props.EnumProperty(items = [('mmd_english', 'MMD English bone names', 'MikuMikuDance English bone names'), ('mmd_japanese', 'MMD Japanese bone names', 'MikuMikuDamce Japanese bone names'), ('mmd_japaneseLR', 'MMD Japanese bones names .L.R suffixes', 'MikuMikuDamce Japanese bones names with .L.R suffixes'), ('xna_lara', 'XNALara bone names', 'XNALara bone names'), ('daz_poser', 'DAZ/Poser bone names', 'DAZ/Poser/Second Life bone names'), ('blender_rigify', 'Blender rigify bone names', 'Blender rigify bone names before generating the complete rig'), ('sims_2', 'Sims 2 bone names', 'Sims 2 bone names'), ('motion_builder', 'Motion Builder bone names', 'Motion Builder bone names'), ('3ds_max', '3ds Max bone names', '3ds Max bone names'), ('bepu', 'Bepu full body IK bone names', 'Bepu full body IK bone names'), ('project_mirai', 'Project Mirai bone names', 'Project Mirai bone names'), ('manuel_bastioni_lab', 'Manuel Bastioni Lab bone names', 'Manuel Bastioni Lab bone names'), ('makehuman_mhx', 'Makehuman MHX bone names', 'Makehuman MHX bone names'), ('sims_3', 'Sims 3 bone names', 'Sims 3 bone names'), ('doa5lr', 'DOA5LR bone names', 'Dead on Arrival 5 Last Round bone names'), ('Bip_001', 'Bip001 bone names', 'Bip001 bone names'), ('biped_3ds_max', 'Biped 3DS Max bone names', 'Biped 3DS Max bone names'), ('biped_sfm', 'Biped Source Film Maker bone names', 'Biped Source Film Maker bone names'), ('valvebiped', 'ValveBiped bone names', 'ValveBiped bone names'), ('iClone7', 'iClone7 bone names', 'iClone7 bone names')], name = "Rename  bones  from :", default = 'mmd_japanese')


	bpy.types.Scene.Destination_Armature_Type = bpy.props.EnumProperty(items = [('mmd_english', 'MMD English bone names', 'MikuMikuDance English bone names'), ('mmd_japanese', 'MMD Japanese bone names', 'MikuMikuDamce Japanese bone names'), ('mmd_japaneseLR', 'MMD Japanese bones names .L.R suffixes', 'MikuMikuDamce Japanese bones names with .L.R suffixes'), ('xna_lara', 'XNALara bone names', 'XNALara bone names'), ('daz_poser', 'DAZ/Poser bone names', 'DAZ/Poser/Second Life bone names'), ('blender_rigify', 'Blender rigify bone names', 'Blender rigify bone names before generating the complete rig'), ('sims_2', 'Sims 2 bone names', 'Sims 2 bone names'), ('motion_builder', 'Motion Builder bone names', 'Motion Builder bone names'), ('3ds_max', '3ds Max bone names', '3ds Max bone names'), ('bepu', 'Bepu full body IK bone names', 'Bepu full body IK bone names'), ('project_mirai', 'Project Mirai bone names', 'Project Mirai bone names'), ('manuel_bastioni_lab', 'Manuel Bastioni Lab bone names', 'Manuel Bastioni Lab bone names'), ('makehuman_mhx', 'Makehuman MHX bone names', 'Makehuman MHX bone names'), ('sims_3', 'Sims 3 bone names', 'Sims 3 bone names'), ('doa5lr', 'DOA5LR bone names', 'Dead on Arrival 5 Last Round bone names'), ('Bip_001', "Bip001 bone names", 'Bip001 bone names'), ('biped_3ds_max', 'Biped 3DS Max bone names', 'Biped 3DS Max bone names'), ('biped_sfm', 'Biped Source Film Maker bone names', 'Biped Source Film Maker bone names'), ('valvebiped', 'ValveBiped bone names', 'ValveBiped bone names'), ('iClone7', 'iClone7 bone names', 'iClone7 bone names')], name = "Rename  bones  to :", default = 'mmd_english')

	#@classmethod
	#def poll(cls, context):
		#return context.active_object.type == 'ARMATURE'
		#return context.active_object is not None

	def execute(self, context):
		main(context)
		return {'FINISHED'}


#####################

    
classes = (
   Bones_PT_Renamer,
   BonesRenamer,
)

register, unregister = bpy.utils.register_classes_factory(classes)

# Register
def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    


# Unregister
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
   


if __name__ == "__main__":
	register()

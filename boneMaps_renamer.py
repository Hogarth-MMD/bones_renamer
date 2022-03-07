#From left to right:
#MMD standard English bone names[0], XNALara bone names[1], DAZ/Poser bone names[2], Blender rigify bone names before generate[3], Sims 2 bone names[4],
# Motion Builder[5], 3ds Max[6], unknown[7]
# MMD standard Japanese bone names
# Motion Builder[5] Arm,ForeArm, not UpArm, LowArm Leg, not LowLeg

# conflict "LeftShoulder", "RightShoulder", Motion Builder[5], 3ds Max[6]



import bpy

def rename_bones(boneMap1, boneMap2, BONE_NAMES_DICTIONARY):
	boneMaps = BONE_NAMES_DICTIONARY[0]
	boneMap1_index = boneMaps.index(boneMap1)
	boneMap2_index = boneMaps.index(boneMap2)
	bpy.ops.object.mode_set(mode='OBJECT')

	for k in BONE_NAMES_DICTIONARY:
		if k[boneMap1_index] in bpy.context.active_object.data.bones.keys():
			if k[boneMap2_index] != '':
				bpy.context.active_object.data.bones[k[boneMap1_index]].name = k[boneMap2_index]

def rename_finger_bones(boneMap1, boneMap2, FINGER_BONE_NAMES_DICTIONARY):
	boneMaps = FINGER_BONE_NAMES_DICTIONARY[0]
	boneMap1_index = boneMaps.index(boneMap1)
	boneMap2_index = boneMaps.index(boneMap2)
	bpy.ops.object.mode_set(mode='OBJECT')
	for k in FINGER_BONE_NAMES_DICTIONARY:
		if k[boneMap1_index] in bpy.context.active_object.data.bones.keys():
			if k[boneMap2_index] != '':
				bpy.context.active_object.data.bones[k[boneMap1_index]].name = k[boneMap2_index]

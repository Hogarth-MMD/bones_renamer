#From left to right:
#MMD standard English bone names[0], XNALara bone names[1], DAZ/Poser bone names[2], Blender rigify bone names before generate[3], Sims 2 bone names[4],
# Motion Builder[5], 3ds Max[6], unknown[7]
# MMD standard Japanese bone names
# Motion Builder[5] Arm,ForeArm, not UpArm, LowArm Leg, not LowLeg

# conflict "LeftShoulder", "RightShoulder", Motion Builder[5], 3ds Max[6]

BONE_NAMES_DICTIONARY = [
("root", "root ground", "", "root", "auskel", "", "", "", "", "全ての親", "全ての親"), 
  
("neck", "head neck lower",  "neck", "neck", "neck", "Neck", "Neck", "Neck", "neck", "首", "首"), #9
("head", "head neck upper", "head", "head", "head", "Head", "Head", "Head", "head", "頭", "頭"), #9

("center", "root hips", "hip", 'hips', "root_rot", "Hips", "Hips", "Hip", "", "センター", "センター"), #9 
("upper body 2", "spine upper", "chest", "chest", "spine2", "Spine2", "Chest3", "", 'chest', "上半身2", "上半身2"), #9
("upper body", "spine lower", "abdomen", "spine", "spine0", "chest", "Chest", "Chest1", 'spine', "上半身", "上半身"), #9
("lower body", "pelvis", "", "", "", "", "", "", 'hips', "下半身", "下半身"), 

("shoulder_L", "arm left shoulder 1", "lCollar", "shoulder.L", "l_clavicle", "LeftShoulder", "LeftCollar", "Left Collar", 'shoulder.L', "左肩", "肩.L"), #9
("arm_L", "arm left shoulder 2", "lShldr", "upper_arm.L", "l_upperarm",  "LeftUpArm", "LeftShoulder", "Left Shoulder", 'uparm.L', "左腕", "腕.L"), #9
("elbow_L", "arm left elbow", "lForeArm", "forearm.L", "l_forearm", "LeftLowArm", "LeftElbow", "Left Forearm", 'loarm.L', "左ひじ", "ひじ.L"), #9
("wrist_L", "arm left wrist", "lHand", "hand.L", "l_hand", "LeftHand", "LeftWrist", "Left Hand", 'finger3-1.L',"左手首", "手首.L"),  #9
("shoulder_R", "arm right shoulder 1", "rCollar", "shoulder.R", "r_clavicle", "RightShoulder", "RightCollar", "Right Collar", 'shoulder.R', "右肩", "肩.R"),  #9
("arm_R", "arm right shoulder 2", "rShldr", "upper_arm.R", "r_upperarm", "RightUpArm", "RightShoulder", "Right Shoulder", 'uparm.R', "右腕", "腕.R"), #9 
("elbow_R", "arm right elbow", "rForeArm", "forearm.R", "r_forearm", "RightLowArm", "RightElbow", "Right Forearm", 'loarm.R', "右ひじ", "ひじ.R"), #9 
("wrist_R", "arm right wrist", "rHand", "hand.R", "r_hand", "RightHand", "RightWrist", "Right Hand", 'finger3-1.R',"右手首", "手首.R"), #9
("leg_L", "leg left thigh", "lThigh", "thigh.L", "l_thigh", "LeftUpLeg", "LeftHip", "Left Thigh", 'upleg.L', "左足", "足.L"),  #9
("knee_L", "leg left knee", "lShin", "shin.L", "l_calf", "LeftLowLeg", "LeftKnee", "Left Shin", 'loleg.L', "左ひざ", "ひざ.L"), #9
("ankle_L", "leg left ankle", "lFoot", "foot.L", "l_foot", "LeftFoot", "LeftAnkle", "Left Foot", 'foot.L', "左足首", "足首.L"), #9 
("leg_R", "leg right thigh", "rThigh", "thigh.R", "r_thigh", "RightUpLeg", "RightHip", "Right Thigh", 'upleg.R', "右足", "足.R"),  #9
("knee_R", "leg right knee", "rShin", "shin.R", "r_calf", "RightLowLeg", "RightKnee", "Right Shin", 'loleg.R', "右ひざ", "ひざ.R"),  #9
("ankle_R", "leg right ankle", "rFoot", "foot.R", "r_foot", "RightFoot", "RightAnkle", "Right Foot", 'foot.R', "右足首", "足首.R"), #9

("toe_L", "leg left toes", "lToe", "toe.L", "l_toe", 'LeftToeBase', "LeftToe", "Left Toe", 'toe1-1.L', "左つま先", "つま先.L"), #9
("toe_R", "leg right toes", "rToe", "toe.R", "r_toe", 'RightToeBase', "RightToe", 'toe1-1.R',"Right Toe", "右つま先", "つま先.R"), #9
("eye_L", "head eyeball left", "leftEye", "eye.L", "l_eye", "LeftEye", "LeftEye", "Left Eye", 'eye.L', "左目", "目.L"), #9
("eye_R", "head eyeball right", "rightEye", "eye.R", "r_eye", "RightEye", "RightEye", "Right Eye", 'eye.R', "右目", "目.R"), #9
]



FINGER_BONE_NAMES_DICTIONARY = [
("thumb1_L", "arm left finger 1b", "lThumb2", "thumb.02.L", "l_thumb1", 'LeftHandThumb2', 'LeftFinger01', 'finger1-3.L', "左親指１", "親指１.L"),
("thumb2_L", "arm left finger 1c", "lThumb3", "thumb.03.L", "l_thumb2", 'LeftHandThumb3', 'LeftFinger02', 'finger1-4.L', "左親指２", "親指２.L"),
("fore1_L", "arm left finger 2a", "lIndex1", "f_index.01.L", "l_index0", 'LeftHandIndex1', 'LeftFinger1', 'finger2-2.L', "左人指１", "人指１.L"),
("fore2_L", "arm left finger 2b", "lIndex2", "f_index.02.L", "l_index1", 'LeftHandIndex2', 'LeftFinger11', 'finger2-3.L', "左人指２", "人指２.L"),
("fore3_L", "arm left finger 2c", "lIndex3", "f_index.03.L", "l_index2", 'LeftHandIndex3', 'LeftFinger12', 'finger2-4.L', "左人指３", "人指３.L"),
("middle1_L", "arm left finger 3a", "lMid1", "f_middle.01.L", "l_mid0", 'LeftHandMiddle1', 'LeftFinger2', 'finger3-2.L', "左中指１", "中指１.L"),
("middle2_L", "arm left finger 3b", "lMid2", "f_middle.02.L", "l_mid1", 'LeftHandMiddle2', 'LeftFinger21', 'finger3-3.L', "左中指２", "中指２.L"),
("middle3_L", "arm left finger 3c", "lMid3", "f_middle.03.L", "l_mid2", 'LeftHandMiddle3', 'LeftFinger22', 'finger3-4.L', "左中指３", "中指３.L"),
("third1_L", "arm left finger 4a", "lRing1", "f_ring.01.L", "l_ring0", 'LeftHandRing1', 'LeftFinger3', 'finger4-2.L', "左薬指１", "薬指１.L"),
("third2_L", "arm left finger 4b", "lRing2", "f_ring.02.L", "l_ring1", 'LeftHandRing2', 'LeftFinger31', 'finger4-3.L', "左薬指２", "薬指２.L"),
("third3_L", "arm left finger 4c", "lRing3", "f_ring.03.L", "l_ring2", 'LeftHandRing3', 'LeftFinger32', 'finger4-4.L', "左薬指３", "薬指３.L"),
("little1_L", "arm left finger 5a", "lPinky1", "f_pinky.01.L", "l_pinky0", 'LeftHandPinky1', 'LeftFinger4', 'finger5-2.L', "左小指１", "小指１.L"),
("little2_L", "arm left finger 5b", "lPinky2", "f_pinky.02.L", "l_pinky1", 'LeftHandPinky2', 'LeftFinger41', 'finger5-3.L', "左小指２", "小指２.L"),
("little3_L", "arm left finger 5c", "lPinky3", "f_pinky.03.L", "l_pinky2", 'LeftHandPinky3', 'LeftFinger42', 'finger5-4.L', "左小指３", "小指３.L"),
("thumb1_R", "arm right finger 1b", "rThumb2", "thumb.02.R", "r_thumb1", 'RightHandThumb2', 'RightFinger01', 'finger1-3.R', "右親指１", "親指１.R"),
("thumb2_R", "arm right finger 1c", "rThumb3", "thumb.03.R", "r_thumb2", 'RightHandThumb3', 'RightFinger02', 'finger1-4.R', "右親指２", "親指２.R"),
("fore1_R", "arm right finger 2a", "rIndex1", "f_index.01.R", "r_index0", 'RightHandIndex1', 'RightFinger1', 'finger2-2.R', "右人指１", "人指１.R"),
("fore2_R", "arm right finger 2b", "rIndex2", "f_index.02.R", "r_index1", 'RightHandIndex2', 'RightFinger11', 'finger2-3.R', "右人指２", "人指２.R"),
("fore3_R", "arm right finger 2c", "rIndex3", "f_index.03.R", "r_index2", 'RightHandIndex3', 'RightFinger12', 'finger2-4.R', "右人指３", "人指３.R"),
("middle1_R", "arm right finger 3a", "rMid1", "f_middle.01.R", "r_mid0", 'RightHandMiddle1', 'RightFinger2', 'finger3-2.R', "右中指１", "中指１.R"),
("middle2_R", "arm right finger 3b", "rMid2", "f_middle.02.R", "r_mid1", 'RightHandMiddle2', 'RightFinger21', 'finger3-3.R', "右中指２", "中指２.R"),
("middle3_R", "arm right finger 3c", "rMid3", "f_middle.03.R", "r_mid2", 'RightHandMiddle3', 'RightFinger22', 'finger3-4.R', "右中指３", "中指３.R"),
("third1_R", "arm right finger 4a", "rRing1", "f_ring.01.R", "r_ring0", 'RightHandRing1', 'RightFinger3', 'finger4-2.R', "右薬指１", "薬指１.R"),
("third2_R", "arm right finger 4b", "rRing2", "f_ring.02.R", "r_ring1", 'RightHandRing2', 'RightFinger31', 'finger4-3.R', "右薬指２", "薬指２.R"),
("third3_R", "arm right finger 4c", "rRing3", "f_ring.03.R", "r_ring2", 'RightHandRing3', 'RightFinger32', 'finger4-4.R', "右薬指３", "薬指３.R"),
("little1_R", "arm right finger 5a", "rPinky1", "f_pinky.01.R", "r_pinky0", 'RightHandPinky1', 'RightFinger4', 'finger5-2.R', "右小指１", "小指１.R"),
("little2_R", "arm right finger 5b", "rPinky2", "f_pinky.02.R", "r_pinky1", 'RightHandPinky2', 'RightFinger41', 'finger5-3.R', "右小指２", "小指２.R"),
("little3_R", "arm right finger 5c", "rPinky3", "f_pinky.03.R", "r_pinky2", 'RightHandPinky3', 'RightFinger42', 'finger5-4.R', "右小指３", "小指３.R"),
("thumb0_L", "arm left finger 1a", "lThumb1", "thumb.01.L", "l_thumb0", 'LeftHandThumb1', 'LeftFinger0', 'finger1-2.L', "左親指0", "親指0.L"),
("thumb0_R", "arm right finger 1a", "rThumb1", "thumb.01.R", "r_thumb0", 'RightHandThumb1', 'RightFinger0', 'finger1-2.R', "右親指0", "親指0.R"),
]



import bpy

#use international fonts and display the names of the bones
def use_international_fonts_display_names_bones():
	bpy.context.user_preferences.system.use_international_fonts = True
	bpy.context.object.data.show_names = True


def unhide_all_armatures():
	for o in bpy.context.scene.objects:
		if o.type == 'ARMATURE':
			o.hide = False



def rename_bones(boneMap1, boneMap2): 
	boneMaps = ('mmd_english', 'xna_lara', 'daz_poser', 'blender_rigify', 'sims_2', 'motion_builder', '3ds_max', 'type_x', 'bepu', 'mmd_japanese', 'mmd_japaneseLR', 'unknown')
	boneMap1_index = boneMaps.index(boneMap1)
	boneMap2_index = boneMaps.index(boneMap2)
	bpy.ops.object.mode_set(mode='OBJECT')

	for k in BONE_NAMES_DICTIONARY:
		if k[boneMap1_index] in bpy.context.active_object.data.bones.keys():
			if k[boneMap2_index] != '':
				bpy.context.active_object.data.bones[k[boneMap1_index]].name = k[boneMap2_index]

def rename_finger_bones(boneMap1, boneMap2):
	boneMaps = ('mmd_english', 'xna_lara', 'daz_poser', 'blender_rigify', 'sims_2', 'motion_builder', '3ds_max', 'bepu', 'mmd_japanese', 'mmd_japaneseLR', 'unknown')
	boneMap1_index = boneMaps.index(boneMap1)
	boneMap2_index = boneMaps.index(boneMap2)
	bpy.ops.object.mode_set(mode='OBJECT')

	for k in FINGER_BONE_NAMES_DICTIONARY:
		if k[boneMap1_index] in bpy.context.active_object.data.bones.keys():
			if k[boneMap2_index] != '':
				bpy.context.active_object.data.bones[k[boneMap1_index]].name = k[boneMap2_index]

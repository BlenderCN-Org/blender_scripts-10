# # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Blender python script for rendering x3d scenes
# Arpit Agarwal
# agarwal32@wisc.edu
# March 2018
# # # # # # # # # # # # # # # # # # # # # # # # # # # #

import bpy

# Loop through all x3d files
for num in range(1):
    # Delete everything 
    bpy.ops.object.select_all(action='TOGGLE') 
    bpy.ops.object.select_all(action='TOGGLE') 
    bpy.ops.object.delete() 
    bpy.ops.object.select_all(action='SELECT') 
    bpy.ops.object.delete() 
    # load new scene
    file = 'Users/cueball/Box Sync/blender_v7/v7_visualization.x3d'
    bpy.ops.import_scene.x3d(filepath = file)
    # Deselect everything
    bpy.ops.object.select_all(action='TOGGLE')
    # Delete not necessary stuff
    for item in bpy.data.objects:
        if item.type != "MESH":
            bpy.data.objects[item.name].select = True
            bpy.ops.object.delete()
    # Rename the left data
    bpy.data.objects["Shape_IndexedFaceSet"].data.name = 'LiqSurfaceMesh'
    bpy.data.objects["Shape_IndexedFaceSet.001"].data.name = 'NozzleSurfaceMesh'
    for obj in bpy.context.scene.objects:
        if obj.name == 'Shape_IndexedFaceSet':
            obj.name = 'LiqSurface'
        if obj.name == 'Shape_IndexedFaceSet.001':
            obj.name = 'NozzleSurface'
    # Scale Relevant Data
    bpy.data.objects['LiqSurface'].scale    = (1000, 1000, 1000)
    bpy.data.objects['NozzleSurface'].scale = (1000, 1000, 1000)
    # liquid material
    bpy.data.objects['LiqSurface'].select   = True
    bpy.ops.object.shade_smooth()
    bpy.context.scene.objects.active        = None
    bpy.context.scene.objects.active        = bpy.data.objects["LiqSurface"]
    ob = bpy.context.active_object
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.vertices_smooth(repeat=5)
    bpy.ops.object.editmode_toggle()
    bpy.context.object.active_material.use_transparency                 = True
    bpy.context.object.active_material.transparency_method              = 'RAYTRACE'
    bpy.context.object.active_material.raytrace_transparency.ior        = 1.37
    bpy.context.object.active_material.alpha                            = 0.1
    bpy.context.object.active_material.specular_intensity               = 1
    bpy.context.object.active_material.specular_hardness                = 511
    bpy.context.object.active_material.specular_color                   = (1, 1, 1)
    bpy.context.object.active_material.ambient                          = 0.5 
    bpy.context.object.active_material.translucency                     = 0.5 
    bpy.context.object.active_material.raytrace_mirror.use              = True
    bpy.context.object.active_material.raytrace_mirror.reflect_factor   = 0.2
    bpy.context.object.active_material.mirror_color                     = (1, 1, 1)
    bpy.context.object.active_material.use_transparent_shadows          = True
    bpy.context.object.active_material.use_vertex_color_paint           = False
    # nozzle material
    bpy.data.objects['NozzleSurface'].select    = True
    bpy.ops.object.shade_smooth()
    bpy.context.scene.objects.active            = None
    bpy.context.scene.objects.active            = bpy.data.objects["NozzleSurface"]
    ob = bpy.context.active_object
    bpy.context.object.active_material.diffuse_color                    = (0.8, 0.8, 0.8)
    bpy.context.object.active_material.specular_intensity               = 1
    bpy.context.object.active_material.specular_hardness                = 10
    bpy.context.object.active_material.specular_color                   = (1, 1, 1)
    bpy.context.object.active_material.ambient                          = 1
    bpy.context.object.active_material.raytrace_mirror.use = True
    bpy.context.object.active_material.raytrace_mirror.reflect_factor   = 1
    bpy.context.object.active_material.mirror_color                     = (0.8, 0.8, 0.8)
    bpy.context.object.active_material.use_transparent_shadows          = True
    #
    # Add planes
    #
    # lateral plane 1
    bpy.ops.mesh.primitive_plane_add(location=(-4, 0, -1))
    bpy.context.object.scale = (4, 1, 1)
    bpy.context.object.name = 'lateralPlane1'
    # lateral plane 2
    bpy.ops.mesh.primitive_plane_add(location=(-4, 1, 0))
    bpy.context.object.scale = (4, 1, 1)
    bpy.context.object.name = 'lateralPlane2'
    bpy.context.object.rotation_euler = (pi/2, 0, 0)
    # lateral planes material
    bpy.context.scene.objects.active        = None
    bpy.context.scene.objects.active        = bpy.data.objects["lateralPlane1"]
    mat = bpy.data.materials.new(name='lateralPlaneMaterial')
    bpy.context.active_object.data.materials.append(mat)
    bpy.context.object.active_material.diffuse_color            = (0, 0, 0.56)
    bpy.context.object.active_material.use_transparent_shadows  = True
    bpy.context.object.active_material.use_cast_shadows         = False
    bpy.context.scene.objects.active        = None
    bpy.context.scene.objects.active        = bpy.data.objects["lateralPlane2"]
    mat = bpy.data.materials.new(name='lateralPlaneMaterial2')
    bpy.context.active_object.data.materials.append(mat)
    bpy.context.object.active_material.diffuse_color            = (0, 0, 0.56)
    bpy.context.object.active_material.use_transparent_shadows  = True
    bpy.context.object.active_material.use_cast_shadows         = False
    # back plane
    bpy.ops.mesh.primitive_plane_add(location=(0, 0, 0))
    bpy.context.object.name = 'backPlane'
    bpy.context.object.rotation_euler = (0, pi/2, 0)
    # lateral plane material
    mat = bpy.data.materials.new(name='backPlaneMaterial')
    bpy.context.active_object.data.materials.append(mat)
    bpy.context.object.active_material.use_transparency                 = True
    bpy.context.object.active_material.transparency_method              = 'RAYTRACE'
    bpy.context.object.active_material.raytrace_transparency.ior        = 1.1
    bpy.context.object.active_material.alpha                            = 0.1
    bpy.context.object.active_material.specular_intensity               = 1
    bpy.context.object.active_material.specular_hardness                = 511
    bpy.context.object.active_material.specular_color                   = (1, 1, 1)
    bpy.context.object.active_material.ambient                          = 0.5 
    bpy.context.object.active_material.translucency                     = 0.5 
    bpy.context.object.active_material.diffuse_color                    = (0.366, 1, 1)
    bpy.context.object.active_material.use_transparent_shadows          = True
    #
    # Lamps
    #
    lamp1 = bpy.ops.object.lamp_add(location=( 0, 0.5, 1))
    #bpy.context.object.data.shadow_method = 'RAY_SHADOW'
    lamp2 = bpy.ops.object.lamp_add(location=( 0,-0.5, 1))
    lamp3 = bpy.ops.object.lamp_add(location=(-5, 0.5, 1))
    lamp4 = bpy.ops.object.lamp_add(location=(-5,-0.5, 1))
    sun_lamp = bpy.ops.object.lamp_add(type='SUN')
    bpy.context.object.data.energy = 2.5
    bpy.context.object.data.shadow_method = 'RAY_SHADOW'
    bpy.context.object.data.use_only_shadow = True
    bpy.context.object.rotation_euler = (-pi/12, -pi/6, 0)
    #cameras
    bpy.ops.object.camera_add(location=(-8, -5.5, 2.167))
    bpy.context.object.rotation_euler = (72*pi/180, 0, -37.5*pi/180)
    # SKY
    bpy.context.scene.world.horizon_color   = (0.2, 0.2, 0.2)
    # For saving
    cam = bpy.data.objects['Camera']
    bpy.context.scene.camera = cam
    bpy.context.scene.render.resolution_x           = 7680
    bpy.context.scene.render.resolution_y           = 4320
    bpy.context.scene.render.resolution_percentage  = 25
    bpy.data.scenes['Scene'].render.filepath = 'Users/cueball/Box Sync/blender_v7/blended_17.png' 
    bpy.ops.render.render( write_still = True )
    # Delete everything
    #bpy.ops.object.select_all(action='TOGGLE')
    #bpy.ops.object.select_all(action='TOGGLE')
    #bpy.ops.object.delete()

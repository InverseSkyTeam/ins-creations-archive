#!/usr/bin/env python


from direct.showbase.ShowBase import ShowBase
from panda3d.core import ShaderTerrainMesh, Shader, load_prc_file_data
from panda3d.core import SamplerState


class ShaderTerrainDemo(ShowBase):
    def __init__(self):

        load_prc_file_data("", """
            textures-power-2 none
            gl-coordinate-system default
            window-title Panda3D ShaderTerrainMesh Demo
            filled-wireframe-apply-shader true

            # As an optimization, set this to the maximum number of cameras
            # or lights that will be rendering the terrain at any given time.
            stm-max-views 8

            # Further optimize the performance by reducing this to the max
            # number of chunks that will be visible at any given time.
            stm-max-chunk-count 2048
        """)

        ShowBase.__init__(self)

        self.camLens.set_fov(90)
        self.camLens.set_near_far(0.1, 50000)

        self.terrain_node = ShaderTerrainMesh()

        heightfield = self.loader.loadTexture("heightfield.png")
        heightfield.wrap_u = SamplerState.WM_clamp
        heightfield.wrap_v = SamplerState.WM_clamp
        self.terrain_node.heightfield = heightfield

        self.terrain_node.target_triangle_width = 10.0

        self.terrain_node.generate()
        self.terrain = self.render.attach_new_node(self.terrain_node)
        self.terrain.set_scale(1024, 1024, 100)
        self.terrain.set_pos(-512, -512, -70.0)

        terrain_shader = Shader.load(Shader.SL_GLSL, "terrain.vert.glsl", "terrain.frag.glsl")
        self.terrain.set_shader(terrain_shader)
        self.terrain.set_shader_input("camera", self.camera)
        self.accept("f3", self.toggleWireframe)
        grass_tex = self.loader.loadTexture("textures/grass.png")
        grass_tex.set_minfilter(SamplerState.FT_linear_mipmap_linear)
        grass_tex.set_anisotropic_degree(16)
        self.terrain.set_texture(grass_tex)
        skybox = self.loader.loadModel("models/skybox.bam")
        skybox.reparent_to(self.render)
        skybox.set_scale(20000)

        skybox_texture = self.loader.loadTexture("textures/skybox.jpg")
        skybox_texture.set_minfilter(SamplerState.FT_linear)
        skybox_texture.set_magfilter(SamplerState.FT_linear)
        skybox_texture.set_wrap_u(SamplerState.WM_repeat)
        skybox_texture.set_wrap_v(SamplerState.WM_mirror)
        skybox_texture.set_anisotropic_degree(16)
        skybox.set_texture(skybox_texture)

        skybox_shader = Shader.load(Shader.SL_GLSL, "skybox.vert.glsl", "skybox.frag.glsl")
        skybox.set_shader(skybox_shader)

ShaderTerrainDemo().run()

# add <script type="text/javascript" src="https://unpkg.com/three@0.144.0/build/three.js"></script>
# put pyweb3d.py to downloads/py
from browser import window, load, document
from pyweb3d import *

brython_div = document["brython_div1"]
scene = Scene()
camera = PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000 )

# Renderer
renderer = WebGLRenderer()
renderer.setSize(800, 600)
brython_div <= renderer.domElement

geometry = BoxGeometry( 1, 2, 1 )
material = MeshBasicMaterial( { 'color': 0xff0000 } )
cube = Mesh( geometry, material )
scene.add( cube )

camera.position.z = 5

def animate(time):
    window.requestAnimationFrame( animate )

    cube.rotation.x += 0.11
    cube.rotation.y += 0.11

    renderer.render( scene, camera )

animate(0)
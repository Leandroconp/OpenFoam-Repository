# trace generated using paraview version 5.6.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'OpenFOAMReader'
foamfoam = OpenFOAMReader(FileName='/media/leandro/fb922f7b-3771-491c-bc75-09d5489038e1/RunOpenFOAM/ReatorHelicoidal/Daniel_CasoT/laminar/foam.foam')

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1387, 735]

# show data in view
foamfoamDisplay = Show(foamfoam, renderView1)

# trace defaults for the display properties.
foamfoamDisplay.Representation = 'Surface'

# reset view to fit data
renderView1.ResetCamera()

# show color bar/color legend
foamfoamDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get color transfer function/color map for 'p'
pLUT = GetColorTransferFunction('p')

# get opacity transfer function/opacity map for 'p'
pPWF = GetOpacityTransferFunction('p')

# create a new 'Slice'
slice1 = Slice(Input=foamfoam)

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0518743684515357, 0.0]
slice1.SliceType.Normal = [0.0, 0.0, 1.0]

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0518743684515357, 0.0]
slice1.SliceType.Normal = [0.0, 0.0, 1.0]

# show data in view
slice1Display = Show(slice1, renderView1)

# trace defaults for the display properties.
slice1Display.Representation = 'Surface'

# hide data in view
Hide(foamfoam, renderView1)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Transform'
transform1 = Transform(Input=slice1)

# Properties modified on transform1.Transform
transform1.Transform.Rotate = [0.0, 90.0, 0.0]

# Properties modified on transform1.Transform
transform1.Transform.Rotate = [0.0, 90.0, 0.0]

# show data in view
transform1Display = Show(transform1, renderView1)

# trace defaults for the display properties.
transform1Display.Representation = 'Surface'

# hide data in view
Hide(slice1, renderView1)

# show color bar/color legend
transform1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# reset view to fit data
renderView1.ResetCamera()

# set active source
SetActiveSource(transform1)

# create a new 'Extract Selection'
extractSelection1 = ExtractSelection(Input=transform1,
    Selection=None)

# show data in view
extractSelection1Display = Show(extractSelection1, renderView1)

# trace defaults for the display properties.
extractSelection1Display.Representation = 'Surface'


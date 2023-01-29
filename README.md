# Programmier-Workshop: Python / Fortgeschrittene

![Logo](doc/mp4/CreateAnimationsWithManim.gif)

![Logo](doc/logo_manim.png)

## Create Manim Development Environment

Using Docker, we will setup a development environment on Ubuntu.

Beside of the Dockerfile to create the environment, we will utilise a Makefile to easly build and run the Manim environment.

To build the envrionnment, type:
```make build```

To run the environment, type:
```make run```

### Dockerfile

- use latest Ubuntu Version

- add sudo functionality für user

- set root password

- install latex and additional fonts
  
- install manim and manimlib
## Using Manim

Run the environment by typing ```make run``. 

This starts the docker environment with the local folder ```src```mapped into docker.

```shell
$ make run
docker run  -v ./src:/home/user/src -it manim-ubuntu
user@622fa8e5830a:~$
```

Run some examples

```shell

```
## DOC 110 DEMO.MD

|SquareToCircle|TexTransformExample|MathematicalEquation|MovingAndZoomingCamera|
|:-----:|:-----:|:-----:|:-----:|
|<img src="src/110_demo/mp4/SquareToCircle.gif" alt="SquareToCircle" style="height:200px;"/>|<img src="src/110_demo/mp4/TexTransformExample.gif" alt="TexTransformExample" style="height:200px;"/>|<img src="src/110_demo/mp4/MathematicalEquation.gif" alt="MathematicalEquation" style="height:200px;"/>|<img src="src/110_demo/mp4/MovingAndZoomingCamera.gif" alt="MovingAndZoomingCamera" style="height:200px;"/>|

|InteractiveDevelopment|ShapesReplacement|TextExample|PointMovingOnShapes|
|:-----:|:-----:|:-----:|:-----:|
|<img src="src/110_demo/mp4/InteractiveDevelopment.gif" alt="InteractiveDevelopment" style="height:200px;"/>|<img src="src/110_demo/mp4/ShapesReplacement.gif" alt="ShapesReplacement" style="height:200px;"/>|<img src="src/110_demo/mp4/TextExample.gif" alt="TextExample" style="height:200px;"/>|<img src="src/110_demo/mp4/PointMovingOnShapes.gif" alt="PointMovingOnShapes" style="height:200px;"/>|

## DOC 120 REFERENCE.MD

|ThreeDCameraRotation|MovingAngle|ThreeDCameraIllusionRotation|MobjectPlacement|
|:-----:|:-----:|:-----:|:-----:|
|<img src="src/120_reference/mp4/ThreeDCameraRotation.gif" alt="ThreeDCameraRotation" style="height:200px;"/>|<img src="src/120_reference/mp4/MovingAngle.gif" alt="MovingAngle" style="height:200px;"/>|<img src="src/120_reference/mp4/ThreeDCameraIllusionRotation.gif" alt="ThreeDCameraIllusionRotation" style="height:200px;"/>|<img src="src/120_reference/mp4/MobjectPlacement.gif" alt="MobjectPlacement" style="height:200px;"/>|

|FixedInFrameMObjectTest|ThreeDSurfacePlot|MovingDots|MovingAround|
|:-----:|:-----:|:-----:|:-----:|
|<img src="src/120_reference/mp4/FixedInFrameMObjectTest.gif" alt="FixedInFrameMObjectTest" style="height:200px;"/>|<img src="src/120_reference/mp4/ThreeDSurfacePlot.gif" alt="ThreeDSurfacePlot" style="height:200px;"/>|<img src="src/120_reference/mp4/MovingDots.gif" alt="MovingDots" style="height:200px;"/>|<img src="src/120_reference/mp4/MovingAround.gif" alt="MovingAround" style="height:200px;"/>|

|MovingGroupToDestination|ArgMinExample|ShowScreenResolution|AnimateExample|
|:-----:|:-----:|:-----:|:-----:|
|<img src="src/120_reference/mp4/MovingGroupToDestination.gif" alt="MovingGroupToDestination" style="height:200px;"/>|<img src="src/120_reference/mp4/ArgMinExample.gif" alt="ArgMinExample" style="height:200px;"/>|<img src="src/120_reference/mp4/ShowScreenResolution.gif" alt="ShowScreenResolution" style="height:200px;"/>|<img src="src/120_reference/mp4/AnimateExample.gif" alt="AnimateExample" style="height:200px;"/>|

|ExampleTransform|RotationUpdater|SquareToCircle2|SquareToCircle3|
|:-----:|:-----:|:-----:|:-----:|
|<img src="src/120_reference/mp4/ExampleTransform.gif" alt="ExampleTransform" style="height:200px;"/>|<img src="src/120_reference/mp4/RotationUpdater.gif" alt="RotationUpdater" style="height:200px;"/>|<img src="src/120_reference/mp4/SquareToCircle2.gif" alt="SquareToCircle2" style="height:200px;"/>|<img src="src/120_reference/mp4/SquareToCircle3.gif" alt="SquareToCircle3" style="height:200px;"/>|

|FollowingGraphCamera|CoordsToPointExample|ExampleRotation|PointToCoordsExample|
|:-----:|:-----:|:-----:|:-----:|
|<img src="src/120_reference/mp4/FollowingGraphCamera.gif" alt="FollowingGraphCamera" style="height:200px;"/>|<img src="src/120_reference/mp4/CoordsToPointExample.gif" alt="CoordsToPointExample" style="height:200px;"/>|<img src="src/120_reference/mp4/ExampleRotation.gif" alt="ExampleRotation" style="height:200px;"/>|<img src="src/120_reference/mp4/PointToCoordsExample.gif" alt="PointToCoordsExample" style="height:200px;"/>|

|PointWithTrace|LineGraphExample|SquareAndCircle2|LogScalingExample|
|:-----:|:-----:|:-----:|:-----:|
|<img src="src/120_reference/mp4/PointWithTrace.gif" alt="PointWithTrace" style="height:200px;"/>|<img src="src/120_reference/mp4/LineGraphExample.gif" alt="LineGraphExample" style="height:200px;"/>|<img src="src/120_reference/mp4/SquareAndCircle2.gif" alt="SquareAndCircle2" style="height:200px;"/>|<img src="src/120_reference/mp4/LogScalingExample.gif" alt="LogScalingExample" style="height:200px;"/>|

|AnimatedSquareToCircle2|RunTime|DifferentRotations2|Shapes|
|:-----:|:-----:|:-----:|:-----:|
|<img src="src/120_reference/mp4/AnimatedSquareToCircle2.gif" alt="AnimatedSquareToCircle2" style="height:200px;"/>|<img src="src/120_reference/mp4/RunTime.gif" alt="RunTime" style="height:200px;"/>|<img src="src/120_reference/mp4/DifferentRotations2.gif" alt="DifferentRotations2" style="height:200px;"/>|<img src="src/120_reference/mp4/Shapes.gif" alt="Shapes" style="height:200px;"/>|

|MobjectStyling|Formula1|IterateColor|SineCurveUnitCircle|
|:-----:|:-----:|:-----:|:-----:|
|<img src="src/120_reference/mp4/MobjectStyling.gif" alt="MobjectStyling" style="height:200px;"/>|<img src="src/120_reference/mp4/Formula1.gif" alt="Formula1" style="height:200px;"/>|<img src="src/120_reference/mp4/IterateColor.gif" alt="IterateColor" style="height:200px;"/>|<img src="src/120_reference/mp4/SineCurveUnitCircle.gif" alt="SineCurveUnitCircle" style="height:200px;"/>|

|OpeningManim|BooleanOperations|MobjectZOrder|PointMovingOnShapes|
|:-----:|:-----:|:-----:|:-----:|
|<img src="src/120_reference/mp4/OpeningManim.gif" alt="OpeningManim" style="height:200px;"/>|<img src="src/120_reference/mp4/BooleanOperations.gif" alt="BooleanOperations" style="height:200px;"/>|<img src="src/120_reference/mp4/MobjectZOrder.gif" alt="MobjectZOrder" style="height:200px;"/>|<img src="src/120_reference/mp4/PointMovingOnShapes.gif" alt="PointMovingOnShapes" style="height:200px;"/>|

|CreatingMobjects|SomeAnimations|MovingFrameBox|CreateCircle|
|:-----:|:-----:|:-----:|:-----:|
|<img src="src/120_reference/mp4/CreatingMobjects.gif" alt="CreatingMobjects" style="height:200px;"/>|<img src="src/120_reference/mp4/SomeAnimations.gif" alt="SomeAnimations" style="height:200px;"/>|<img src="src/120_reference/mp4/MovingFrameBox.gif" alt="MovingFrameBox" style="height:200px;"/>|<img src="src/120_reference/mp4/CreateCircle.gif" alt="CreateCircle" style="height:200px;"/>|

## DOC 121 MANIM.MD

|AddToVGroup|Anagram|AnimateChainExample|AnimateExample|
|:-----:|:-----:|:-----:|:-----:|
|<img src="src/121_manim/mp4/AddToVGroup.gif" alt="AddToVGroup" style="height:200px;"/>|<img src="src/121_manim/mp4/Anagram.gif" alt="Anagram" style="height:200px;"/>|<img src="src/121_manim/mp4/AnimateChainExample.gif" alt="AnimateChainExample" style="height:200px;"/>|<img src="src/121_manim/mp4/AnimateExample.gif" alt="AnimateExample" style="height:200px;"/>|

|AnimateWithArgsExample|AnimatedBoundaryExample|AnimationOverrideExample|ApplyFuncExample|
|:-----:|:-----:|:-----:|:-----:|
|<img src="src/121_manim/mp4/AnimateWithArgsExample.gif" alt="AnimateWithArgsExample" style="height:200px;"/>|<img src="src/121_manim/mp4/AnimatedBoundaryExample.gif" alt="AnimatedBoundaryExample" style="height:200px;"/>|<img src="src/121_manim/mp4/AnimationOverrideExample.gif" alt="AnimationOverrideExample" style="height:200px;"/>|<img src="src/121_manim/mp4/ApplyFuncExample.gif" alt="ApplyFuncExample" style="height:200px;"/>|

|ApplyingWaves|ArcBetweenPointsExample|ArcPolygonExample|ArcPolygonExample2|
|:-----:|:-----:|:-----:|:-----:|
|<img src="src/121_manim/mp4/ApplyingWaves.gif" alt="ApplyingWaves" style="height:200px;"/>|<img src="src/121_manim/mp4/ArcBetweenPointsExample.gif" alt="ArcBetweenPointsExample" style="height:200px;"/>|<img src="src/121_manim/mp4/ArcPolygonExample.gif" alt="ArcPolygonExample" style="height:200px;"/>|<img src="src/121_manim/mp4/ArcPolygonExample2.gif" alt="ArcPolygonExample2" style="height:200px;"/>|

|ArgMinExample|BecomeScene|BraceBPExample|BroadcastExample|
|:-----:|:-----:|:-----:|:-----:|
|<img src="src/121_manim/mp4/ArgMinExample.gif" alt="ArgMinExample" style="height:200px;"/>|<img src="src/121_manim/mp4/BecomeScene.gif" alt="BecomeScene" style="height:200px;"/>|<img src="src/121_manim/mp4/BraceBPExample.gif" alt="BraceBPExample" style="height:200px;"/>|<img src="src/121_manim/mp4/BroadcastExample.gif" alt="BroadcastExample" style="height:200px;"/>|

|ChangeGraphLayout|ChangeOfDirection|ChangingCameraWidthAndRestore|ChangingZoomScale|
|:-----:|:-----:|:-----:|:-----:|
|<img src="src/121_manim/mp4/ChangeGraphLayout.gif" alt="ChangeGraphLayout" style="height:200px;"/>|<img src="src/121_manim/mp4/ChangeOfDirection.gif" alt="ChangeOfDirection" style="height:200px;"/>|<img src="src/121_manim/mp4/ChangingCameraWidthAndRestore.gif" alt="ChangingCameraWidthAndRestore" style="height:200px;"/>|<img src="src/121_manim/mp4/ChangingZoomScale.gif" alt="ChangingZoomScale" style="height:200px;"/>|

|ClockwisePathExample|ComplexValueTrackerExample|ContinuousMotion|CounterclockwisePathExample|
|:-----:|:-----:|:-----:|:-----:|
|<img src="src/121_manim/mp4/ClockwisePathExample.gif" alt="ClockwisePathExample" style="height:200px;"/>|<img src="src/121_manim/mp4/ComplexValueTrackerExample.gif" alt="ComplexValueTrackerExample" style="height:200px;"/>|<img src="src/121_manim/mp4/ContinuousMotion.gif" alt="ContinuousMotion" style="height:200px;"/>|<img src="src/121_manim/mp4/CounterclockwisePathExample.gif" alt="CounterclockwisePathExample" style="height:200px;"/>|

|CreateScene|CreateTableExample|CreatingMobjects|CutoutExample|
|:-----:|:-----:|:-----:|:-----:|
|<img src="src/121_manim/mp4/CreateScene.gif" alt="CreateScene" style="height:200px;"/>|<img src="src/121_manim/mp4/CreateTableExample.gif" alt="CreateTableExample" style="height:200px;"/>|<img src="src/121_manim/mp4/CreatingMobjects.gif" alt="CreatingMobjects" style="height:200px;"/>|<img src="src/121_manim/mp4/CutoutExample.gif" alt="CutoutExample" style="height:200px;"/>|

|DarkThemeBanner|DifferentFadeTransforms|DissipatingPathExample|DtUpdater|
|:-----:|:-----:|:-----:|:-----:|
|<img src="src/121_manim/mp4/DarkThemeBanner.gif" alt="DarkThemeBanner" style="height:200px;"/>|<img src="src/121_manim/mp4/DifferentFadeTransforms.gif" alt="DifferentFadeTransforms" style="height:200px;"/>|<img src="src/121_manim/mp4/DissipatingPathExample.gif" alt="DissipatingPathExample" style="height:200px;"/>|<img src="src/121_manim/mp4/DtUpdater.gif" alt="DtUpdater" style="height:200px;"/>|

|EndAnimation|ExampleTransform|ExpandDirections|FadeInExample|
|:-----:|:-----:|:-----:|:-----:|
|<img src="src/121_manim/mp4/EndAnimation.gif" alt="EndAnimation" style="height:200px;"/>|<img src="src/121_manim/mp4/ExampleTransform.gif" alt="ExampleTransform" style="height:200px;"/>|<img src="src/121_manim/mp4/ExpandDirections.gif" alt="ExpandDirections" style="height:200px;"/>|<img src="src/121_manim/mp4/FadeInExample.gif" alt="FadeInExample" style="height:200px;"/>|

|FadeTransformSubmobjects|Fading|FlashOnCircle|GrowArrowExample|
|:-----:|:-----:|:-----:|:-----:|
|<img src="src/121_manim/mp4/FadeTransformSubmobjects.gif" alt="FadeTransformSubmobjects" style="height:200px;"/>|<img src="src/121_manim/mp4/Fading.gif" alt="Fading" style="height:200px;"/>|<img src="src/121_manim/mp4/FlashOnCircle.gif" alt="FlashOnCircle" style="height:200px;"/>|<img src="src/121_manim/mp4/GrowArrowExample.gif" alt="GrowArrowExample" style="height:200px;"/>|

|GrowFromCenterExample|GrowFromEdgeExample|GrowFromPointExample|Growing|
|:-----:|:-----:|:-----:|:-----:|
|<img src="src/121_manim/mp4/GrowFromCenterExample.gif" alt="GrowFromCenterExample" style="height:200px;"/>|<img src="src/121_manim/mp4/GrowFromEdgeExample.gif" alt="GrowFromEdgeExample" style="height:200px;"/>|<img src="src/121_manim/mp4/GrowFromPointExample.gif" alt="GrowFromPointExample" style="height:200px;"/>|<img src="src/121_manim/mp4/Growing.gif" alt="Growing" style="height:200px;"/>|

|HeightExample|Indications|InvertSumobjectsExample|JustifyText|
|:-----:|:-----:|:-----:|:-----:|
|<img src="src/121_manim/mp4/HeightExample.gif" alt="HeightExample" style="height:200px;"/>|<img src="src/121_manim/mp4/Indications.gif" alt="Indications" style="height:200px;"/>|<img src="src/121_manim/mp4/InvertSumobjectsExample.gif" alt="InvertSumobjectsExample" style="height:200px;"/>|<img src="src/121_manim/mp4/JustifyText.gif" alt="JustifyText" style="height:200px;"/>|

|LagRatios|LightThemeBanner|LineExample|LinearTransformationSceneExample|
|:-----:|:-----:|:-----:|:-----:|
|<img src="src/121_manim/mp4/LagRatios.gif" alt="LagRatios" style="height:200px;"/>|<img src="src/121_manim/mp4/LightThemeBanner.gif" alt="LightThemeBanner" style="height:200px;"/>|<img src="src/121_manim/mp4/LineExample.gif" alt="LineExample" style="height:200px;"/>|<img src="src/121_manim/mp4/LinearTransformationSceneExample.gif" alt="LinearTransformationSceneExample" style="height:200px;"/>|

|MatchPointsScene|MatchingEquationParts|MobjectPlacement|MobjectStyling|
|:-----:|:-----:|:-----:|:-----:|
|<img src="src/121_manim/mp4/MatchPointsScene.gif" alt="MatchPointsScene" style="height:200px;"/>|<img src="src/121_manim/mp4/MatchingEquationParts.gif" alt="MatchingEquationParts" style="height:200px;"/>|<img src="src/121_manim/mp4/MobjectPlacement.gif" alt="MobjectPlacement" style="height:200px;"/>|<img src="src/121_manim/mp4/MobjectStyling.gif" alt="MobjectStyling" style="height:200px;"/>|

|MobjectZOrder|MoveAlongPathExample|MovingAndZoomingCamera|MovingCameraCenter|
|:-----:|:-----:|:-----:|:-----:|
|<img src="src/121_manim/mp4/MobjectZOrder.gif" alt="MobjectZOrder" style="height:200px;"/>|<img src="src/121_manim/mp4/MoveAlongPathExample.gif" alt="MoveAlongPathExample" style="height:200px;"/>|<img src="src/121_manim/mp4/MovingAndZoomingCamera.gif" alt="MovingAndZoomingCamera" style="height:200px;"/>|<img src="src/121_manim/mp4/MovingCameraCenter.gif" alt="MovingCameraCenter" style="height:200px;"/>|

|MovingCameraOnGraph|MovingDots|MovingGroupToDestination|MovingSquareWithUpdaters|
|:-----:|:-----:|:-----:|:-----:|
|<img src="src/121_manim/mp4/MovingCameraOnGraph.gif" alt="MovingCameraOnGraph" style="height:200px;"/>|<img src="src/121_manim/mp4/MovingDots.gif" alt="MovingDots" style="height:200px;"/>|<img src="src/121_manim/mp4/MovingGroupToDestination.gif" alt="MovingGroupToDestination" style="height:200px;"/>|<img src="src/121_manim/mp4/MovingSquareWithUpdaters.gif" alt="MovingSquareWithUpdaters" style="height:200px;"/>|

|MovingVertices|MyScene|NextToUpdater|Nudging|
|:-----:|:-----:|:-----:|:-----:|
|<img src="src/121_manim/mp4/MovingVertices.gif" alt="MovingVertices" style="height:200px;"/>|<img src="src/121_manim/mp4/MyScene.gif" alt="MyScene" style="height:200px;"/>|<img src="src/121_manim/mp4/NextToUpdater.gif" alt="NextToUpdater" style="height:200px;"/>|<img src="src/121_manim/mp4/Nudging.gif" alt="Nudging" style="height:200px;"/>|

|OverrideAnimationExample|PathAlongArcExample|PathAlongCirclesExample|PointCloudDotExample2|
|:-----:|:-----:|:-----:|:-----:|
|<img src="src/121_manim/mp4/OverrideAnimationExample.gif" alt="OverrideAnimationExample" style="height:200px;"/>|<img src="src/121_manim/mp4/PathAlongArcExample.gif" alt="PathAlongArcExample" style="height:200px;"/>|<img src="src/121_manim/mp4/PathAlongCirclesExample.gif" alt="PathAlongCirclesExample" style="height:200px;"/>|<img src="src/121_manim/mp4/PointCloudDotExample2.gif" alt="PointCloudDotExample2" style="height:200px;"/>|

|PolygramExample|RateFunctions1Example|RunTime|ScaleVectorFieldFunction|
|:-----:|:-----:|:-----:|:-----:|
|<img src="src/121_manim/mp4/PolygramExample.gif" alt="PolygramExample" style="height:200px;"/>|<img src="src/121_manim/mp4/RateFunctions1Example.gif" alt="RateFunctions1Example" style="height:200px;"/>|<img src="src/121_manim/mp4/RunTime.gif" alt="RunTime" style="height:200px;"/>|<img src="src/121_manim/mp4/ScaleVectorFieldFunction.gif" alt="ScaleVectorFieldFunction" style="height:200px;"/>|

|SeveralArcPolygons|Shapes|ShapesWithVDict|ShowDrawBorderThenFill|
|:-----:|:-----:|:-----:|:-----:|
|<img src="src/121_manim/mp4/SeveralArcPolygons.gif" alt="SeveralArcPolygons" style="height:200px;"/>|<img src="src/121_manim/mp4/Shapes.gif" alt="Shapes" style="height:200px;"/>|<img src="src/121_manim/mp4/ShapesWithVDict.gif" alt="ShapesWithVDict" style="height:200px;"/>|<img src="src/121_manim/mp4/ShowDrawBorderThenFill.gif" alt="ShowDrawBorderThenFill" style="height:200px;"/>|

|ShowIncreasingSubsetsScene|ShowUncreate|ShowWrite|ShowWriteReversed|
|:-----:|:-----:|:-----:|:-----:|
|<img src="src/121_manim/mp4/ShowIncreasingSubsetsScene.gif" alt="ShowIncreasingSubsetsScene" style="height:200px;"/>|<img src="src/121_manim/mp4/ShowUncreate.gif" alt="ShowUncreate" style="height:200px;"/>|<img src="src/121_manim/mp4/ShowWrite.gif" alt="ShowWrite" style="height:200px;"/>|<img src="src/121_manim/mp4/ShowWriteReversed.gif" alt="ShowWriteReversed" style="height:200px;"/>|

|ShuffleSubmobjectsExample|SizingAndSpacing|SomeAnimations|SpinInFromNothingExample|
|:-----:|:-----:|:-----:|:-----:|
|<img src="src/121_manim/mp4/ShuffleSubmobjectsExample.gif" alt="ShuffleSubmobjectsExample" style="height:200px;"/>|<img src="src/121_manim/mp4/SizingAndSpacing.gif" alt="SizingAndSpacing" style="height:200px;"/>|<img src="src/121_manim/mp4/SomeAnimations.gif" alt="SomeAnimations" style="height:200px;"/>|<img src="src/121_manim/mp4/SpinInFromNothingExample.gif" alt="SpinInFromNothingExample" style="height:200px;"/>|

|SpiralPathExample|StraightPathExample|StreamLineCreation|TracedPathExample|
|:-----:|:-----:|:-----:|:-----:|
|<img src="src/121_manim/mp4/SpiralPathExample.gif" alt="SpiralPathExample" style="height:200px;"/>|<img src="src/121_manim/mp4/StraightPathExample.gif" alt="StraightPathExample" style="height:200px;"/>|<img src="src/121_manim/mp4/StreamLineCreation.gif" alt="StreamLineCreation" style="height:200px;"/>|<img src="src/121_manim/mp4/TracedPathExample.gif" alt="TracedPathExample" style="height:200px;"/>|

|UnwriteReverseFalse|UnwriteReverseTrue|UseZoomedScene|UsingFlash|
|:-----:|:-----:|:-----:|:-----:|
|<img src="src/121_manim/mp4/UnwriteReverseFalse.gif" alt="UnwriteReverseFalse" style="height:200px;"/>|<img src="src/121_manim/mp4/UnwriteReverseTrue.gif" alt="UnwriteReverseTrue" style="height:200px;"/>|<img src="src/121_manim/mp4/UseZoomedScene.gif" alt="UseZoomedScene" style="height:200px;"/>|<img src="src/121_manim/mp4/UsingFlash.gif" alt="UsingFlash" style="height:200px;"/>|

|UsingFocusOn|UsingIndicate|ValueTrackerExample|VariableExample|
|:-----:|:-----:|:-----:|:-----:|
|<img src="src/121_manim/mp4/UsingFocusOn.gif" alt="UsingFocusOn" style="height:200px;"/>|<img src="src/121_manim/mp4/UsingIndicate.gif" alt="UsingIndicate" style="height:200px;"/>|<img src="src/121_manim/mp4/ValueTrackerExample.gif" alt="ValueTrackerExample" style="height:200px;"/>|<img src="src/121_manim/mp4/VariableExample.gif" alt="VariableExample" style="height:200px;"/>|

## Additional Readings

[Talking Physics - A conversation about teaching and learning physics](https://talkingphysics.wordpress.com/2018/07/13/fields-of-a-moving-charge-manim-series-part-11/)


[readthedocs - manim documentation/examples](https://manimce--458.org.readthedocs.build/en/458/examples.html)


https://financial-engineering.medium.com/manim-examples-3ec2a6e985c5


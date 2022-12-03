SEGMENTATION

Segmentation is often referred to as the clustering of pixels of a similar category.
In traditional segmentation techniques, the key property used is image intensity levels.
First, different smaller regions of similar intensity values are found, and later they are merged into
larger regions. 
To get the best performance, an initial point is chosen by the user for
algorithms. Recent approaches using deep learning have shown better performance without
the need for initialization.

CHALLENGES

The challenges in a segmentation task are greater than the previous object detection task, as
the complexity of detection is increased:

• Noisy boundaries: Grouping pixels that belong to a category may not be as accurate
due to the fuzzy edges of an object. As a result, objects from different categories are
clustered together.
• Cluttered scene: With several objects in the image frame, it becomes harder to
classify pixels correctly. With more clutter, the chances of false positive classification
also increase


TRACKING

Tracking is the problem of estimating the position of an object over consecutive image
sequences. This is also further divided into single object tracking and multiple object
tracking, however, both single and multi-object tracking require slightly different
approaches.

CHALLENGES

It is always crucial to know which challenges we need to take care of before building apps.
As a standard computer vision method, a lot of the challenges here are common:

• Object occlusion: If the target object is hidden behind other objects in a sequence of
images, then it becomes not only hard to detect the object but also to update future
images if it becomes visible again.

• Fast movement: Cameras, such as on smartphones, often suffers from jittery
movement. This causes a blurring effect and, sometimes, the complete absence of an
object from the frame. Therefore, sudden changes in the motion of cameras also lead
to problems in tracking applications.

• Change of shape: If we are targeting non-rigid objects, changes in shape or the
complete deformation of an object will often lead to being unable to detect the
object and also tracking failure.

• False positives: In a scene with multiple similar objects, it is hard to match which
object is targeted in subsequent images. The tracker may lose the current object in
terms of detection and start tracking a similar object.


METHODS FOR OBJECT TRACKING

An intuitive method for tracking is to use the object detection method from the previous
chapter and compute detection in each frame. This will result in a bounding box detection for
every frame, but we would also like to know if a particular object stays in the image
sequence and for how many frames, that is, to keep track of K-frames for the object in the
scene. We would also need a matching strategy to say that the object found in the previous
image is the same as the one in the current image frame.

Continuing with this intuition, we add a predictor for the bounding box motion. We assume a
state for the bounding box, which consists of coordinates for the box center as well as its
velocities. This state changes as we see more boxes in the sequence.

Given the current state of the box, we can predict a possible region for where it will be in the
next frame by assuming some noise in our measurement. The object detector can search for
an object similar to the previous object in the next possible region. The location of the newly
found object box and the previous box state will help us to update the new state of the box.
This will be used for the next frame. As a result, iterating this process over all of the frames
will result in not only the tracking of the object bounding box but keeping a location check
on particular objects over the whole sequence. This method of tracking is also termed
as tracking by detection.


In tracking by detection, each frame uses an object detector to find possible instances of
objects and matches those detections with corresponding objects in the previous frame.

On the other hand, if no object detector is to be used, we can initialize the target object and
track it by matching it and finding a similar object in each frame.


DeepSort for Object Tracking

Using the richer functions of CNN's to perform tracking. DeepSort is a recent algorithm for tracking
that extends Simple Online Real-Time Tracking (SORT) and has shown remarkable results in the Multiple Object 
Tracking (MOT) problems.

In the problem setting of MOT, each frame has more than one object to track. A generic
method to solve this has two steps:

• Detection: First, all the objects are detected in the frame. There can be single or
multiple detections.

• Association: Once we have detections for the frame, a matching is performed for
similar detections with respect to the previous frame. The matched frames are
followed through the sequence to get the tracking for an object.

In Deep SORT, this generic method is further divided into three steps:

1. To compute detections, a popular CNN-based object detection method is used.The Faster-RCNN is used to perform the initial detection per frame.This method is two-stage object detection, which
performs well for object detection, even in cases of object transformations and
occlusions.
2. The intermediate step before data association consists of an estimation model. This
uses the state of each track as a vector of eight quantities, that is, box center (x, y),
box scale (s), box aspect ratio (a), and their derivatives with time as velocities. The
Kalman filter is used to model these states as a dynamical system. If there is no
detection of a tracking object for a threshold of consecutive frames, it is considered
to be out of frame or lost. For a newly detected box, the new track is started.

3. In the final step, given the predicted states from Kalman filtering using the previous
information and the newly detected box in the current frame, an association is made
for the new detection with old object tracks in the previous frame. This is computed
using Hungarian algorithm on bipartite graph matching. This is made even more
robust by setting the weights of the matching with distance formulation.




For Effective Demo of DeepSort, You can have a look at the official Repository :
https://github.com/nwojke/deep_sort

Dataset for DeepSort can be downloaded from:
https://motchallenge.net/data/MOT16.zip



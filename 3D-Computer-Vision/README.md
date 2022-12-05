Dataset - RGDB 

https://vision.in.tum.de/data/datasets/rgbd-dataset/download.

Image Formation

Geometry of image formation, it is necessary to introduce the homogeneous coordinate system.
The physical world coordinate system is referred to as Euclidean coordinate system. 
In the image plane, a point P' with (x, y) coordinates is
represented in homogeneous coordinate system as (x, y, 1). Similarly a point Pw with (x, y,
z) in world coordinates can be represented in homogeneous coordinate system as (x, y, z, 1).

To convert back from homogeneous to Euclidean, we need to divide by the last coordinate
value. To convert a point on an image plane in homogeneous system as (x,y, w) to Euclidean
system as (x/w, y/w) . Similarly, for a 3D point in a homogeneous system given by (x, y, z,
w), the Euclidean coordinates are given by (x/w, y/w, z/ w).

Image formation comes from transforming physical world coordinates to image plane
coordinates but losing information about an extra dimension. This means that when we
construct an image we are losing depth information for each pixel. As a result, converting
back from image pixel coordinates to real-world coordinates is not possible.

There can be an infinite number of points lying along the line. 
Points P1, P2, and P3 have the same image pixel location, and therefore
estimations of depth (distance from camera) are lost during image formation. 

Check Figure Image-Formation in Images Folder.


EPIPOLAR GEOMETRY 

The camera centers O1 and O2 are connected to point Pw in the world, and the plane forming the line Pw, O1, O2 is the epipolar plane. 

The points where the camera's center line O1O2 intersects with the image are epipoles for the image.
These may or may not lie on the image. In cases where both the image planes are parallel, the epipoles will lie at infinity.

Here, we can define an epipolar constraint, as if we know the transformation
between camera center O1 and O2 as translation T and rotation R, we can compute the
location of point P1 in Image 1 to the corresponding location in Image 2.

Check Epipolar Geometry Figure in the images folder.

Aligning Images

Image alignment is a problem for computing a transformation matrix so that on applying that
transformation to an input image, it can be converted to the target image plane. As a result,
the resulting images look like they are stitched together and form a continuous larger image.

Panorama is one such example of aligning images, where we collect images of a scene with
changing camera angles and the resulting image is a combination of images aligned

Check Panorama Figure in Images Folder.
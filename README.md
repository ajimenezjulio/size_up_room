# Sizing Room
Estimate dimensions of a room with a **single 2-D image** is an extremely difficult challenge due to the lack of spatial information. However the results obtained in this approach were **very satisfactory** and through improvements of the model, it is possible to achieve it. The approach  has the next 4 steps.

1. Computation of Vanishing points
2. Wall segmentation using the [ade20k](http://sceneparsing.csail.mit.edu/) dataset and following the approach by [hellochick](https://github.com/hellochick/Indoor-segmentation)
3. Hough lines transformation to reduce the oscilations in the edges
4. Object recognition using a RNN trained on COCO dataset (for this approach we need to know the size of one object)

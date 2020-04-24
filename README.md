# trt-mtcnn

Forked from https://github.com/jkjung-avt/tensorrt_demos, this contains only MTCNN code. A small wrapper class (`TrtMTCNNWrapper`) was written for `aisecurity` use using the `mtcnn` code from the original repository.

## Usage

Can only be used on the production Jetson Nanos / GPU development machines.

1. Clone repository to `~/.aisecurity`
2. Run `make` in `trt-mtcnn/mtcnn`
3. Run `./create_engines` in `trt-mtcnn/mtcnn`
4. Run `make` in `trt-mtcnn`
5. Use `detector="trt-mtcnn"` in `aisecurity.FaceNet`'s `real_time_recognize`

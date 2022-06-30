import sys
from timeit import default_timer as timer

import cv2

sys.path.insert(1, "../..")
from trt_mtcnn import TrtMTCNNWrapper
from util.visuals import GraphicsRenderer, Camera


if __name__ == "__main__":
    mtcnn = TrtMTCNNWrapper(
        "mtcnn/det1.engine", "mtcnn/det2.engine", "mtcnn/det3.engine"
    )

    cap = Camera(threaded=False)
    graphics = GraphicsRenderer()

    try:
        visuals = bool(int(sys.argv[1]))
    except IndexError:
        print("USAGE: python3 cam_test.py [visuals]")
        sys.exit(1)

    while True:
        _, frame = cap.read()

        start = timer()
        result = mtcnn.detect_faces(frame)
        elapsed = timer() - start

        if result:
            if visuals:
                for person in result:
                    graphics.add_graphics(frame, person, True, "", elapsed)
            print("FACE DETECTED!!")
        print(f"{elapsed * 1000} ms")

        if visuals:
            cv2.imshow("cam test", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

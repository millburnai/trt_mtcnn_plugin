from utils.mtcnn import TrtMtcnn

class TrtMTCNNWrapper:

    LANDMARK_KEY = ["left_eye", "mouth_left", "nose", "right_eye", "mouth_right"]

    def __init__(self):
        self.mtcnn = TrtMtcnn()

    def detect_faces(self, img, minsize=40):
        result = []

        boxes, landmarks = self.mtcnn.detect(img[:, :, ::-1], minsize=minsize)
        for box, features in zip(boxes, landmarks):
            face = {}

            face["confidence"] = box[-1]

            x1, y1, x2, y2 = [int(coord) for coord in box[:-1]]
            face["box"] = [x1, y1, x2 - x1, y2 - y1]

            x_key, y_key = features[:5], features[5:]
            face["keypoints"] = {
                feat: (int(x), int(y)) for feat, x, y in zip(self.LANDMARK_KEY, x_key, y_key)
            }

            result.append(face)

        return result

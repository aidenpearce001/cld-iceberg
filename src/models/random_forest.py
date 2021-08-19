from utils.feature_extraction import Extractor
import numpy as np
import joblib


class RandomForest():
    def __init__(self, ckpt_path="./model/weights/rf_final.pkl"):
        self.ckpt_path = ckpt_path
        self.extractor = Extractor()
        self.classifier = joblib.load(ckpt_path)

    def predict(self, url):
        url_feature_vector = self.extractor(url)

        if url_feature_vector is not None:
            url_feature_vector = list(url_feature_vector)
            feature_vector = [feature[1] for feature in url_feature_vector]
            vector = np.array(feature_vector[:-3])
            prediction = self.classifier.predict(vector.reshape(1, -1))

            return prediction, url_feature_vector
        else:
            return None, None

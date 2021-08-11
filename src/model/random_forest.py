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
            vector = np.array(url_feature_vector[:-3])
            prediction = self.classifier.predict(vector.reshape(1, -1))
            
            return prediction
        else:
            return None

from .convolution import ConvModel
from .random_forest import RandomForest

__model_factory = {
    "cnn": ConvModel
    "rf": RandomForest
 }

def show_avail_models():
    """Displays available models

    Examples:
        >>> import models
        >>> models.show_avai_models()
    """

    print(list(__model_factory.keys()))

def build_model(name):
    pass

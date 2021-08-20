from .random_forest import *
from .cnn_char import *

__model_factory = {
    "rf": RandomForest,
    "cnn_char": CNN
 }

__config_factory = {
    "cnn_char": CNNconf
}

def show_avail_models():
    """Displays available models

    Examples:
        >>> import models
        >>> models.show_avai_models()
    """

    print(list(__model_factory.keys()))

def build_model(name):
    if name not in __model_factory:
        raise KeyError("Model name not exists, current model support: ", __model_factory.keys())
    
    config = __config_factory[name]
    return __model_factory[name](config)

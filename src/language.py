import requests
import os
EINSTEIN_VISION_URL = os.getenv('EINSTEIN_VISION_URL')
_LANGUAGE_URL = EINSTEIN_VISION_URL+"/v2/language/intent"


def predict_for_intent(token, model_id, document):
    """Run a prediction against a model using image url.

    Args:
        token: oauth token
        model_id: model id
        document: Text for which you want to return an intent prediction.
        https://metamind.readme.io/reference#prediction-intent

    Returns:
        Returns an intent prediction for the given string.
    """

    payload = {'document': (None, document),
               'modelId': (None, model_id)}
    headers = {'Authorization': 'Bearer ' + token, 'Cache-Control': 'no-cache'}
    return _prediction_request(_LANGUAGE_URL, payload, headers)


def _prediction_request(url, payload, headers):
    """Make a prediction request.
    Args:
        url: endpoint url
        data: multipart payload
        headers: request headers

    Returns:
        JSON response
    """
    try:
        response = requests.post(url, files=payload, headers=headers)
        return response
    except requests.exceptions.RequestException as exp:
        raise exp("Prediction failed: \"{}\"".format(response))

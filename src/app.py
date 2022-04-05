import os
import sys
import json
import time
import pprint
import traceback

import jwt_helper
import language as language
# import prediction
import token_generator

from dotenv import load_dotenv

load_dotenv()
# Read account id and private from environment variables
account_id = os.getenv('EINSTEIN_VISION_ACCOUNT_ID')
private_key = os.getenv('EINSTEIN_VISION_PRIVATE_KEY')
model_id = os.getenv('EINSTEIN_MODEL_ID')


def _language(access_token, model_id, msg):
    # https://metamind.readme.io/reference#prediction-intent
    # Returns a sentiment prediction for the given string.
    sentiment_prediction = language.predict_for_intent(
        access_token, model_id, msg)
    pprint.pprint(sentiment_prediction.json())


def _vision(access_token):
    print('vision')
    # # Make a prediction call using image url
    # prediction_url_response = prediction.predict_with_url(access_token, 'GeneralImageClassifier',
    #     'https://animalso.com/wp-content/uploads/2017/01/Siberian-Husky_7.jpg')

    # # Print prediction response
    # pprint.pprint(prediction_url_response.json())

    # Make a prediction call using image file
    # prediction_file_response = prediction.predict_with_image_file(access_token, 'GeneralImageClassifier',
    #     '/path/to/image/file/Siberian-Husky.jpg')

    # Print prediction response
    # pprint.pprint(prediction_file_response.json())


def get_token():

    try:

        # account_id = os.environ['EINSTEIN_VISION_ACCOUNT_ID']
        # private_key = os.environ['EINSTEIN_VISION_PRIVATE_KEY'].decode('string_escape')

        # Set expiry time
        expiry = int(time.time()) + (15*60)

        # Generate an assertion using RSA private key
        assertion = jwt_helper.generate_assertion(
            account_id, private_key, expiry)

        # Obtain oauth token
        token = token_generator.generate_token(assertion)
        response = token.json()

        # If there is no token print the response
        if 'access_token' not in response:
            raise ValueError(
                "Access token generation failed. Received reply: \"{}\"".format(response))
        else:
            # Collect the access token from response
            access_token = response['access_token']
        return access_token

    except Exception as e:
        traceback.print_exc()


if __name__ == "__main__":
    access_token = get_token()
    msg = 'where is my ticket'
    _language(access_token, model_id, msg)
    # _vision(access_token)

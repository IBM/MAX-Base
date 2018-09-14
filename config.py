# Flask settings
DEBUG = False

# Flask-restplus settings
RESTPLUS_MASK_SWAGGER = False

# Application settings

# API metadata
API_TITLE = 'Model Asset Exchange Server'
API_DESC = 'An API for serving models'
API_VERSION = '0.1'

# default model
MODEL_NAME = 'MODEL NAME'
DEFAULT_MODEL_PATH = 'assets/{}'.format(MODEL_NAME)
MODEL_LICENSE = 'MODEL LICENSE'

MODEL_META_DATA = {
    'id': '{} MODEL ID'.format(MODEL_NAME.lower()),
    'name': '{} MODEL NAME'.format(MODEL_NAME),
    'description': '{} MODEL DESCRIPTION'.format(MODEL_NAME),
    'type': 'TYPE',
    'license': '{}'.format(MODEL_LICENSE)
}

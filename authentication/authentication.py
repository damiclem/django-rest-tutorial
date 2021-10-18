# Import token authentication
from rest_framework.authentication import TokenAuthentication


# Extend token autentication in order to create Bearer authentication
class BearerAuthentication(TokenAuthentication):

    # Define keyword as Bearer
    keyword = 'Bearer'

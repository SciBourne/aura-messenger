from dataclasses import dataclass


@dataclass(frozen=True)
class AuthDocs:
    class POST:
        login = {
            "summary": "Authentication user",

            "description": (
                "Login with email + password "
                "in the absence of an access token"
            ),

            "status_code": 204,

            "responses": {
                204: {
                    "model": None,
                    "description": "Successful Response",
                },

                401: {
                    "model": None,
                    "description": "Unauthorized",
                },
            }
        }

        logout = {
            "summary": "Logout user",

            "description": (
                "Deleting all user access tokens"
            ),

            "status_code": 204,

            "responses": {
                204: {
                    "model": None,
                    "description": "Successful Response",
                }
            }
        }

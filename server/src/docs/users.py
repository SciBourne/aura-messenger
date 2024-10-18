from dataclasses import dataclass


@dataclass(frozen=True)
class UserDocs:
    class POST:
        user = {
            "summary": "Create new user",

            "description": (
                "Creating new user account with email + password"
            ),

            "status_code": 201,

            "responses": {
                201: {
                    "model": None,
                    "description": "Successful Response",
                }
            }
        }

    class GET:
        users = {
            "summary": "Get user list",

            "description": (
                "Get list of names of all registered users"
            ),

            "status_code": 200,

            "responses": {
                200: {
                    "model": None,
                    "description": "Successful Response",
                }
            }
        }

        user = {
            "summary": "Get user info",

            "description": (
                "Get public user info by only username "
                "or get full user info by access token"
            ),

            "status_code": 200,

            "responses": {
                200: {
                    "model": None,
                    "description": "Successful Response",
                },

                404: {
                    "model": None,
                    "description": "Not Found"
                }
            }
        }

    class PATCH:
        user = {
            "summary": "Update user info",

            "description": (
                "Update user info. Access is required"
            ),

            "status_code": 200,

            "responses": {
                200: {
                    "model": None,
                    "description": "Successful Response",
                },

                401: {
                    "model": None,
                    "description": "Unauthorized"
                },

                404: {
                    "model": None,
                    "description": "Not Found"
                }
            }
        }

    class DELETE:
        user = {
            "summary": "Delete user account",

            "description": (
                "Delete user account. Access is required"
            ),

            "status_code": 204,

            "responses": {
                204: {
                    "model": None,
                    "description": "Successful Response",
                },

                401: {
                    "model": None,
                    "description": "Unauthorized"
                },

                404: {
                    "model": None,
                    "description": "Not Found"
                }
            }
        }

from dataclasses import dataclass


@dataclass(frozen=True)
class MessageDocs:
    class POST:
        message = {
            "summary": "Create new message",

            "description": (
                "Create new message, when the interlocutor is offline"
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
        messages = {
            "summary": "Get messages",

            "description": (
                "Get the message history"
            ),

            "status_code": 200,

            "responses": {
                200: {
                    "model": None,
                    "description": "Successful Response",
                },

                401: {
                    "model": None,
                    "description": "Unauthorized",
                },

                404: {
                    "model": None,
                    "description": "Not Found",
                }
            }
        }

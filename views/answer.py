def generate_view(ts: str, channel_id: str):
    return {
        "type": "modal",
        "callback_id": "answer_call",
        "title": {"type": "plain_text", "text": "Answer Call"},
        "submit": {"type": "plain_text", "text": "Answer"},
        "blocks": [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": ":celeste-madelineph-normal05: Answer a call",
                    "emoji": True,
                },
            },
            {
                "type": "input",
                "block_id": "username",
                "element": {
                    "type": "plain_text_input",
                    "action_id": "username",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Madeline",
                    },
                },
                "label": {
                    "type": "plain_text",
                    "text": "Should I pretend to be someone else?",
                    "emoji": True,
                },
            },
            {
                "type": "input",
                "block_id": "emoji",
                "element": {
                    "type": "plain_text_input",
                    "action_id": "emoji",
                    "placeholder": {
                        "type": "plain_text",
                        "text": ":celeste-madeline-normal04:",
                    },
                },
                "label": {
                    "type": "plain_text",
                    "text": "What should I look like?",
                    "emoji": True,
                },
            },
            {
                "type": "input",
                "block_id": "message_input",
                "element": {
                    "type": "plain_text_input",
                    "multiline": True,
                    "action_id": "message_input",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Hi frens! :D",
                    },
                },
                "label": {"type": "plain_text", "text": "Call to make", "emoji": True},
            },
        ],
        "private_metadata": f"{ts};{channel_id}",
    }


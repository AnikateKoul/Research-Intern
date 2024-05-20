from guardrails.hub import ToxicLanguage
from guardrails import Guard

from services import plain_prompt

guard = Guard().use(
    ToxicLanguage, threshold=0.5, validation_method="sentence", on_fail="exception"
)

# guard1 = Guard().use_many()


def ai_model(input_text):
    ai_output = plain_prompt.get_response(user_input=input_text)
    return ai_output


def ai_model_with_guardrails(input_text):
    try:
        guard.validate(
            input_text
        )
    except Exception as e:
        return str(e)

    try:
        guard.validate(ai_model(input_text))
    except Exception as e:
        return str(e)



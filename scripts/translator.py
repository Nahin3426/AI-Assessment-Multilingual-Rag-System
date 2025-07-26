from deep_translator import GoogleTranslator

def bn_to_en(text: str) -> str:
    try:
        return GoogleTranslator(source='bn', target='en').translate(text)
    except Exception as e:
        print(f"Translation error (bn->en): {e}")
        return text

def en_to_bn(text: str) -> str:
    try:
        return GoogleTranslator(source='en', target='bn').translate(text)
    except Exception as e:
        print(f"Translation error (en->bn): {e}")
        return text

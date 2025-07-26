from googletrans import Translator
import time

def load_text_chunks(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read().split('\n\n')  # assuming chunks are split by double newline

def save_translated_chunks(chunks, out_path):
    with open(out_path, 'w', encoding='utf-8') as f:
        for chunk in chunks:
            f.write(chunk + '\n\n')

def translate_chunks(chunks):
    translator = Translator()
    translated = []

    for i, chunk in enumerate(chunks, 1):
        print(f"🌐 Translating chunk {i}/{len(chunks)}...")
        try:
            result = translator.translate(chunk, src='bn', dest='en')
            translated.append(result.text)
        except Exception as e:
            print(f"❌ Error on chunk {i}: {e}")
            translated.append("[Translation Failed]")
        time.sleep(2)  # avoid being blocked

    return translated

if __name__ == "__main__":
    INPUT_PATH = "../data/ocr_extracted_text.txt"
    OUTPUT_PATH = "../data/translated_text.txt"

    chunks = load_text_chunks(INPUT_PATH)
    translated_chunks = translate_chunks(chunks)
    save_translated_chunks(translated_chunks, OUTPUT_PATH)
    print("✅ Translation complete and saved.")


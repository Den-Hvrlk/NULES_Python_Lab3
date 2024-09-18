from translator.googletrans import TransLate, LangDetect, LanguageList, CodeLang

if __name__ == "__main__":
    print(TransLate("Would you like a coffee?", "de"))
    print(CodeLang("da"))
    detected, confidence = LangDetect("Möchten Sie einen Kaffee?")
    print(f"Detected lang: {CodeLang(detected)} in probability {confidence}")
    print(LanguageList("Як там у Курську?"))
    print("Запис у файл...")
    LanguageList("Повітряна тривога", "file")
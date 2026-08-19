import os

def load_threat_documents(knowledge_base_dir):
    documents = []
    
    if not os.path.exists(knowledge_base_dir):
        return documents

    for file_name in os.listdir(knowledge_base_dir):
        file_path = os.path.join(knowledge_base_dir, file_name)
        
        # TXT Dosyalarını Okuma
        if file_name.endswith(".txt"):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    text = f.read()
                    if text.strip():
                        documents.append({"text": text, "source": file_name})
            except Exception as e:
                print(f"[Hata]: {file_name} okunamadı: {e}")

        # PDF Dosyalarını Okuma (Varsa)
        elif file_name.endswith(".pdf"):
            try:
                from pypdf import PdfReader
                reader = PdfReader(file_path)
                text = ""
                for page in reader.pages:
                    extracted = page.extract_text()
                    if extracted:
                        text += extracted + "\n"
                if text.strip():
                    documents.append({"text": text, "source": file_name})
            except Exception as e:
                print(f"[Hata]: {file_name} PDF okunamadı: {e}")

    return documents
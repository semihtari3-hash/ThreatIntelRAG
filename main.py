import os
from threat_intel_core.config import KNOWLEDGE_BASE_DIR, DEFAULT_CHUNK_SIZE, DEFAULT_OVERLAP, DEFAULT_TOP_K
from threat_intel_core.main_pipeline import run_threat_ingest, run_threat_rag

def main():
    if not os.path.exists(KNOWLEDGE_BASE_DIR) or not os.listdir(KNOWLEDGE_BASE_DIR):
        print("[Sistem]: threat_knowledge_base klasörü boş! Lütfen analiz edilecek tehdit raporu ekleyin.")
        return

    print("[Sistem]: Siber tehdit istihbarat dökümanları işleniyor ve vektör veritabanı güncelleniyor...")
    count = run_threat_ingest(chunk_size=DEFAULT_CHUNK_SIZE, overlap=DEFAULT_OVERLAP)
    print(f"[Sistem]: Toplam {count} metin parçası veritabanına başarıyla yüklendi.")
    print("[Sistem]: Tehdit bilgi bankası hazır. Sorgularınızı girebilirsiniz.\n")
    
    history = []

    while True:
        query = input("Tehdit Sorgusu Girin (çıkmak için çıkış yazın): ").strip()
        
        if not query:
            continue
            
        if query.lower() in ["çıkış", "exit", "quit"]:
            print("\nGüvenli çıkış yapılıyor. İyi çalışmalar!")
            break
            
        print("\nVeritabanı taranıyor ve tehdit analizi motoru tetikleniyor...\n")
        
        stream = run_threat_rag(
            query=query,
            history=history,
            chunk_size=DEFAULT_CHUNK_SIZE,
            overlap=DEFAULT_OVERLAP,
            top_k=DEFAULT_TOP_K,
            model_name="ThreatIntel-Phi4",
            temperature=0.2
        )
        
        printed_chars = 0
        full_response = ""
        
        for val in stream:
            if val[1]:
                current_response = val[1][-1]["content"]
                full_response = current_response
                new_text = current_response[printed_chars:]
                print(new_text, end="", flush=True)
                printed_chars = len(current_response)
        
        print("\n" + "-"*60 + "\n")
        
        history.append({"role": "user", "content": query})
        history.append({"role": "assistant", "content": full_response})

if __name__ == "__main__":
    main()
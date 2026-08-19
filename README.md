#  ThreatIntelRAG - Siber Tehdit İstihbaratı ve Ağ Analizi RAG Sistemi

**ThreatIntelRAG**, yerel siber tehdit istihbaratı raporlarını, ağ analiz dökümanlarını ve MITRE ATT&CK eşleştirmelerini semantik (anlamsal) olarak indeksleyen ve kullanıcı sorgularına nokta atışı analiz raporları üreten bir **Retrieval-Augmented Generation (RAG)** motorudur.

---

##  Temel Özellikler

* **Semantik Arama:** `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` çok dilli vektör modeli ile Türkçe tehdit istihbaratını anlamsal olarak analiz eder.
* **Kalıcı Vektör Belleği:** ChromaDB persistent storage mimarisi ile dökümanları yüksek hızda vektörleştirip önbelleğe alır.
* **Akıllı Cümle/Paragraf Süzgeci:** Gelen bağlam (context) içinden kural, filtre ve tehdit tanımlarını cımbızlayarak kullanıcıya doğrudan nokta atışı bulgular sunar.
* **Geniş Format Desteği:** `.txt` ve `.pdf` formatındaki tehdit bilgi bankalarını otomatik işler.

---

##  Proje Mimarisi

```text
ThreatIntelRAG/
├── threat_knowledge_base/       # Analiz edilecek tehdit dökümanları (.txt, .pdf)
│   └── siber_tehdit.txt
├── threat_intel_core/           # RAG Çekirdek Modülleri
│   ├── config.py                # Konfigürasyon ve parametreler
│   ├── threat_loader.py         # Döküman okuyucu
│   ├── threat_chunker.py        # Metin parçalayıcı (Chunking)
│   ├── threat_embeddings.py     # Vektörleştirme motoru
│   ├── threat_vector_db.py      # ChromaDB kalıcı indeksleme
│   ├── threat_search.py         # Semantik sorgu motoru
│   ├── foundry_llm.py           # Akıllı yanıt ve süzgeç simülasyonu
│   └── main_pipeline.py         # Uçtan uca RAG boru hattı
├── main.py                      # İnteraktif CLI terminal arayüzü
├── requirements.txt             # Bağımlılıklar
└── README.md                    # Proje dökümantasyonu

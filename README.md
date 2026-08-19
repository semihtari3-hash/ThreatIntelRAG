# ThreatIntelRAG - Siber Tehdit İstihbaratı ve Ağ Analizi RAG Sistemi

ThreatIntelRAG; yerel siber tehdit istihbaratı raporlarını, ağ analiz dokümanlarını ve MITRE ATT&CK eşleştirmelerini semantik olarak indeksleyen ve sorgulara bağlamsal analiz çıktıları üreten bir Retrieval-Augmented Generation (RAG) motorudur.

## Temel Özellikler

* **Semantik Arama:** `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` çok dilli vektör modeli ile tehdit istihbaratı verilerini anlamsal olarak analiz eder.
* **Kalıcı Vektör Belleği:** ChromaDB persistent storage mimarisi ile dokümanları yerel veritabanında saklar ve sorgu eşleşmelerini optimize eder.
* **Hibrit Tehdit Sınıflandırması:** Tespit edilen tehditleri MITRE ATT&CK teknikleri, Snort/YARA kuralları ve ağ analiz imzaları ile ilişkilendirir.
* **Yerel ve Güvenli:** Tüm embedding ve vektör benzerlik hesaplamaları yerel donanımda çalışır, dış API bağımlılığı gerektirmez.

## Mimari ve Veri Akışı

1. **Veri Toplama (Ingestion):** `threat_knowledge_base` dizinindeki teknik tehdit raporları ve IOC verileri taranır.
2. **Parçalama ve Vektörleştirme (Chunking & Embedding):** Dokümanlar semantik parçalara bölünerek çok dilli transformatör modeli ile 384 boyutlu vektörlere dönüştürülür.
3. **İndeksleme (Indexing):** Üretilen vektörler ChromaDB koleksiyonuna yerel olarak kaydedilir.
4. **Sorgu ve Geri Çağırma (Retrieval):** Kullanıcı sorgusu vektör uzayında taranarak en yüksek benzerlik skoruna sahip tehdit desenleri listelenir.

## Kurulum

Projeyi yerel ortamınızda çalıştırmak için aşağıdaki adımları izleyin:

```bash
# Depoyu klonlayın
git clone [https://github.com/semihtari3-hash/ThreatIntelRAG.git](https://github.com/semihtari3-hash/ThreatIntelRAG.git)

# Proje dizinine geçin
cd ThreatIntelRAG

# Gerekli bağımlılıkları yükleyin
pip install -r requirements.txt

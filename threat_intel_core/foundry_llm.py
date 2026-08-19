import time

def process_threat_query_stream(context_text, query, temperature, model_name):
    time.sleep(0.1)
    
    if not context_text or not context_text.strip():
        yield f"[Model: {model_name}] Tehdit veritabanında bu sorguya dair bir eşleşme bulunamadı."
        return

    ignore_words = {"nedir", "nelerdir", "nasıl", "hangi", "için", "veya", "ve", "kullanılır", "gerçekleşir", "nerede", "ise", "yapar"}
    keywords = [
        w.lower() for w in query.replace("?", "").replace("'", " ").replace('"', " ").split() 
        if len(w) > 2 and w.lower() not in ignore_words
    ]
    
    # Noktalı kodların bölünmesini önlemek için sadece ". " (nokta + boşluk) veya "\n" ile bölüyoruz
    raw_segments = context_text.replace("\n", ". ").split(". ")
    
    relevant_bullets = []
    
    for segment in raw_segments:
        clean_seg = segment.strip()
        if len(clean_seg) < 10:
            continue
            
        seg_lower = clean_seg.lower()
        
        if any(kw in seg_lower for kw in keywords):
            if clean_seg not in relevant_bullets:
                relevant_bullets.append(clean_seg)

    if relevant_bullets:
        response_text = f"[Model: {model_name}] Tehdit Analiz Raporu (Nokta Atışı Bulgular):\n\n"
        for bullet in relevant_bullets:
            # Eğer cümlenin sonunda nokta yoksa ekle
            bullet_clean = bullet if bullet.endswith(".") else bullet + "."
            response_text += f"• {bullet_clean}\n\n"
    else:
        response_text = f"[Model: {model_name}] Tehdit Analiz Raporu:\n\n{context_text.strip()[:300]}..."

    words = response_text.split(" ")
    for word in words:
        yield word + " "
        time.sleep(0.005)
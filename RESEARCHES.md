# **Ağ Trafiği Analizinin Temelleri: PCAP, IDS ve Protokol Analizi**

## **1\. Ağ Trafiği Analizine ve PCAP Dosyalarına Giriş**

Ağ Trafiği Analizi (NTA), bir ağ üzerinden geçen veri paketlerini yakalayarak, inceleyerek ve analiz ederek güvenlik tehditlerini, performans sorunlarını ve operasyonel anormallikleri tespit etme sürecidir. Modern siber güvenlik savunmasının temel taşlarından biridir. Analizin en temel birimi, genellikle .pcap uzantısıyla bilinen **paket yakalama (packet capture)** dosyasıdır. PCAP dosyaları, bir güvenlik ihlali sonrasında saldırganın ağ içinde nasıl hareket ettiğini, hangi sistemlerle iletişim kurduğunu ve hangi zafiyetleri kullandığını anlamak için en güvenilir kanıt kaynağıdır.

## **2\. Ağ Analizinin Temel Araçları**

Etkili bir ağ analizi için çeşitli araçlar birlikte kullanılır:

* **Wireshark/TShark:** Ağ paketlerini en ince detayına kadar incelemek için kullanılan bir endüstri standardıdır. TShark, bu aracın komut satırı versiyonudur ve otomasyon için idealdir.  
* **Suricata (IDS/IPS):** Ağ trafiğini, bilinen tehditleri tanımlayan kural setleriyle karşılaştırarak **uyarı (alert)** üreten bir Saldırı Tespit Sistemi'dir.  
* **Zeek (Eski adıyla Bro):** Trafiği sadece kurallarla karşılaştırmak yerine, onu "anlamlandırır" ve conn.log (bağlantı logu), dns.log (DNS sorguları) gibi yüksek seviyeli, yapılandırılmış loglar üretir.

## **3\. Güvenlik Odaklı Protokol Analizi**

Saldırganlar, amaçlarına ulaşmak için genellikle standart ağ protokollerini kötüye kullanırlar. Bu projede özellikle şu protokollere odaklanılmıştır:

* **DNS (Domain Name System):** Kötü amaçlı yazılımların Komuta-Kontrol (C2) sunucularıyla iletişim kurmak için kullandığı kritik bir protokoldür.  
* **HTTP/HTTPS:** Web trafiği, kimlik avı (phishing) ve zararlı yazılım indirme gibi birçok tehdidin giriş kapısıdır.  
* **SMB (Server Message Block):** Ağ içinde yatay olarak yayılmak isteyen solucanlar ve fidye yazılımları tarafından sıklıkla hedef alınır.

## **Sonuç**

Ağ trafiği analizi, reaktif bir olay müdahale sürecinden proaktif bir tehdit avcılığına geçişin anahtarıdır. Bu proje, PCAP dosyalarındaki ham veriyi; Wireshark, Suricata ve Zeek gibi araçlarla işleyerek anlamlı, eyleme geçirilebilir güvenlik istihbaratına dönüştürmeyi hedefler.
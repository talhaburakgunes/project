Bu proje, **Talha** tarafından geliştirilmiş olup, ağ trafiği kayıtlarını (.pcap) Wireshark, Zeek ve Suricata gibi endüstri standardı araçlarla analiz ederek şüpheli ağ etkinliklerini tespit etmeyi ve elde edilen bulguları modern ve etkileşimli bir HTML dashboard üzerinden görselleştirmeyi amaçlamaktadır.

## **🎯 Projenin Amacı**

Projenin temel amacı, ham ve karmaşık ağ verilerini, bir güvenlik analistinin kolayca yorumlayabileceği, eyleme geçirilebilir içgörülere dönüştürmektir. Bu araç sayesinde:

* **Tehdit Tespiti:** Ağdaki bilinen ve bilinmeyen tehditler, saldırı girişimleri ve anormal aktiviteler proaktif olarak belirlenir.  
* **Risk Analizi:** Saldırı tespit sistemi uyarılarına dayanarak en çok risk teşkil eden IP adresleri otomatik olarak skorlanır.  
* **Görselleştirme:** Karmaşık veriler, grafikler ve tablolar aracılığıyla anlaşılır hale getirilir, bu da karar verme süreçlerini hızlandırır.

## **✨ Özellikler**

* **Derinlemesine PCAP Analizi:** TShark kullanılarak ağ paketlerinden protokol bazında detaylı istatistikler çıkarılır.  
* **Saldırı Tespiti Entegrasyonu:** Suricata tarafından üretilen IDS/IPS uyarıları ayrıştırılarak bilinen tehditler anında tespit edilir.  
* **Yapısal Loglama:** Zeek ile ağ trafiği, bağlantı (connection), DNS ve HTTP gibi yüksek seviyeli, anlamlı loglara dönüştürülür.  
* **Otomatik Risk Skorlama:** IDS uyarılarının ciddiyet seviyesine göre kaynak IP adreslerine otomatik olarak bir risk puanı atanır.  
* **Etkileşimli Web Dashboard:** Tüm analiz sonuçları, Chart.js ile güçlendirilmiş, kullanıcı dostu bir web arayüzünde sunulur.

## **🛠️ Kullanılan Teknolojiler**

* **Veri Analizi:** Python 3.x  
* **Ağ Trafiği Yakalama ve Analiz:** Wireshark (TShark), Suricata, Zeek  
* **Web Geliştirme:** HTML5, CSS3, JavaScript  
* **Görselleştirme Kütüphanesi:** Chart.js

## **🚀 Kurulum ve Kullanım**

Projenin nasıl kurulacağı ve çalıştırılacağı ile ilgili detaylı bilgi için [ROADMAP.MD](http://docs.google.com/ROADMAP.MD) dosyasına göz atın.

## **🖼️ Web Sayfası Görünümü**

Projenin web arayüzünün nasıl görüneceğine dair kavramsal örnekler aşağıdadır.
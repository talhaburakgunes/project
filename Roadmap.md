# **ROADMAP.MD: Ağ Güvenliği ve Trafik Analizi Aracı**

## **Proje Özeti**

Bu proje, ağ trafiği kayıtlarını (.pcap) Wireshark, Zeek ve Suricata gibi araçlarla analiz ederek şüpheli ağ etkinliklerini tespit etmeyi ve bir HTML dashboard üzerinden görselleştirmeyi amaçlar. Proje, **Talha** tarafından 3 gün içinde tamamlanacaktır.

Toplam Süre: 3 gün  
Geliştirici: Talha (Uçtan Uca Geliştirme)  
Yöntem: Tüm modüller geliştirilir, output klasöründe veriler birleştirilir ve Git ile versiyon kontrolü yapılır.

## **Görev ve Zaman Planı**

### **👤 Talha: Proje Lideri ve Geliştirici**

**Görev:** Ağ trafiği verilerini işlemek, tehditleri tespit etmek, risk analizi yapmak ve tüm sonuçları dinamik bir web dashboard'unda görselleştirmek.

### **Gün 1: Kurulum, Veri Toplama ve Temel Ayrıştırma**

**Hedef:** Proje altyapısını kurmak ve ilk analiz çıktılarını oluşturmak.

1. **Araç Kurulumu:** Python 3.x, Wireshark (TShark), Suricata ve Zeek kurulumlarını tamamla.  
2. **Veri Toplama:** Analiz için örnek bir .pcap dosyası indir.  
3. **Log Üretimi:** İndirilen .pcap dosyasını **Zeek** ve **Suricata** ile işleyerek conn.log ve eve.json loglarını üret.  
4. **IDS Ayrıştırıcısı (suricata\_alert\_parser.py):** eve.json dosyasındaki "alert" olaylarını ayrıştırıp output/alerts.json olarak kaydedecek script'i geliştir.

### **Gün 2: Derinlemesine Analiz ve Risk Mantığı**

**Hedef:** Ham verileri anlamlı risk metriklerine ve raporlara dönüştürmek.

1. **Protokol Analizi (pcap\_parser.py):** TShark kullanarak .pcap dosyasından protokol istatistiklerini çıkarıp output/protocol\_stats.json dosyasına kaydeden script'i geliştir.  
2. **Risk Skorlama (ip\_risk\_scorer.py):** output/alerts.json dosyasını okuyarak kaynak IP'ler için bir risk skoru hesaplayan ve sonuçları output/risk\_report.json olarak kaydeden script'i geliştir.  
3. **Dashboard Altyapısı (web/):** index.html, style.css ve server.bat dosyalarını oluşturarak dashboard'un temel görsel iskeletini tasarla.

### **Gün 3: Görselleştirme, Entegrasyon ve Projeyi Tamamlama**

**Hedef:** Tüm analiz sonuçlarını kullanıcı dostu bir arayüzde birleştirmek ve projeyi sonlandırmak.

1. **Dinamik Dashboard Geliştirme (report.js):** protocol\_stats.json, alerts.json ve risk\_report.json dosyalarını dinamik olarak yükleyip Chart.js ile grafikler, tablolar ve zaman çizelgeleri oluşturan script'i geliştir.  
2. **Kod Kalitesi ve Dokümantasyon:** Tüm scriptlere ve kodlara açıklayıcı yorum satırları ekle. README.MD dosyasını detaylandır.  
3. **Final Test ve Commit:** Tüm sistemin uçtan uca hatasız çalıştığını test et ve projeyi main branch'ine commit'le.

## **Kurulum ve Çalıştırma**

1. **Gereksinimler:** Python 3.x, Wireshark (TShark), Suricata, Zeek.  
2. **Klonlama ve Bağımlılıklar:**  
   git clone https://github.com/talhaburakgunes/project.git  
   cd Network-Security-Analyzer  
   pip install \-r requirements.txt

3. **Analizi Çalıştırma:** (Scriptler adım adım çalıştırılacak)  
   \# 1\. Zeek & Suricata ile log üret  
   zeek \-r \<path\_to.pcap\>  
   suricata \-r \<path\_to.pcap\> \-l ./output/

   \# 2\. Python scriptleri ile JSON'ları oluştur  
   python scripts/suricata\_alert\_parser.py  
   python scripts/pcap\_parser.py   
   python scripts/ip\_risk\_scorer.py

4. **Dashboard Görüntüleme:**  
   \# Windows için  
   web\\server.bat  
   \# Linux/macOS için  
   python3 \-m http.server 8000 \--directory web

   * Tarayıcıda aç: http://localhost:8000/
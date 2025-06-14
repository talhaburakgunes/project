## **WEB SAYFASI GÖRÜNÜMÜ (Ağ Güvenliği Analizi Konsepti)**

Bu ekran görüntüleri, projemin web tabanlı raporlama arayüzünün nasıl görünebileceğini temsil etmektedir. Geliştirici **Talha** tarafından hayata geçirilecek olan bu dashboard, ağ analizi sonuçlarını etkileşimli bir şekilde sunmayı hedefler.

Konsept 1: Ana Dashboard \- Genel Bakış. Bu panel, analiz edilen PCAP dosyasının genel bir özetini sunar. Solda protokol dağılımını gösteren bir grafik, sağda ise en çok uyarı üreten IP adresleri ve genel risk skoru yer alır.

Konsept 2: Uyarılar ve Zaman Çizelgesi. Bu bölümde, Suricata gibi bir IDS tarafından tespit edilen güvenlik uyarıları, oluş zamanlarına göre sıralanır. Her bir uyarı, tehdit türünü, ciddiyetini ve ilgili IP adreslerini gösterir.

Konsept 3: Ağ Akışları. Zeek'in conn.log dosyasından elde edilen verilerle oluşturulmuş, ağdaki tüm bağlantıların bir listesi. Hangi IP'nin hangi IP ile hangi port üzerinden ne kadar süre konuştuğu gibi detaylar yer alır.

Konsept 4: Detaylı Analiz. Belirli bir uyarıya veya IP adresine tıklandığında, o varlıkla ilgili tüm ilişkili olayları, logları ve detayları gösteren derinlemesine bir analiz ekranı.
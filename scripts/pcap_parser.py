# ==============================================================================
# Dosya: scripts/pcap_parser.py
# Geliştirici: Talha
# Amaç: TShark (Wireshark CLI) kullanarak bir .pcap dosyasını ayrıştırır
# ve ağ trafiği hakkında temel protokol istatistikleri çıkarır.
# ==============================================================================
import subprocess
import json
from collections import Counter

def analyze_pcap_with_tshark(pcap_file_path, output_json_path):
    """
    TShark kullanarak PCAP dosyasını analiz eder ve tüm paketleri JSON formatında kaydeder.
    """
    # TShark komutu: PCAP'i JSON formatında ayrıştır
    command = ['tshark', '-r', pcap_file_path, '-T', 'json']
    
    print(f"'{' '.join(command)}' komutu çalıştırılıyor...")
    
    try:
        with open(output_json_path, 'w', encoding='utf-8') as f:
            # TShark komutunu çalıştır ve çıktısını doğrudan dosyaya yaz
            subprocess.run(command, stdout=f, stderr=subprocess.PIPE, text=True, check=True)
        
        print(f"Analiz tamamlandı. Çıktı '{output_json_path}' dosyasına kaydedildi.")
        return True
    except FileNotFoundError:
        print("Hata: 'tshark' komutu bulunamadı. Lütfen Wireshark'ın kurulu ve PATH'e ekli olduğundan emin olun.")
        return False
    except subprocess.CalledProcessError as e:
        print(f"TShark çalışırken hata oluştu: {e.stderr}")
        return False

# Bu script ana işlevi olarak TShark'ı çalıştırır.
# İstatistik çıkarma gibi ek işlemler bu temel üzerine inşa edilebilir
# veya ayrı bir script'te bu JSON çıktısı kullanılabilir.

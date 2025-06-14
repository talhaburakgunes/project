# ==============================================================================
# Dosya: scripts/suricata_alert_parser.py
# Geliştirici: Talha
# Amaç: Suricata IDS tarafından üretilen eve.json log dosyasını okur
# ve içindeki güvenlik uyarılarını (alerts) temiz bir formata getirir.
# ==============================================================================
import json
from typing import List, Dict

def parse_suricata_log(log_file_path: str) -> List[Dict]:
    """Suricata eve.json log dosyasını satır satır okur ve sadece 'alert' olaylarını ayrıştırır."""
    alerts = []
    try:
        with open(log_file_path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    log_entry = json.loads(line)
                    # Sadece 'alert' tipindeki olayları işle
                    if log_entry.get('event_type') == 'alert':
                        alert_info = {
                            "timestamp": log_entry.get('timestamp'),
                            "src_ip": log_entry.get('src_ip'),
                            "src_port": log_entry.get('src_port'),
                            "dest_ip": log_entry.get('dest_ip'),
                            "dest_port": log_entry.get('dest_port'),
                            "protocol": log_entry.get('proto'),
                            "signature": log_entry.get('alert', {}).get('signature'),
                            "category": log_entry.get('alert', {}).get('category'),
                            "severity": log_entry.get('alert', {}).get('severity')
                        }
                        alerts.append(alert_info)
                except json.JSONDecodeError:
                    continue # Satır geçerli bir JSON değilse atla
    except FileNotFoundError:
        print(f"Hata: Suricata log dosyası bulunamadı -> {log_file_path}")
    return alerts

def save_alerts_to_json(alerts: List[Dict], output_file: str):
    """Ayrıştırılan uyarıları bir JSON dosyasına kaydeder."""
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(alerts, f, indent=4)
    print(f"Toplam {len(alerts)} adet uyarı '{output_file}' dosyasına kaydedildi.")

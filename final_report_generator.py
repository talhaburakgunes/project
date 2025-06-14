# ==============================================================================
# Dosya: scripts/final_report_generator.py
# Geliştirici: Talha
# Amaç: Projenin farklı adımlarından gelen tüm analiz çıktılarını
# tek bir nihai JSON raporunda birleştirir.
# ==============================================================================
import json
from datetime import datetime

def generate_final_report(alerts_path, ip_risk_path, output_file="final_analysis_report.json"):
    """Tüm analiz sonuçlarını okur ve birleşik bir JSON raporu oluşturur."""
    
    report = {
        "report_generated_by": "Talha",
        "report_timestamp": datetime.now().isoformat(),
        "system": "Ağ Güvenliği Analiz Raporu",
        "summary": {}
    }

    # 1. Ayrıştırılmış Uyarıları Oku ve Raporla
    try:
        with open(alerts_path, 'r', encoding='utf-8') as f:
            alerts_data = json.load(f)
            report["detected_alerts"] = alerts_data
            report["summary"]["total_alerts"] = len(alerts_data)
    except (FileNotFoundError, json.JSONDecodeError):
        report["detected_alerts"] = []
        report["summary"]["total_alerts"] = 0

    # 2. IP Risk Skorlarını Oku ve Raporla
    try:
        with open(ip_risk_path, 'r', encoding='utf-8') as f:
            ip_risk_data = json.load(f)
            report["ip_risk_analysis"] = ip_risk_data
            report["summary"]["high_risk_ip_count"] = len([ip for ip, score in ip_risk_data.items() if score > 50])
    except (FileNotFoundError, json.JSONDecodeError):
        report["ip_risk_analysis"] = {}
        report["summary"]["high_risk_ip_count"] = 0

    # Raporu dosyaya yaz
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4, ensure_ascii=False)

    print(f"\n📄 Nihai analiz raporu '{output_file}' olarak başarıyla oluşturuldu.")

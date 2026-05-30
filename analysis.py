"""
Phân tích điểm kiểm tra của học sinh
"""

import statistics
from typing import List, Dict
from datetime import datetime

# Dữ liệu điểm kiểm tra mẫu (thang điểm 100)
test_scores = {
    "Toán": [85, 92, 78, 95, 88, 76, 90, 82, 94, 87],
    "Văn": [88, 85, 90, 82, 86, 91, 84, 89, 87, 83],
    "Tiếng Anh": [92, 88, 85, 90, 87, 93, 86, 91, 89, 84],
    "Lý": [78, 82, 85, 80, 88, 76, 84, 81, 86, 79],
    "Hóa": [90, 87, 92, 85, 89, 91, 88, 86, 93, 84]
}


def analyze_subject(subject: str, scores: List[float]) -> Dict:
    """Phân tích điểm của một môn học"""
    return {
        "môn_học": subject,
        "số_học_sinh": len(scores),
        "điểm_trung_bình": round(statistics.mean(scores), 2),
        "điểm_cao_nhất": max(scores),
        "điểm_thấp_nhất": min(scores),
        "điểm_trung_vị": statistics.median(scores),
        "độ_lệch_chuẩn": round(statistics.stdev(scores), 2)
    }


def classify_score(score: float) -> str:
    """Phân loại điểm số"""
    if score >= 90:
        return "Xuất sắc"
    elif score >= 80:
        return "Giỏi"
    elif score >= 70:
        return "Khá"
    elif score >= 60:
        return "Trung bình"
    else:
        return "Yếu"


def export_to_file(all_analyses: List[Dict], best_subject: Dict,
                   worst_subject: Dict, classification_count: Dict,
                   overall_average: float, filename: str = "analysis_results.txt"):
    """Xuất kết quả phân tích ra file text"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filename, 'w', encoding='utf-8') as f:
        f.write("=" * 60 + "\n")
        f.write("PHÂN TÍCH ĐIỂM KIỂM TRA HỌC SINH\n")
        f.write(f"Thời gian: {timestamp}\n")
        f.write("=" * 60 + "\n\n")

        # Phân tích từng môn học
        for analysis in all_analyses:
            f.write(f"📚 Môn: {analysis['môn_học']}\n")
            f.write(f"   Số học sinh: {analysis['số_học_sinh']}\n")
            f.write(f"   Điểm trung bình: {analysis['điểm_trung_bình']}\n")
            f.write(f"   Điểm cao nhất: {analysis['điểm_cao_nhất']}\n")
            f.write(f"   Điểm thấp nhất: {analysis['điểm_thấp_nhất']}\n")
            f.write(f"   Điểm trung vị: {analysis['điểm_trung_vị']}\n")
            f.write(f"   Độ lệch chuẩn: {analysis['độ_lệch_chuẩn']}\n\n")

        # Tổng kết
        f.write("=" * 60 + "\n")
        f.write("TỔNG KẾT\n")
        f.write("=" * 60 + "\n")
        f.write(f"✅ Môn có điểm TB cao nhất: {best_subject['môn_học']} ({best_subject['điểm_trung_bình']})\n")
        f.write(f"⚠️  Môn có điểm TB thấp nhất: {worst_subject['môn_học']} ({worst_subject['điểm_trung_bình']})\n\n")

        # Phân loại
        f.write("=" * 60 + "\n")
        f.write("PHÂN LOẠI ĐIỂM MÔN TOÁN\n")
        f.write("=" * 60 + "\n")
        for classification, count in sorted(classification_count.items(),
                                           key=lambda x: x[1], reverse=True):
            f.write(f"   {classification}: {count} học sinh\n")
        f.write("\n")

        # Điểm trung bình chung
        f.write(f"📊 Điểm trung bình chung tất cả các môn: {overall_average}\n")


def main():
    print("=" * 60)
    print("PHÂN TÍCH ĐIỂM KIỂM TRA HỌC SINH")
    print("=" * 60)
    print()

    # Phân tích từng môn học
    all_analyses = []
    for subject, scores in test_scores.items():
        analysis = analyze_subject(subject, scores)
        all_analyses.append(analysis)

        print(f"📚 Môn: {analysis['môn_học']}")
        print(f"   Số học sinh: {analysis['số_học_sinh']}")
        print(f"   Điểm trung bình: {analysis['điểm_trung_bình']}")
        print(f"   Điểm cao nhất: {analysis['điểm_cao_nhất']}")
        print(f"   Điểm thấp nhất: {analysis['điểm_thấp_nhất']}")
        print(f"   Điểm trung vị: {analysis['điểm_trung_vị']}")
        print(f"   Độ lệch chuẩn: {analysis['độ_lệch_chuẩn']}")
        print()

    # Tìm môn có điểm trung bình cao nhất và thấp nhất
    print("=" * 60)
    print("TỔNG KẾT")
    print("=" * 60)

    best_subject = max(all_analyses, key=lambda x: x['điểm_trung_bình'])
    worst_subject = min(all_analyses, key=lambda x: x['điểm_trung_bình'])

    print(f"✅ Môn có điểm TB cao nhất: {best_subject['môn_học']} ({best_subject['điểm_trung_bình']})")
    print(f"⚠️  Môn có điểm TB thấp nhất: {worst_subject['môn_học']} ({worst_subject['điểm_trung_bình']})")
    print()

    # Phân loại điểm số của môn Toán
    print("=" * 60)
    print("PHÂN LOẠI ĐIỂM MÔN TOÁN")
    print("=" * 60)

    classification_count = {}
    for score in test_scores["Toán"]:
        classification = classify_score(score)
        classification_count[classification] = classification_count.get(classification, 0) + 1

    for classification, count in sorted(classification_count.items(),
                                       key=lambda x: x[1], reverse=True):
        print(f"   {classification}: {count} học sinh")
    print()

    # Tính điểm trung bình chung của tất cả các môn
    all_scores = [score for scores in test_scores.values() for score in scores]
    overall_average = round(statistics.mean(all_scores), 2)
    print(f"📊 Điểm trung bình chung tất cả các môn: {overall_average}")
    print()

    # Xuất kết quả ra file
    export_to_file(all_analyses, best_subject, worst_subject,
                   classification_count, overall_average)
    print("=" * 60)
    print("✅ Đã xuất kết quả phân tích ra file: analysis_results.txt")
    print("=" * 60)


if __name__ == "__main__":
    main()

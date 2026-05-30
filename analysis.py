"""
Phân tích điểm kiểm tra của học sinh
"""

import statistics
from typing import List, Dict

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


if __name__ == "__main__":
    main()

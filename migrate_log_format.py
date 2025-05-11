import json

log_file = "fail_log.json"

def migrate_log_format():
    with open(log_file, 'r+') as f:
        data = json.load(f)
        logs = data.get("logs", [])
        total_count = data.get("total_count", 0)

        # 🔄 ลบ field 'status' ที่อยู่ในแต่ละ log (ถ้ามี)
        for log in logs:
            if "status" in log:
                del log["status"]

        # 🔃 เรียง log จากใหม่ไปเก่า
        logs.sort(key=lambda x: x["count"], reverse=True)

        # ✅ สร้างข้อมูลใหม่พร้อม status ด้านบน
        new_data = {
            "status": "no ok",  # ค่า default แสดงสถานะล่าสุด จะถูกอัปเดตใน runtime
            "total_count": total_count,
            "logs": logs
        }

        f.seek(0)
        json.dump(new_data, f, indent=2)
        f.truncate()

    print("Migration complete. Log updated.")

if __name__ == "__main__":
    migrate_log_format()
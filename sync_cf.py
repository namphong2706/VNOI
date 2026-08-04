import os
import requests

# Tên tài khoản Codeforces của bạn
CF_HANDLE = "namphong2706"

def sync_codeforces():
    url = f"https://codeforces.com/api/user.status?handle={CF_HANDLE}&from=1&count=50"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Không thể kết nối tới API Codeforces!")
        return

    data = response.json()
    if data.get("status") != "OK":
        print("Lỗi từ API Codeforces:", data.get("comment"))
        return

    os.makedirs("codeforces", exist_ok=True)
    submissions = data.get("result", [])

    for sub in submissions:
        # Trong API Codeforces, "OK" chính là Accepted (AC)
        if sub.get("verdict") == "OK":
            sub_id = sub.get("id")
            problem = sub.get("problem", {})
            contest_id = problem.get("contestId", "")
            index = problem.get("index", "")
            name = problem.get("name", "")
            lang = sub.get("programmingLanguage", "")

            # Tạo file lưu thông tin bài nộp vào thư mục /codeforces/
            filename = f"codeforces/{contest_id}{index}_{name}.txt"

            if not os.path.exists(filename):
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(f"// Bài: {contest_id}{index} - {name}\n")
                    f.write(f"// Ngôn ngữ: {lang}\n")
                    f.write(f"// Link nộp bài: https://codeforces.com/contest/{contest_id}/submission/{sub_id}\n")
                print(f"Đã lưu bài: {contest_id}{index} - {name}")

if __name__ == "__main__":
    sync_codeforces()

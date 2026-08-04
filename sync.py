import os
import requests

HANDLE = "namphong2706"  # Tên tài khoản Codeforces của bạn

def main():
    url = f"https://codeforces.com/api/user.status?handle={HANDLE}&from=1&count=50"
    res = requests.get(url).json()

    if res.get("status") == "OK":
        os.makedirs("codeforces", exist_ok=True)
        for sub in res.get("result", []):
            if sub.get("verdict") == "OK":
                prob = sub.get("problem", {})
                c_id = prob.get("contestId", "")
                idx = prob.get("index", "")
                name = prob.get("name", "")
                
                filename = f"codeforces/{c_id}{idx}_{name}.txt"
                if not os.path.exists(filename):
                    with open(filename, "w", encoding="utf-8") as f:
                        f.write(f"// Bài: {c_id}{idx} - {name}\n")
                        f.write(f"// Link: https://codeforces.com/contest/{c_id}/submission/{sub.get('id')}\n")
                    print("Đã lưu bài:", name)

if __name__ == "__main__":
    main()

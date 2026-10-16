# 模拟 SSH 登录日志
logs = [
    "Failed password for root from 192.0.2.10",
    "Accepted password for admin from 192.0.2.20",
    "Failed password for admin from 192.0.2.10",
    "Failed password for root from 192.0.2.30",
]

failed_count = 0

for log in logs:
    if "Failed password" in log:
        failed_count += 1

print(f"Failed login attempts: {failed_count}")
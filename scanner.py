import os

# 🔧 Configs
SUSPICIOUS_EXTENSIONS = ['.exe', '.bat', '.js', '.vbs']
KEYWORDS = ['password', 'secret', 'malware']
MAX_FILE_SIZE_MB = 10


def scan_directory(path):
    print(f"\n🔍 Scanning directory: {path}\n")

    for root, dirs, files in os.walk(path):
        for file in files:
            filepath = os.path.join(root, file)
            try:
                size_mb = os.path.getsize(filepath) / (1024 * 1024)
                _, ext = os.path.splitext(file)

                is_suspicious = False
                reasons = []

                # Check for suspicious extension
                if ext.lower() in SUSPICIOUS_EXTENSIONS:
                    is_suspicious = True
                    reasons.append(f"Extension '{ext}'")

                # Check for large file size
                if size_mb > MAX_FILE_SIZE_MB:
                    is_suspicious = True
                    reasons.append(f"Size: {size_mb:.2f}MB")

                # Check for keywords in filename
                for keyword in KEYWORDS:
                    if keyword.lower() in file.lower():
                        is_suspicious = True
                        reasons.append(f"Keyword: '{keyword}'")
                        break

                if is_suspicious:
                    print(f"⚠️ Suspicious File: {filepath}")
                    print(f"   👉 Reason(s): {', '.join(reasons)}\n")

            except Exception as e:
                print(f"❌ Error reading file {filepath}: {e}")


if __name__ == "__main__":
    path = input("📁 Enter folder path to scan: ")
    if os.path.exists(path):
        scan_directory(path)
    else:
        print("🚫 Path does not exist.")

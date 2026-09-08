import json, sys, os
BASE = "/home/user/NEXAPOCKET/collecte_cyber"
def main():
    target = sys.argv[1]
    payload = json.load(sys.stdin)
    path = os.path.join(BASE, target)
    seen = set()
    if os.path.exists(path):
        for line in open(path, encoding="utf-8"):
            line = line.strip()
            if line:
                try: seen.add(json.loads(line).get("URL","")+"|"+json.loads(line).get("PREUVE","")[:80])
                except Exception: pass
    n = 0
    with open(path, "a", encoding="utf-8") as f:
        for rec in payload:
            key = rec.get("URL","")+"|"+rec.get("PREUVE","")[:80]
            if key in seen: continue
            seen.add(key)
            f.write(json.dumps(rec, ensure_ascii=False)+"\n"); n += 1
    print(f"{target}: +{n} lignes (total {sum(1 for _ in open(path, encoding='utf-8'))})")
main()

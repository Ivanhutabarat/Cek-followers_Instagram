import json

try:
    # 1. Buka file following
    with open('following.json', 'r') as f:
        following_data = json.load(f)

    following = set()
    for item in following_data['relationships_following']:
        try:
            username = item.get('title') or item['string_list_data'][0]['href'].split('/')[-1]
            following.add(username)
        except Exception:
            continue

    # 2. Buka file followers
    with open('followers_1.json', 'r') as f:
        followers_data = json.load(f)

    followers = set()
    for item in followers_data:
        try:
            username = item['string_list_data'][0]['value']
            followers.add(username)
        except Exception:
            continue

    # 3. Cari yang tidak follback
    tidak_follback = following - followers

    # 4. Tampilkan hasil
    print(f"\nAda {len(tidak_follback)} akun yang tidak follback kamu. Berikut daftarnya:\n")
    for akun in sorted(tidak_follback):
        print(f"@{akun}")

except FileNotFoundError:
    print("Gagal! Pastikan kamu membuat file 'cek_follback.py' ini di SATU FOLDER YANG SAMA dengan 'following.json' dan 'followers_1.json'")

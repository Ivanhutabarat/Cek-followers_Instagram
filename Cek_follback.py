import json

def cek_instagram():
    print("🔍 Memulai Pengecekan Data Instagram...\n")

    # ==========================================
    # 1. CEK AKUN YANG TIDAK FOLLBACK
    # ==========================================
    try:
        with open('following.json', 'r') as f:
            following_data = json.load(f)
        
        following = set()
        for item in following_data['relationships_following']:
            try:
                username = item.get('title') or item['string_list_data'][0]['href'].split('/')[-1]
                following.add(username)
            except Exception:
                continue

        with open('followers_1.json', 'r') as f:
            followers_data = json.load(f)
            
        followers = set()
        for item in followers_data:
            try:
                username = item['string_list_data'][0]['value']
                followers.add(username)
            except Exception:
                continue

        tidak_follback = following - followers
        print(f"❌ Ada {len(tidak_follback)} akun yang kamu follow tapi TIDAK FOLLBACK:")
        print("-" * 40)
        for akun in sorted(tidak_follback):
            print(f"   @{akun}")
        print("-" * 40 + "\n")

    except FileNotFoundError:
        print("⚠️ Gagal mengecek follback: File 'following.json' atau 'followers_1.json' tidak ditemukan.\n")

    # ==========================================
    # 2. CEK PERMINTAAN FOLLOW YANG PENDING
    # ==========================================
    try:
        with open('pending_follow_requests.json', 'r') as f:
            pending_data = json.load(f)
            
        pending_requests = []
        for item in pending_data['relationships_follow_requests_sent']:
            try:
                username = item['string_list_data'][0]['value']
                pending_requests.append(username)
            except Exception:
                continue

        print(f"⏳ Ada {len(pending_requests)} permintaan follow kamu yang BELUM DI-ACC (Pending):")
        print("-" * 40)
        for akun in pending_requests:
            print(f"   @{akun}")
        print("-" * 40 + "\n")

    except FileNotFoundError:
        print("⚠️ Gagal mengecek pending request: File 'pending_follow_requests.json' tidak ditemukan.\n")
    except KeyError:
        print("✔️ Tidak ada permintaan follow yang pending saat ini.\n")

    print("✅ Pengecekan Selesai!")

if __name__ == "__main__":
    cek_instagram()

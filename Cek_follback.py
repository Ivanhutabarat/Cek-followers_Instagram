import json
import os

def cek_instagram():
    print("🔍 Memulai Pengecekan Data Instagram...\n")

    # Ini adalah kunci rahasianya: Mendeteksi lokasi folder secara otomatis
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    file_following = os.path.join(base_dir, 'following.json')
    file_followers = os.path.join(base_dir, 'followers_1.json')
    file_pending = os.path.join(base_dir, 'pending_follow_requests.json')

    # ==========================================
    # 1. CEK AKUN YANG TIDAK FOLLBACK
    # ==========================================
    try:
        with open(file_following, 'r', encoding='utf-8') as f:
            following_data = json.load(f)
        
        following = set()
        for item in following_data['relationships_following']:
            try:
                username = item.get('title') or item['string_list_data'][0]['href'].split('/')[-1]
                following.add(username)
            except Exception:
                continue

        with open(file_followers, 'r', encoding='utf-8') as f:
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
        print(f"⚠️ Gagal mengecek follback: File 'following.json' atau 'followers_1.json' tidak ditemukan di folder:\n{base_dir}\n")

    # ==========================================
    # 2. CEK PERMINTAAN FOLLOW YANG PENDING
    # ==========================================
    try:
        with open(file_pending, 'r', encoding='utf-8') as f:
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
        print(f"⚠️ Gagal mengecek pending request: File 'pending_follow_requests.json' tidak ditemukan di folder:\n{base_dir}\n")
    except KeyError:
        print("✔️ Tidak ada permintaan follow yang pending saat ini.\n")

    print("✅ Pengecekan Selesai!")

if __name__ == "__main__":
    cek_instagram()

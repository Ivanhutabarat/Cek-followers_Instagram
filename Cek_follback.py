import json
import os
import glob

def cari_file_terbaru(base_dir, nama_asli):
    """Fitur Auto-Update: Mencari file versi angka berapapun dan mengambil yang PALING BARU"""
    # Menghilangkan '.json' untuk mencari nama dasarnya (misal: 'followers_1')
    nama_dasar = nama_asli.replace('.json', '')
    
    # Mencari semua file yang namanya mirip (followers_1.json, followers_1 (2).json, dst)
    pola_pencarian = os.path.join(base_dir, f"{nama_dasar}*.json")
    daftar_file = glob.glob(pola_pencarian)
    
    if daftar_file:
        # Mengurutkan file berdasarkan waktu download/modifikasi yang paling baru
        daftar_file.sort(key=os.path.getmtime, reverse=True)
        return daftar_file[0] # Selalu ambil file urutan pertama (paling terbaru)
        
    # Kalau tidak ada file yang cocok sama sekali, kembalikan nama aslinya untuk memicu error handling
    return os.path.join(base_dir, nama_asli)

def ekstrak_akun(file_path, key_utama):
    """Fungsi pintar untuk mengekstrak username dari berbagai format JSON Instagram"""
    if not os.path.exists(file_path):
        return None 
        
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        hasil = set()
        
        if isinstance(data, dict):
            items = data.get(key_utama, [])
            if not items and 'followers_1' in file_path and data:
                items = list(data.values())[0]
        else:
            items = data

        for item in items:
            try:
                username = item.get('title')
                if not username and 'string_list_data' in item:
                    username = item['string_list_data'][0].get('value')
                if not username and 'string_list_data' in item: 
                    href = item['string_list_data'][0].get('href', '')
                    username = href.strip('/').split('/')[-1]
                
                if username:
                    hasil.add(username)
            except Exception:
                continue
                
        return sorted(list(hasil))
    except Exception:
        return None

def cetak_hasil(judul, data_list, ikon="✅"):
    """Fungsi untuk mencetak hasil ke layar dengan rapi"""
    if data_list is None:
        print(f"⚠️ {judul} dilewati (File tidak ditemukan).")
    elif len(data_list) == 0:
        print(f"{ikon} {judul} (0 akun)")
    else:
        print(f"{ikon} {judul} ({len(data_list)} akun):")
        print("-" * 40)
        for akun in data_list:
            print(f"   @{akun}")
        print("-" * 40)
    print("")

def cek_instagram_ultimate():
    print("=" * 50)
    print("🚀 INSTAGRAM SUPER CHECKER MULAI MEMINDAI...")
    print("=" * 50 + "\n")

    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 1. Ekstrak Semua Data (Sekarang otomatis mencari file paling baru, angka (2), (3), dst tidak masalah!)
    following = ekstrak_akun(cari_file_terbaru(base_dir, 'following.json'), 'relationships_following')
    followers = ekstrak_akun(cari_file_terbaru(base_dir, 'followers_1.json'), '') 
    pending = ekstrak_akun(cari_file_terbaru(base_dir, 'pending_follow_requests.json'), 'relationships_follow_requests_sent')
    blocked = ekstrak_akun(cari_file_terbaru(base_dir, 'blocked_profiles.json'), 'relationships_blocked_users')
    cf = ekstrak_akun(cari_file_terbaru(base_dir, 'close_friends.json'), 'relationships_close_friends')
    hide_story = ekstrak_akun(cari_file_terbaru(base_dir, 'hide_story_from.json'), 'relationships_hide_stories_from')
    recent_req = ekstrak_akun(cari_file_terbaru(base_dir, 'recent_follow_requests.json'), 'relationships_permanent_follow_requests')
    unfollowed = ekstrak_akun(cari_file_terbaru(base_dir, 'recently_unfollowed_profiles.json'), 'relationships_unfollowed_users')

    # 2. Proses Logika & Cetak Hasil
    if following is not None and followers is not None:
        tidak_follback = sorted(list(set(following) - set(followers)))
        cetak_hasil("AKUN YANG TIDAK FOLLBACK KAMU", tidak_follback, "❌")
    else:
        print("⚠️ Cek Follback dilewati (File following/followers_1 tidak lengkap).\n")

    cetak_hasil("PERMINTAAN FOLLOW MENGGANTUNG (PENDING)", pending, "⏳")
    cetak_hasil("AKUN YANG KAMU BLOKIR", blocked, "🚫")
    cetak_hasil("DAFTAR CLOSE FRIENDS (CF) KAMU", cf, "🟢")
    cetak_hasil("AKUN YANG DI-SEMBUNYIKAN DARI STORY KAMU", hide_story, "👻")
    cetak_hasil("PERMINTAAN FOLLOW TERBARU KE KAMU", recent_req, "📥")
    cetak_hasil("AKUN YANG BARU SAJA KAMU UNFOLLOW", unfollowed, "👋")

    print("=" * 50)
    print("✨ PEMINDAIAN SELESAI ✨")
    print("=" * 50)

if __name__ == "__main__":
    cek_instagram_ultimate()

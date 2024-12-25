import psutil
import subprocess
import time

# Danh sách các tiến trình cần kill
tienTrinh = ['flood', 'tlskill', 'bypass', 'tlskill']

# Hàm kiểm tra tình trạng sử dụng RAM
def check_ram_usage(ram_threshold=95):
    # Lấy thông tin sử dụng RAM
    ram_usage = psutil.virtual_memory().percent  # Lấy mức sử dụng RAM

    print(f"RAM Usage: {ram_usage}%")

    # Kiểm tra nếu vượt ngưỡng
    if ram_usage > ram_threshold:
        return True
    return False

# Hàm thực hiện lệnh pkill với -9 -f (kill mạnh mẽ)
def kill_processes():
    for process_name in tienTrinh:
        print(f"Đang kill tiến trình: {process_name} với pkill -9 -f")
        try:
            # Sử dụng pkill với -9 -f để kill các tiến trình
            subprocess.run(['pkill', '-9', '-f', process_name], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Lỗi khi kill tiến trình {process_name}: {e}")

# Hàm chính để theo dõi hệ thống và thực thi pkill khi cần
def monitor_system():
    while True:
        if check_ram_usage():
            print("Cảnh báo: RAM sử dụng vượt quá 95%. Đang thực hiện lệnh pkill...")
            kill_processes()
        else:
            print("Tài nguyên hệ thống ổn định.")
        
        # Đợi 1 giây trước khi kiểm tra lại
        time.sleep(1)

if __name__ == "__main__":
    monitor_system()

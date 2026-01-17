import tkinter as tk
from tkinter import ttk
import winsound
import random
class CoolGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("c00lgui Reborn RcT by v3rx")
        self.root.geometry("320x600")
        self.root.configure(bg='black')
        self.root.resizable(False, False)
        
        # Tạo style cho các nút
        style = ttk.Style()
        style.configure('TButton', 
                       foreground='red', 
                       background='black',
                       font=('Arial', 8, 'bold'),
                       padding=2)
        
        # Tạo các frame chính
        self.create_server_destruction_frame()
        self.create_commands_frame()
        self.create_btool_frame()
        self.create_settings_frame()
        
    def create_server_destruction_frame(self):
        frame = ttk.LabelFrame(self.root, text="Server Destruction", style='TFrame')
        frame.pack(fill="x", padx=5, pady=2)
        
        # Hàng 1
        row1 = ttk.Frame(frame)
        row1.pack(fill="x", pady=1)
        
        ttk.Button(row1, text="Crash Server", command=lambda: self.button_click("Crash Server"), width=15).pack(side="left", padx=1)
        ttk.Button(row1, text="Lag Server", command=lambda: self.button_click("Lag Server"), width=15).pack(side="left", padx=1)
        
        # Hàng 2
        row2 = ttk.Frame(frame)
        row2.pack(fill="x", pady=1)
        
        ttk.Button(row2, text="Kick All Players", command=lambda: self.button_click("Kick All Players"), width=15).pack(side="left", padx=1)
        ttk.Button(row2, text="Ban All Players", command=lambda: self.button_click("Ban All Players"), width=15).pack(side="left", padx=1)
        
        # Hàng 3
        row3 = ttk.Frame(frame)
        row3.pack(fill="x", pady=1)
        
        ttk.Button(row3, text="Delete All Data", command=lambda: self.button_click("Delete All Data"), width=15).pack(side="left", padx=1)
        ttk.Button(row3, text="Server Lock", command=lambda: self.button_click("Server Lock"), width=15).pack(side="left", padx=1)
        
        # Hàng 4
        row4 = ttk.Frame(frame)
        row4.pack(fill="x", pady=1)
        
        ttk.Button(row4, text="Shutdown Server", command=lambda: self.button_click("Shutdown Server"), width=15).pack(side="left", padx=1)
        ttk.Button(row4, text="Destroy Server", command=lambda: self.button_click("Destroy Server"), width=15).pack(side="left", padx=1)
    
    def create_commands_frame(self):
        frame = ttk.LabelFrame(self.root, text="Infinite Commands/Gm", style='TFrame')
        frame.pack(fill="x", padx=5, pady=2)
        
        # Hàng 1
        row1 = ttk.Frame(frame)
        row1.pack(fill="x", pady=1)
        
        ttk.Button(row1, text="Fly", command=lambda: self.button_click("Fly"), width=15).pack(side="left", padx=1)
        ttk.Button(row1, text="Speed Hack", command=lambda: self.button_click("Speed Hack"), width=15).pack(side="left", padx=1)
        
        # Hàng 2
        row2 = ttk.Frame(frame)
        row2.pack(fill="x", pady=1)
        
        ttk.Button(row2, text="No Clip", command=lambda: self.button_click("No Clip"), width=15).pack(side="left", padx=1)
        ttk.Button(row2, text="God Mode", command=lambda: self.button_click("God Mode"), width=15).pack(side="left", padx=1)
        
        # Hàng 3
        row3 = ttk.Frame(frame)
        row3.pack(fill="x", pady=1)
        
        ttk.Button(row3, text="Infinite Jump", command=lambda: self.button_click("Infinite Jump"), width=15).pack(side="left", padx=1)
        ttk.Button(row3, text="Teleport To Me", command=lambda: self.button_click("Teleport To Me"), width=15).pack(side="left", padx=1)
        
        # Hàng 4
        row4 = ttk.Frame(frame)
        row4.pack(fill="x", pady=1)
        
        ttk.Button(row4, text="Teleport To Player", command=lambda: self.button_click("Teleport To Player"), width=15).pack(side="left", padx=1)
        ttk.Button(row4, text="Teleport To Base", command=lambda: self.button_click("Teleport To Base"), width=15).pack(side="left", padx=1)
        
        # Hàng 5
        row5 = ttk.Frame(frame)
        row5.pack(fill="x", pady=1)
        
        ttk.Button(row5, text="Teleport To Spawn", command=lambda: self.button_click("Teleport To Spawn"), width=23).pack(side="left", padx=1)
        ttk.Button(row5, text="ESP", command=lambda: self.button_click("ESP"), width=8).pack(side="left", padx=1)
    
    def create_btool_frame(self):
        frame = ttk.LabelFrame(self.root, text="Broken/Btool ID", style='TFrame')
        frame.pack(fill="x", padx=5, pady=2)
        
        # Hàng 1 - Ô nhập ID
        entry_frame = ttk.Frame(frame)
        entry_frame.pack(fill="x", pady=2)
        
        ttk.Label(entry_frame, text="ID:", foreground='red', background='black').pack(side="left", padx=2)
        self.btool_entry = ttk.Entry(entry_frame, width=30)
        self.btool_entry.pack(side="left", padx=2, fill="x", expand=True)
        
        # Hàng 2 - Nút bấm
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(fill="x", pady=2)
        
        ttk.Button(btn_frame, text="Execute", command=self.execute_btool, width=15).pack(side="left", padx=1)
        ttk.Button(btn_frame, text="Clear", command=self.clear_btool, width=15).pack(side="left", padx=1)
        
        # Hàng 3 - Ô kết quả
        self.result_text = tk.Text(frame, height=4, width=30, bg='black', fg='red', font=('Arial', 8))
        self.result_text.pack(fill="x", padx=2, pady=2)
        self.result_text.insert('1.0', 'Result will be shown here...')
        self.result_text.config(state='disabled')
    
    def create_settings_frame(self):
        frame = ttk.LabelFrame(self.root, text="Settings", style='TFrame')
        frame.pack(fill="x", padx=5, pady=2)
        
        # Checkbox
        self.var_sound = tk.BooleanVar(value=True)
        self.var_autoclose = tk.BooleanVar(value=False)
        
        # Hàng 1 - Checkbox
        chk_frame1 = ttk.Frame(frame)
        chk_frame1.pack(fill="x", pady=1)
        
        ttk.Checkbutton(chk_frame1, text="Enable Sound", variable=self.var_sound, style='TCheckbutton').pack(side="left", padx=5)
        ttk.Checkbutton(chk_frame1, text="Auto Close", variable=self.var_autoclose, style='TCheckbutton').pack(side="left", padx=5)
        
        # Hàng 2 - Nút bấm
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(fill="x", pady=5)
        
        ttk.Button(btn_frame, text="Save Settings", command=self.save_settings, width=15).pack(side="left", padx=1)
        ttk.Button(btn_frame, text="Exit", command=self.root.quit, width=15).pack(side="left", padx=1)
    
    def execute_btool(self):
        btool_id = self.btool_entry.get()
        if btool_id:
            self.show_result(f"Executing BTool ID: {btool_id}")
            self.button_click(f"Execute BTool: {btool_id}")
        else:
            self.show_result("Error: Please enter a valid ID")
    
    def clear_btool(self):
        self.btool_entry.delete(0, 'end')
        self.show_result("Cleared")
        self.button_click("Cleared BTool ID")
    
    def show_result(self, message):
        self.result_text.config(state='normal')
        self.result_text.delete('1.0', 'end')
        self.result_text.insert('1.0', message)
        self.result_text.config(state='disabled')
    
    def save_settings(self):
        settings = {
            'sound': self.var_sound.get(),
            'autoclose': self.var_autoclose.get()
        }
        self.show_result("Settings saved!")
        self.button_click("Settings saved")
    
    def button_click(self, button_text):
        # Phát âm thanh khi bấm nút
        if self.var_sound.get():
            try:
                # Phát âm thanh hệ thống (beep)
                frequency = random.randint(500, 1000)  # Tần số ngẫu nhiên
                duration = 100  # Thời gian phát âm thanh (ms)
                winsound.Beep(frequency, duration)
            except:
                pass  # Bỏ qua nếu không thể phát âm thanh
        
        # In ra console khi bấm nút
        print(f"Button clicked: {button_text}")
        
        # Tự động đóng nếu autoclose được bật và nút Exit được nhấn
        if button_text == "Exit" and self.var_autoclose.get():
            self.root.after(1000, self.root.quit)
if __name__ == "__main__":
    root = tk.Tk()
    
    # Đặt màu nền đen cho tất cả các frame
    style = ttk.Style()
    style.theme_use('alt')  # Sử dụng theme 'alt' để dễ tùy chỉnh
    
    # Cấu hình style
    style.configure('TFrame', background='black')
    style.configure('TLabelframe', background='black', foreground='red')
    style.configure('TLabelframe.Label', background='black', foreground='red')
    style.configure('TLabel', background='black', foreground='red')
    style.configure('TCheckbutton', background='black', foreground='red')
    style.configure('TButton', 
                   foreground='red', 
                   background='black',
                   font=('Arial', 8, 'bold'),
                   padding=2)
    
    app = CoolGUI(root)
    root.mainloop()

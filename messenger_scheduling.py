from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import time
import config as conf
import pickle
import tkinter as tk

class AUTO_SEND_MESSENGE:
    def __init__(self):
        self.driver = Chrome()
        self.scheduler = BlockingScheduler()

    def create_waiting_button(self):
        def on_continue():
            print("用戶已完成操作，繼續執行...")
            root.destroy()  # 關閉 GUI 窗口
        # 創建 GUI 窗口
        root = tk.Tk()
        root.title("操作提示")
        label = tk.Label(root, text="請手動完成操作，然後點擊 '繼續'")
        label.pack(pady=20)
        continue_button = tk.Button(root, text="繼續", command=on_continue)
        continue_button.pack(pady=10)
        root.mainloop()  # 開始 GUI 循環
    
    def save_cookies(self):
        self.driver.get(conf.fb_normal_url)
        self.create_waiting_button()
            
        pickle.dump(self.driver.get_cookies(), open(conf.cookie_path, "wb"))
        self.driver.close()

    def open_messenger(self):
        self.driver.get(conf.fb_normal_url)

        # 加載保存的 cookies
        cookies = pickle.load(open(conf.cookie_path, "rb"))
        for cookie in cookies:
            self.driver.add_cookie(cookie)

        self.driver.get(conf.friend_url)

        # 切到messenger介面時，會要求同步訊息的驗證。因需要手機驗證碼，可能只能手動操作。
        self.create_waiting_button()
    

    def send_facebook_messenge(self):
        message_box = self.driver.find_element(By.XPATH, "//div[@role='textbox']")

        # 發送訊息
        message_box.send_keys(conf.message)
        message_box.send_keys(Keys.RETURN)

        # 暫停幾秒鐘，以確保訊息發送成功
        time.sleep(10)

        # 任務完成後關閉調度器
        self.scheduler.shutdown(wait=False)

    def main(self):
        if conf.cookie_status == "dump":
            self.save_cookies()
        else:
            self.open_messenger()

            # 使用 schedule 模組在指定時間調用發送函數
            self.scheduler.add_job(self.send_facebook_messenge, 'date', run_date=conf.send_time)
            self.scheduler.start()
            self.driver.close()


if __name__ == '__main__':
    test = AUTO_SEND_MESSENGE()
    test.main()
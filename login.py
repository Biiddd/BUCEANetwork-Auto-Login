# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass
from selenium import webdriver
from selenium.webdriver.common.by import By
import yagmail
import socket
import ipaddress

def login_and_send_email():
    username = username_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    email_password = email_password_entry.get()

    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)

    print("IP: ", IPAddr)
    netwowrk = ipaddress.ip_network("10.100.0.0/18")

    current_ip = ipaddress.ip_address(IPAddr)

    if current_ip in netwowrk:
        print("校园网有线连接中")

        driver = webdriver.Chrome()
        driver.get("http://10.1.1.131/")
        print("打开登录界面")

        time.sleep(2)
        try:
            driver.find_element(By.CLASS_NAME, "btn-logout")
            print("校园网已登录")
            driver.quit()
        except:
            username_input = driver.find_element(By.ID, "username")
            username_input.send_keys(username)

            password_input = driver.find_element(By.ID, "password")
            password_input.send_keys(password)
            print("账号密码填充完成")

            login_key = driver.find_element(By.CLASS_NAME, "btn-login")

            login_key.click()
            print("登录完成")

            time.sleep(2)

            used_flow = (driver.find_element(By.ID, "used-flow")).text
            print("读取流量完成")
            rest_pocket = (driver.find_element(By.ID, "balance")).text
            print("读取余额完成")
            user_rest_pocket_widget = tk.Text(root)
            user_rest_pocket_widget.pack()
            user_rest_pocket_widget.delete("1.0", tk.END)
            user_rest_pocket_widget.insert(tk.END, rest_pocket)

            time.sleep(2)

            # 连接服务器
            print("邮件发送中")
            yag_server = yagmail.SMTP(user=email, password=email_password, host='smtp.qq.com')

            # 发送对象列表
            email_to = [email, ]
            email_title = '校园网自动登陆成功'
            email_content = "账户余额：{}元, 已使用流量：{}, IP：{}".format(rest_pocket, used_flow, IPAddr)

            # 发送邮件
            yag_server.send(email_to, email_title, email_content)

            print("邮件发送完成")
            print("执行完成")
            driver.quit()
    else:
        print("不在校园网中")
        yag_server = yagmail.SMTP(user=email, password=email_password, host='smtp.qq.com')

        # 发送对象列表
        email_to = [email, ]
        email_title = '脚本执行完成，未在校园网中'
        email_content = "当前IP：{}".format(IPAddr)

        # 发送邮件
        yag_server.send(email_to, email_title, email_content)

        print("邮件发送完成")
        print("执行完成")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_login(email, password):
    try:
        
        driver = webdriver.Chrome()
        driver.get("http://localhost:5227/identity/Account/Login")
        
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.NAME, "Input.Email")))

        email_field = driver.find_element(By.NAME, "Input.Email")
        email_field.send_keys(email)

        password_field = driver.find_element(By.NAME, "Input.Password")
        password_field.send_keys(password)

        submit_button = driver.find_element(By.XPATH, '//button[@id="login-submit"]')
        submit_button.click()

        success_notification = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/main/div[1]/div[1]/h2'))
        )
        print(f"Percobaan berhasil untuk registrasi dengan email {email}")

        logout_button = driver.find_element(By.ID, "logout")
        logout_button.click()
        print("Logout berhasil:", email)

        return True
    except Exception as e:
        print("Login gagal:", email)
        print(f"Percobaan gagal untuk login dengan email {email}")
        return False
    finally:
        driver.quit()

users_to_test = [
    {"email": "john.doe@example.com", "password": "P@ssword123"},
    {"email": "jane.smith@example.com", "password": "Password456"},
]

start_time = time.time()

for user in users_to_test:
    user["success"] = test_login(user["email"], user["password"])

end_time = time.time()

duration = end_time - start_time
print("Durasi pengujian:", f"{int(duration // 3600)} jam, {int((duration % 3600) // 60)} menit, {int(duration % 60)} detik")

total_success = sum(user["success"] for user in users_to_test)
total_failure = len(users_to_test) - total_success

print("Total login berhasil:", total_success)
print("Total login gagal:", total_failure)
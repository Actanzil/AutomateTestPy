from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_registration(firstname, lastname, email, password, confirmpassword):
    try:

        driver = webdriver.Chrome()
        driver.get("http://localhost:5227/identity/Account/Register")

        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.NAME, "Input.FirstName")))

        first_name_field = driver.find_element(By.NAME, "Input.FirstName")
        first_name_field.send_keys(firstname)
        time.sleep(1)

        last_name_field = driver.find_element(By.NAME, "Input.LastName")
        last_name_field.send_keys(lastname)
        time.sleep(1)

        email_field = driver.find_element(By.NAME, "Input.Email")
        email_field.send_keys(email)
        time.sleep(1)

        password_field = driver.find_element(By.NAME, "Input.Password")
        password_field.send_keys(password)
        time.sleep(1)

        confirm_password_field = driver.find_element(By.NAME, "Input.ConfirmPassword")
        confirm_password_field.send_keys(confirmpassword)
        time.sleep(1)

        submit_button = driver.find_element(By.XPATH, '//*[@id="registerSubmit"]')
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
        print("Percobaan gagal:", email)
        print(f"Percobaan gagal untuk registrasi dengan email {email}")
        return False
    finally:
        driver.quit()

users_to_test = [
    {"firstname": "John", "lastname": "Doe", "email": "john.doe@example.com", "password": "P@ssword123", "confirmpassword": "P@ssword123"},
    {"firstname": "Jane", "lastname": "Smith", "email": "jane.smith@example.com", "password": "P@ssword456", "confirmpassword": "P@ssword456"},
]

start_time = time.time()

for user in users_to_test:
    user["success"] = test_registration(user["firstname"], user["lastname"], user["email"], user["password"], user["confirmpassword"])

end_time = time.time()
duration = end_time - start_time
print("Durasi pengujian:", f"{int(duration // 3600)} jam, {int((duration % 3600) // 60)} menit, {int(duration % 60)} detik")

total_success = sum(user["success"] for user in users_to_test)
total_failure = len(users_to_test) - total_success

print("Total percobaan berhasil:", total_success)
print("Total percobaan gagal:", total_failure)

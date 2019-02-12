from selenium import webdriver
import config
browser = webdriver.Chrome()
browser.get("https://github.com")

signin_link = browser.find_element_by_link_text("Sign in")
signin_link.click()

username_box = browser.find_element_by_id("login_field")
username_box.send_keys("keenwilson")
password_box = browser.find_element_by_id("password")
password_box.send_keys(config.password)
password_box.submit()

assert "keenwilson" in browser.page_source

profile_link = browser.find_element_by_class_name("user-profile-link")
link_label = profile_link.get_attribute("innerHTML")

assert "keenwilson" in link_label

browser.quit()
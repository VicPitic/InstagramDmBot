import instaloader
from instapy import InstaPy
from selenium import webdriver
import time
import multiprocessing
import random

L = instaloader.Instaloader()

other_accounts = [
    "1st",
    "2nd",
]

other_passwords = [
    "1st",
    "2nd",
]


PATH = "chromedriver.exe"

#driver = webdriver.Chrome(PATH)

# Login or load session
username = other_accounts[0]
password = other_passwords[0]

L.login(user=username, passwd=password)  # (login)

# Obtain profile metadata
profile = instaloader.Profile.from_username(L.context, "hiphopcrewro")

# Print list of followees

follow_list = []


def GetFollowers():
    count = 0
    for followee in profile.get_followers():
        try:
            follow_list.append(followee.username)
            file = open("prada_followers.txt", "a+")
            file.write(follow_list[count])
            file.write("\n")
            file.close()
            print(follow_list[count])
            count = count + 1
        except:
            print("Got all the accounts")
            break

GetFollowers()

print("Got all the accounts")

def RunAccount(name, password):

    driver = webdriver.Chrome()

    driver.get("https://instagram.com")

    time.sleep(2)

    try:
        driver.find_element_by_xpath("/html/body/div[2]/div/div/button[1]").click()
        time.sleep(2)
    except:
        pass

    username_input = driver.find_element_by_xpath(
        "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
    password_input = driver.find_element_by_xpath(
        "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")

    username_input.send_keys(name)
    password_input.send_keys(password)

    login_button = driver.find_element_by_xpath(
        "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button")
    login_button.click()

    time.sleep(3.5)

    count = 0

    while (count <= 500):
        driver.get("https://www.instagram.com/direct/inbox/")

        time.sleep(4)

        try:
            driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[3]/button[1]").click()
        except:
            pass

        time.sleep(2)

        compose_button = driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button")
        compose_button.click()

        time.sleep(1)

        follower_input = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input")
        follower_input.send_keys(str(follow_list[random.randrange(0, len(follow_list))]))

        time.sleep(1.5)

        follower_name_button = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div[2]/div[1]/div")
        follower_name_button.click()



        next_button = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/div/button/div")
        next_button.click()

        time.sleep(5)

        message_input_field = driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
        message_input_field.send_keys("Boost your sales!!! Hey there my name is Jasmine an executive at Sales Booster and was wanting to spread the message of this new ecommerce platform that can boost your sales by up to 300% compared to shopify. I would highly recommend checking it out and making the change to boost your sales Here’s the link https://www.onefunnelaway.com/challenge?cf_affiliate_id=3114647&affiliate_id=3114647")

        time.sleep(0.5)

        try:
            notification_button = driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[1]")
            notification_button.click()
            notification_button = True
        except:
            pass

        time.sleep(2.5)

        send_button = driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]")
        send_button.click()

        print(f"Stored {follow_list[random.randrange(0, len(follow_list))]}")
        count = count + 1

        time.sleep(3)

if __name__ == "__main__":
    i = 0

    while i < len(other_accounts):
        p = multiprocessing.Process(target=RunAccount, args=(other_accounts[i], other_passwords[i]))
        p.start()
        i += 1

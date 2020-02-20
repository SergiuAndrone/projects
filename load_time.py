#!usr/bin/env python3

from selenium import webdriver
import getpass
import time

driver = webdriver.Firefox()
driver.set_page_load_timeout(30)


def create_log_file():
    with open(f'/Users/{getpass.getuser()}/Desktop/test_results.txt', 'w') as f:
        f.write('THE RESULTS OF THE TEST ARE: \n\n\n')


def write_in_file(text):
    with open(f'/Users/{getpass.getuser()}/Desktop/test_results.txt', 'a') as f:
        f.write(text)


page1 = "https://www.amazon.com/"
page2 = "https://cnn.com/"
page3 = "https://hbogo.ro/"
page4 = "https://www.euronews.com/"
page5 = "https://www.youtube.com/"
page6 = "https://www.imdb.com/"
page7 = "https://www.facebook.com/"
page8 = "https://www.twitch.tv/"
page9 = "https://hotnews.ro/"
page10 = "https://medium.com/"
page11 = "https://emag.ro/"

pages = [page1, page2, page3, page4, page5, page6, page7, page8, page9, page10, page11]

create_log_file()

avg_list = []

for run in range(10):
    total_time = 0
    for page in pages:
        try:
            time_start = time.time()
            driver.get(page)
            time_end = time.time()
            #write_in_file(f"The load time for page {page} is: {time_end-time_start} seconds\n\n")
            total_time += (time_end - time_start)
        except:
            #write_in_file(f"The page {page} didn't load in 30 sec\n\n")
            total_time += 30

    average_loading_time = total_time / len(pages)
    avg_list.append(average_loading_time)

    write_in_file(f"RUN {run+1}: the average loading time for all pages is {average_loading_time}\n\n")
    time.sleep(5)

write_in_file(f"Total average is: {sum(avg_list)/len(avg_list)}\n\n")

driver.close()
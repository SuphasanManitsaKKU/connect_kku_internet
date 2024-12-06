import requests
import time
import random
check_list = [
    "https://www.google.com",
    "https://www.youtube.com",
    "https://www.facebook.com",
    "https://www.instagram.com",
    "https://www.linkedin.com",
    "https://www.github.com",
    "https://www.medium.com",
    "https://www.stackoverflow.com",
    "https://www.wikipedia.org",
    "https://www.apple.com",
    "https://www.microsoft.com",
    "https://www.spotify.com",
    "https://www.cnn.com",
    "https://www.bbc.com",
    "https://www.nytimes.com",
    "https://www.oracle.com",
    "https://www.ibm.com",
    "https://www.intel.com",
    "https://www.mozilla.org",
    "https://www.cloudflare.com",
    "https://www.paypal.com",
    "https://www.quora.com",
    "https://www.booking.com",
    "https://www.tiktok.com",
    "https://www.ebay.com",
    "https://www.pinterest.com",
    "https://www.shopify.com",
    "https://www.samsung.com",
    "https://www.huawei.com",
    "https://www.sony.com",
    "https://www.dell.com",
    "https://www.lenovo.com",
    "https://www.dropbox.com",
    "https://www.slack.com",
    "https://www.atlassian.com",
    "https://www.trello.com",
    "https://www.theguardian.com",
    "https://www.bloomberg.com",
    "https://www.target.com",
    "https://www.ikea.com",
    "https://www.nordstrom.com",
    "https://www.sephora.com",
    "https://www.abcnews.go.com",
    "https://www.usatoday.com",
    "https://www.vox.com",
    "https://www.npr.org",
    "https://www.ted.com",
    "https://www.khanacademy.org",
    "https://www.coursera.org",
    "https://www.udemy.com",
    "https://www.edx.org",
    "https://www.freecodecamp.org",
    "https://www.bitbucket.org",
    "https://www.digitalocean.com",
    "https://www.heroku.com",
    "https://www.wordpress.com",
    "https://www.wix.com",
    "https://www.zoho.com",
    "https://www.hubspot.com"
]


# response = requests.get("https://www.oracle.com", timeout=1)
# print(response.status_code)



while True:
    set_list = random.choice(check_list)
    try:
        response = requests.get(set_list, timeout=3)
        print(response.status_code)
    except requests.exceptions.ReadTimeout:
        print(set_list + ": Timeout")
        break
    time.sleep(1)

# def check_url_status(urls):
#     results = {}
#     for url in urls:
#         try:
#             response = requests.get(url, timeout=1)
#             if response.status_code == 200:
#                 results[url] = "Accessible"
#             else:
#                 results[url] = f"Error: {response.status_code}"
#         except requests.RequestException as e:
#             results[url] = f"Failed: {str(e)}"
#     return results

# # ตรวจสอบ URL ทั้งหมด
# results = check_url_status(check_list)

# # แสดงผลลัพธ์
# for url, status in results.items():
#     print(f"{url}: {status}")

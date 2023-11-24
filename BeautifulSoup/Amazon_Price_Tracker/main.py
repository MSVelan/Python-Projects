import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

productEndpoint = "https://www.amazon.in/Kobo-WTA12-Weight-Lifting-Grip/dp/B01MQOCQWX/ref=pd_ci_mcx_mh_mcx_views_0?pd_rd_w=DOVF2&content-id=amzn1.sym.cd312cd6-6969-4220-8ac7-6dc7c0447352&pf_rd_p=cd312cd6-6969-4220-8ac7-6dc7c0447352&pf_rd_r=GXC32CPBNBY8JHES8CKT&pd_rd_wg=SDazC&pd_rd_r=5e11e529-4fd1-4aac-bb81-3e829f46ed31&pd_rd_i=B01MQOCQWX&th=1"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language":"en-GB,en;q=0.9,en-US;q=0.8,ta;q=0.7",
    "Cookie":'session-id=260-5516442-2080838; ai_user=jzNPnZbnztcT4WeT35UtqH|2023-06-10T07:46:47.910Z; ubid-acbin=260-4706114-7069305; lc-acbin=en_IN; x-acbin=k8KHUVvsFVF6eX7YU6Au85vQx2ToOqmqo08olfjslbAqCnOPnIhcWo9Qd5WmSuh3; at-acbin=Atza|IwEBIBe-WUVuuB2-vuETLF9wHDYDPiL0L8Qs35NQh_HyWN3jYN0RJhI8bGNa7qLi2rwdyAd5CthyEWLNgjfE-Jdd8nz58CJsJ9mL27t3UqIGhHKbn7Lls3bS0PxC-mq1vyB-HQDpd2T-9KDCeOvI50taYBt28pHX5ihump8pAsYVL-tpEgfLJfyP81hvaSPn9qx5vGDQlwubnY7T605TLbz11DY6dFHJ1wXkI08kD6ky5ujrdGIomZo-v_iDzM5YTv9hYg4; sess-at-acbin="Z32YqNVJ8BMyFvc2nPqu6SFaralZzbJdLoj/0KVaEOg="; sst-acbin=Sst1|PQEGFzdsUcM4lnSARYnGiFjFCURNpPu9cDGCvsLtUFcWx4JyHYmmqFlQy_oVS1RdpE5h1maPJ1EVDe2iZgT-ChCJzidJs6hFTc5c34AmAIt7GyQwCZ2Yf8-3tLT7Xif9RR9HBMB_ZvAWJfSsfzQZmwIZc6b_lveflXKsc3CBg4Np5xdqzC-f0N2slZ2mqvx49s5tRIhpFCNblqjB-i1naqjg_Jb-OlaT3eRAC-GLGeHsRxyRYXOAZ2AMRJQ01CZjH8dfP7siG5dmXRSaoYHEj2bxNhBIwhFQuoNLvNmTOA1N1XY; session-id-time=2082787201l; i18n-prefs=INR; session-token=KQOOK3jqtUW+7DPvC7RCVeec47jznxHqFENCNX2ry/u2NlJ+M21ibw1+bO8j6tQ37MDCf1FzXLsbYr8wReXDMJcLmlt+8E3e8PBExQ1KRWW//teN0O5SuM5UxiEAaCI/Idk4qb/azcdDJB0fE6RgJio60LKZq+4SIw5bDUo33fUKe3rmu1ZJOM6iNvKeSPFnUSdwrXjiy6VODd4+cY/w8M0lbvf/9e/XMlolarkYKdKd6/7foPRJXGVjbVSX2XL7NtnY7ozKQwk=; csm-hit=tb:s-TFCDWYGFJD5NWYRPG89V|1687634733290&t:1687634734857&adb:adblk_yes',
    "Viewport-Width":"424",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Cache-Control": "no-cache"
}
response = requests.get(url=productEndpoint, headers=headers)
productWebsite = response.content

soup = BeautifulSoup(productWebsite, "lxml")
# print(soup)
price = int(soup.find(name="span", class_="a-price-whole").getText().rstrip("."))


productTitle = soup.find(name="span", id="productTitle").getText().strip()
# print(productTitle)
# print(price)

smtpObj = smtplib.SMTP("smtp.gmail.com",port=587)
smtpObj.ehlo()
smtpObj.starttls()

sender = "muthiahsivavelan2026@gmail.com"
receiver = "muthiahsvn@gmail.com"
message = f"Subject:Amazon Price Alert!\n\n{productTitle} is now ₹ {price}.\nBuy now: {productEndpoint}"

password = "udihcqqyafyzrwii"

smtpObj.login(user=sender,password=password)

if(price<527):
    try:
        smtpObj.sendmail(sender,receiver,message.encode('utf-8'))
        print("Successfully mailed")
    except Exception as e:
        print("Error unable to send mail")
        print(f"Caught {type(e)}: ", e)

smtpObj.close()
print("Program executed!")
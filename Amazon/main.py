from bs4 import BeautifulSoup
import requests
import lxml
import smtplib


Accept_Language = 'en-US,en;q=0.9'
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
URl = "https://www.amazon.com/MSI-Stealth-15M-Gaming-Laptop/dp/B091GGZT1S/ref=sr_1_2?content-id=amzn1.sym.714c697a-23b8-4778-b5e2-40f1f2c6de75%3Aamzn1.sym.714c697a-23b8-4778-b5e2-40f1f2c6de75&keywords=laptop&pd_rd_r=1608e6ca-46e6-4955-8a66-3deb22ae62dc&pd_rd_w=w2K85&pd_rd_wg=Ud39C&pf_rd_p=714c697a-23b8-4778-b5e2-40f1f2c6de75&pf_rd_r=SYBMYMRKG5SEPGKBYVRX&qid=1670144267&refinements=p_n_graphics_type_browse-bin%3A14292273011%2Cp_n_operating_system_browse-bin%3A23724785011%7C23724787011%7C23724789011%7C23724790011%7C23724797011%2Cp_n_feature_thirty-three_browse-bin%3A23720418011%7C23720421011%7C23720422011%2Cp_n_feature_seven_browse-bin%3A18107822011&s=pc&sr=1-2"

header = {'Accept-Language': Accept_Language, 'User-Agent': user_agent}

response = requests.get(URl, headers=header)
website = response.text

soup = BeautifulSoup(website, "html.parser")
price = soup.find('span', class_="a-offscreen").getText().split('$')[-1]
print(price)


title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 200

if price < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(#YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )
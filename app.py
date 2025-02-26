import pyqrcode
import png
link = "https://www.linkedin.com/in/ankush-prajapati-583ab3295/"
qr_code = pyqrcode.create(link)
qr_code.png("linkedin.png",scale=5)
from aip import AipOcr
import re

APP_ID="19146502"
API_KEY="tmsh4fG5nMxOyEzX5r6kdYEv"
SECRET_KEY="GQ7wR7rzPc3ESXMAKfds1FyY6ov1H3Gb"

client=AipOcr(APP_ID,API_KEY,SECRET_KEY)

with open(r"D:/images/3.jpg","rb") as f:
    image=f.read()

data=str(client.basicGeneral(image))
#.replace(" ","")

#pat=re.compile(r"{'words':'(.*?)'}")

#result=pat.findall(data)[0]

#print(result)
print(data)

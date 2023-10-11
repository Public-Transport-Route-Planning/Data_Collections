import requests
import csv
import pandas as pd

api_key = "AIzaSyCtmL7XR_iyRJ5nODJCZDUAco_wqs5BzCY"

# locations = [
#                 "คูคต สถานีรถไฟ สายสุขุมวิท",
#                 "สถานีแยก คปอ.",
#                 "สถานีพิพิธภัณฑ์กองทัพอากาศ",
#                 "สถานีโรงพยาบาลภูมิพล-อดุลยเดช",
#                 "สถานีสะพานใหม่",
#                 "สถานีสายหยุด",
#                 "สถานีพหลโยธิน 59",
#                 "หลังแตะบัตรไปเคหะฯ (ฝั่งใต้) 40 ถ. พหลโยธิน แขวงอนุสาวรีย์ เขตบางเขน กรุงเทพมหานคร 10220", #หลังแตะบัตรไปเคหะฯ (ฝั่งใต้) 40 ถ. พหลโยธิน แขวงอนุสาวรีย์ เขตบางเขน กรุงเทพมหานคร 10220
#                 "สถานีกรมทหารราบที่ 11",
#                 "สถานีบางบัว",
#                 "สถานีกรมป่าไม้",
#                 "สถานีมหาวิทยาลัยเกษตรศาสตร์",
#                 "สถานีเสนานิคม",
#                 "รถไฟฟ้าสายสีเขียวเหนือ สถานี N11 รัชโยธิน",
#                 "สถานีพหลโยธิน 24",
#                 "สถานีห้าแยกลาดพร้าว",
#                 "สถานีหมอชิต",
#                 "สถานีรถไฟใต้ดินสะพานควาย แขวงพญาไท เขตพญาไท กรุงเทพมหานคร 10400", #
#                 "สถานีรถไฟฟ้าอารีย์ แขวงสามเสนใน เขตพญาไท กรุงเทพมหานคร 10400",
#                 "สถานีรถรางเบาสนามเป้า",
#                 "สถานีอนุสาวรีย์ชัยสมรภูมิ",
#                 "สถานีรถไฟฟ้าพญาไท", #
#                 "สถานีราชเทวี",
#                 "สถานีรถไฟฟ้าสยาม แขวงปทุมวัน เขตปทุมวัน กรุงเทพมหานคร 10330",
#                 "สถานีรถไฟฟ้าชิดลม ถนน เพลินจิต แขวงลุมพินี เขตปทุมวัน กรุงเทพมหานคร 10330", #
#                 "สถานีเพลินจิต",
#                 "สถานีนานา",
#                 "สถานีรถไฟใต้ดินอโศก ถ. กำแพงเพชร ๗ แขวงบางกะปิ เขตห้วยขวาง กรุงเทพมหานคร 10310",
#                 "สถานีพร้อมพงษ์",
#                 "สถานีทองหล่อ",
#                 "สถานีเอกมัย",
#                 "สถานีพระโขนง",
#                 "สถานีรถไฟฟ้าอ่อนนุช",
#                 "Bang Chak, แขวงพระโขนงใต้ Khet Phra Khanong, Krung Thep Maha Nakhon 10260, Thailand",
#                 "สถานีปุณณวิถี",
#                 "บีทีเอสอุดมสุข เขตบางนา กรุงเทพมหานคร 10260",
#                 "สถานีบางนา",
#                 "แบริ่ง, เขตบางนา, แขวงบางนา,รถไฟฟ้าบีทีเอสสายสุขุมวิท (สีเขียวอ่อน), ถนนสุขุมวิท, 10260", #
#                 "สถานีสำโรง",
#                 "สถานีปู่เจ้า",
#                 "สถานีช้างเอราวัณ",
#                 "สถานีรถไฟโรงเรียนนายเรือ",
#                 "สถานีปากน้ำ",
#                 "BTS Srinagarindra, Tambon Pak Nam, Amphoe Mueang Samut Prakan, Chang Wat Samut Prakan 10270, Thailand", #
#                 "Phraek Sa, Tambon Pak Nam, Amphoe Mueang Samut Prakan, Chang Wat Samut Prakan 10270, Thailand",
#                 "สถานีรถไฟสายลวด",
#                 "เคหะฯ ตำบล ท้ายบ้านใหม่ อำเภอเมืองสมุทรปราการ สมุทรปราการ 10280",
# ]

# locations = [
#     "สถานีสนามกีฬาแห่งชาติ",
#     "สถานีรถไฟฟ้าสยาม แขวงปทุมวัน เขตปทุมวัน กรุงเทพมหานคร 10330",
#     "สถานีราชดำริ",
#     "สถานีรถไฟใต้ดินศาลาแดง ถนน สีลม แขวงสีลม เขตบางรัก กรุงเทพมหานคร 10500",
#     "สถานีช่องนนทรี",
#     "สถานีเซนต์หลุยส์",
#     "สถานีสุรศักดิ์",
#     "สถานีสะพานตากสิน",
#     "สถานีกรุงธนบุรี",
#     "สถานีวงเวียนใหญ่",
#     "สถานีโพธิ์นิมิตร",
#     "สถานีตลาดพลู",
#     "สถานีวุฒากาศ",
#     # "บางหว้า สถานีรถไฟ แขวงปากคลองภาษีเจริญ เขตภาษีเจริญ กรุงเทพมหานคร 10160" #
# ]

# locations = [
#                 "Krung Thonburi (Golden Line), Khwaeng Khlong Ton Sai, Khet Khlong San, Krung Thep Maha Nakhon 10600, Thailand",
#                 "เจริญนคร สถานีรถไฟ แขวงคลองต้นไทร เขตคลองสาน กรุงเทพมหานคร 10600 สายสีทอง",
#                 "คลองสาน สถานีรถไฟ สายสีทอง",
# ]

# purple
# locations = [
#     "สถานีรถไฟใต้ดินคลองบางไผ่",
#     "สถานีรถไฟใต้ดินตลาดบางใหญ่",
#     "สถานีรถไฟใต้ดินสามแยกบางใหญ่",
#     "สถานีรถไฟใต้ดินบางพลู",
#     "สถานีรถไฟใต้ดินบางรักใหญ่",
#     "สถานีรถไฟใต้ดินบางรักน้อย-ท่าอิฐ",
#     "สถานีรถไฟใต้ดินไทรม้า",
#     "สถานีรถไฟใต้ดินสะพานพระนั่งเกล้า",
#     "สถานีรถไฟใต้ดินแยกนนทบุรี 1",
#     "สถานีรถไฟใต้ดินบางกระสอ บางกระสอ อำเภอเมืองนนทบุรี นนทบุรี 11000",
#     "สถานีรถไฟใต้ดินศูนย์ราชการนนทบุรี",
#     "สถานี กระทรวงสาธารณสุข 218 ถ. ติวานนท์ ตำบลตลาดขวัญ อำเภอเมืองนนทบุรี นนทบุรี 11000",
#     "สถานีรถไฟใต้ดินแยกติวานนท์",
#     "สถานี วงศ์สว่าง แขวงวงศ์สว่าง เขตบางซื่อ กรุงเทพมหานคร 10800",
#     "สถานีรถไฟใต้ดินบางซ่อน",
#     "สถานีรถไฟใต้ดินเตาปูน",
# ]

# blue line mrt
locations = [
    "สถานีรถไฟใต้ดินท่าพระ",
    "สถานีรถไฟใต้ดินจรัญฯ 13",
    "สถานีรถไฟใต้ดินไฟฉาย ถนน จรัญสนิทวงศ์ แขวงบ้านช่างหล่อ เขตบางกอกน้อย กรุงเทพมหานคร 10700",
    "สถานีรถไฟใต้ดินบางขุนนนท์",
    "สถานีรถไฟใต้ดินบางยี่ขัน",
    "สถานีรถไฟใต้ดินสิรินธร",
    "สถานีรถไฟใต้ดินบางพลัด",
    "สถานีรถไฟใต้ดินบางอ้อ",
    "สถานีรถไฟใต้ดินบางโพ",
    "สถานีรถไฟใต้ดินเตาปูน",
    # "สถานีรถไฟใต้ดินบางซื่อ",
    # "สถานีรถไฟใต้ดิน กำแพงเพชร MRT",  ##
    "สถานีรถไฟใต้ดินสวนจตุจักร",
    "สถานีรถไฟใต้ดินพหลโยธิน",
    "สถานีรถไฟใต้ดิน ลาดพร้าว MRT",
    # "สถานีรถไฟใต้ดินรัชดาภิเษก",
    "สถานีรถไฟใต้ดินสุทธิสาร",
    # "สถานีรถไฟใต้ดินห้วยขวาง",
    "สถานีรถไฟใต้ดินศูนย์วัฒนธรรมแห่งประเทศไทย",
    "สถานี พระราม 9 MRT ",
    "7600 Phetchaburi Rd, Bang Kapi, Huai Khwang, Krung Thep Maha Nakhon 10310, Thailand",
    # "สถานีรถไฟใต้ดินสุขุมวิท",
    "สถานีรถไฟใต้ดินศูนย์การประชุมแห่งชาติสิริกิติ์",
    # "สถานีรถไฟใต้ดินคลองเตย",
    # "สถานีรถไฟใต้ดินลุมพินี",
    # "สถานีรถไฟใต้ดินสีลม",
    "สถานีรถไฟใต้ดินสามย่าน",
    # "สถานีรถไฟใต้ดินหัวลำโพง",
    "สถานีรถไฟใต้ดินวัดมังกร",
    "สถานีรถไฟใต้ดินสามยอด",
    "สถานีรถไฟใต้ดินสนามไชย",
    "สถานีรถไฟใต้ดินอิสรภาพ",  # ท่าพระ แล้วบางไผ่
    "สถานีรถไฟใต้ดินบางไผ่",
    "สถานีรถไฟใต้ดินบางหว้า",
    "สถานีรถไฟใต้ดินเพชรเกษม 48",
    "สถานีรถไฟใต้ดินภาษีเจริญ 607 ถนน เพชรเกษมสายเก่า แขวงบางหว้า เขตภาษีเจริญ กรุงเทพมหานคร 10160",
    "สถานีรถไฟใต้ดินบางแค แขวงบางแคเหนือ เขตบางแค กรุงเทพมหานคร 10160",
    # "สถานีรถไฟใต้ดินสีลม",
    "สถานีรถไฟใต้ดินหลักสอง 13 ซ. เพชรเกษม 82 แขวงบางแคเหนือ เขตบางแค กรุงเทพมหานคร 10160",
]

# # yellow
# locations = [
#     # "สถานี ลาดพร้าว",  ###
#     "สถานีรถไฟรางเดี่ยวภาวนา",
#     "สถานี โชคชัย 4",
#     "สถานีรถไฟรางเดี่ยวลาดพร้าว 71",
#     "สถานีรถไฟรางเดี่ยวลาดพร้าว 83",
#     "สถานีรถไฟรางเดี่ยวมหาดไทย",
#     "สถานีรถไฟรางเดี่ยวลาดพร้าว 101",
#     "สถานี บางกะปิ",
#     "สถานีรถไฟรางเดี่ยวแยกลำสาลี",
#     "สถานีรถไฟรางเดี่ยวศรีกรีฑา",
#     "สถานีหัวหมาก รถไฟฟ้าสายสีเหลือง แขวงสวนหลวง เขตสวนหลวง กรุงเทพมหานคร 10250",
#     "สถานีรถไฟรางเดี่ยวกลันตัน",
#     "สถานีรถไฟรางเดี่ยวศรีนุช",
#     "สถานีรถไฟรางเดี่ยวศรีนครินทร์ 38",
#     "สถานีรถไฟรางเดี่ยวสวนหลวง ร.9",
#     "สถานีรถไฟรางเดี่ยวศรีอุดม",
#     "สถานีรถไฟรางเดี่ยวศรีเอี่ยม",
#     "สถานีรถไฟรางเดี่ยวศรีลาซาล",
#     "สถานีรถไฟรางเดี่ยวศรีแบริ่ง",
#     "สถานีรถไฟรางเดี่ยวศรีด่าน",
#     "สถานีรถไฟรางเดี่ยวศรีเทพา",
#     "สถานีรถไฟรางเดี่ยวทิพวัล",
#     "สถานีรถไฟฟ้า MRT สายสีเหลือง สำโรง",
# ]


data = []

# data.append(["สถานีลาดพร้าว", 13.807000, 100.574789])  # yellow

for location in locations:  # [1:] yellow
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={location}&key={api_key}"

    response = requests.get(url)
    data_json = response.json()

    if data_json["status"] == "OK":
        lat = data_json["results"][0]["geometry"]["location"]["lat"]
        lng = data_json["results"][0]["geometry"]["location"]["lng"]
        data.append([location, lat, lng])
    else:
        print(f"Error for location: {location}")

data.insert(10, ["สถานีรถไฟใต้ดินบางซื่อ", 13.80313166, 100.5393519])
data.insert(11, ["สถานีรถไฟใต้ดิน กำแพงเพชร MRT", 13.7977896, 100.5475589])
data.insert(15, ["สถานีรัชดาภิเษก", 13.799141, 100.574613])
data.insert(17, ["สถานีห้วยขวาง", 13.778505, 100.573645])
data.insert(21, ["สถานีสุขุมวิท", 13.73845642, 100.561462])
data.insert(23, ["สถานีคลองเตย", 13.722292, 100.553916])
data.insert(24, ["สถานีลุมพินี", 13.725769, 100.545678])
data.insert(25, ["สถานีสีลม", 13.729534, 100.536631])
data.insert(27, ["สถานีหัวลำโพง", 13.737540, 100.517073])

# data.append(["สถานีบางหว้า", 13.7207756, 100.4577677])
# Write to CSV
with open("blue_lines.csv", "w", newline="", encoding="utf-8") as csvfile:  ##
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["loc", "lat", "lon"])
    csvwriter.writerows(data)

# Create DataFrame
# df = pd.DataFrame(data, columns=["Location", "lat", "long"])

# df.to_csv('locations_dataframe.csv', index=True)
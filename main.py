import imager
import weather
from PIL import Image, ImageDraw, ImageFont  # 編輯照片用
from googletrans import Translator

title_dict = {
    # "日期": [760, 160],
    "天氣": [850, 160],
    "氣溫": [1210, 160],
    "降雨": [1460, 160],
    "舒適度": [1710, 160],
}

if __name__ == "__main__":

    weather_list = weather.getWeatherData()
    date_dict = {
        "year": "",
        "month": "",
        "datetime": [],
    }

    for index, item in enumerate(weather_list):
        time = item['startTime']  # "2024-06-11 18:00:00"
        tmp_list = time.split("-")  # ["2024", "06", "11 18:00:00"]

        if index == 0:
            date_dict['year'] = tmp_list[0]
            date_dict['month'] = tmp_list[1]

        tmp_datetime_list = tmp_list[2].split()
        datetime_list = [tmp_datetime_list[0], tmp_datetime_list[1][:-3]]
        date_dict['datetime'].append(datetime_list)

        if index == len(weather_list) - 1:
            date_dict['datetime'].append(
                [item['endTime'][8:10], item['endTime'][11:-3]])

    translator = Translator()
    translated_keyword = translator.translate(weather_list[0]["Wx"],  dest='zh-TW')
    background_list = imager.getBackground(
        weather=translated_keyword.text, count=1)

    if background_list is not None:
        noto_serif = ImageFont.truetype(
            'assets/NotoSerifTC-VariableFont_wght.ttf', size=40)
        # print("noto_serif:", noto_serif.get_variation_names())
        rubik = ImageFont.truetype('assets/Rubik-VariableFont_wght.ttf', size=40)
        # print("rubik:", rubik.get_variation_names())

        for index, background in enumerate(background_list):
            weather_image = Image.new("RGBA", (1920, 1080), color=10)
            weather_image.paste(background, (0, 0))
            weather_data_box = ImageDraw.Draw(weather_image)

            black_layer = Image.new("RGBA", (1920, 1080))
            black_draw = ImageDraw.Draw(black_layer, "RGBA")
            black_draw.rectangle(xy=(0, 0, 1920, 1080), fill=(0, 0, 0, 100))
            black_layer.putalpha(100)

            weather_image.paste(Image.alpha_composite(
                weather_image, black_layer))

            for key, value in title_dict.items():
                weather_data_box.text(
                    value,
                    key,
                    fill=(255, 255, 255), anchor="ma", font=noto_serif
                )

            for order, item in enumerate(weather_list):
                # weather_data_box.text(
                #     (230, 300 - 25 + 200 * order),
                #     f"{item['startTime'][:-3]}",
                #     fill=(255, 255, 255), anchor="ma", font=rubik
                # )

                # weather_data_box.text(
                #     (230, 300 + 25 + 200 * order),
                #     f"{item['endTime'][:-3]}",
                #     fill=(255, 255, 255), anchor="ma", font=rubik
                # )

                weather_data_box.text(
                    (title_dict['天氣'][0], 320 + 165 * order),
                    f"{item['Wx']}",
                    fill=(255, 255, 255), anchor="ma", font=noto_serif
                )

                weather_data_box.text(
                    (title_dict['氣溫'][0], 320 + 165 * order),
                    f"{item['MinT']}~{item['MaxT']}",
                    fill=(255, 255, 255), anchor="ma", font=noto_serif
                )

                weather_data_box.text(
                    (title_dict['降雨'][0], 320 + 165 * order),
                    f"{item['PoP']}",
                    fill=(255, 255, 255), anchor="ma", font=noto_serif
                )

                weather_data_box.text(
                    (title_dict['舒適度'][0], 320 + 165 * order),
                    f"{item['CI']}",
                    fill=(255, 255, 255), anchor="ma", font=noto_serif
                )

            noto_serif = ImageFont.truetype(
                'assets/NotoSerifTC-VariableFont_wght.ttf', size=80)
            noto_serif.set_variation_by_name("Bold")
            weather_data_box.text(
                (180, 80),
                f"{date_dict['year']}",
                fill=(250, 140, 5), anchor="ma", font=noto_serif
            )
            weather_data_box.text(
                (390, 80),
                f"{date_dict['month']}月",
                fill=(250, 140, 5), anchor="ma", font=noto_serif
            )

            for order, item in enumerate(date_dict['datetime']):

                noto_serif = ImageFont.truetype(
                    'assets/NotoSerifTC-VariableFont_wght.ttf', size=80)
                noto_serif.set_variation_by_name("Bold")
                weather_data_box.text(
                    (360, 200 + 170 * order),
                    f"{item[0]}",
                    fill=(255, 255, 255), anchor="ma", font=noto_serif
                )

                noto_serif = ImageFont.truetype(
                    'assets/NotoSerifTC-VariableFont_wght.ttf', size=40)
                noto_serif.set_variation_by_name("Light")
                weather_data_box.text(
                    (480, 230 + 170 * order),
                    f"{item[1]}",
                    fill=(255, 255, 255), anchor="ma", font=noto_serif
                )

                weather_data_box.line((550, 260 + 170 * order, 1800, 260 + 170 * order))
                weather_data_box.line((100, 260 + 170 * order, 300, 260 + 170 * order))

            filename = f"result.png"
            weather_image.save(filename)

    else:
        print("取得照片失敗!")

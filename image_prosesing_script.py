import cv2  # open source computer version 2
import csv


def is_leap(l_year):
    # cange value 29 if leap else 28 for feb month
    if l_year % 4 == 0 and (l_year % 100 != 0 or l_year % 400 == 0):
        feb = 29
    else:
        feb = 28
    return feb


listCount = 0
dataList = []
mulplyList = [
    100,
    116.6666667,
    133.3333333,
    150,
    162.5,
    175,
    187.5,
    200,
    203.8461538,
    207.6923077,
    211.5384615,
    215.3846154,
    219.2307692,
    223.0769231,
    226.9230769,
    230.7692308,
    234.6153846,
    238.4615385,
    242.3076923,
    246.1538462,
    250,
    252.9411765,
    255.8823529,
    258.8235294,
    261.7647059,
    264.7058824,
    267.6470588,
    270.5882353,
    273.5294118,
    276.4705882,
    279.4117647,
    282.3529412,
    285.2941176,
    288.2352941,
    291.1764706,
    294.1176471,
    297.0588235,
    300,
    301.7857143,
    303.5714286,
    305.3571429,
    307.1428571,
    308.9285714,
    310.7142857,
    312.5,
    314.2857143,
    316.0714286,
    317.8571429,
    319.6428571,
    321.4285714,
    323.2142857,
    325,
    326.7857143,
    328.5714286,
    330.3571429,
    332.1428571,
    333.9285714,
    335.7142857,
    337.5,
    339.2857143,
    341.0714286,
    342.8571429,
    344.6428571,
    346.4285714,
    348.2142857,
    350,
    351.6666667,
    353.3333333,
    355,
    356.6666667,
    358.3333333,
    360,
    361.6666667,
    363.3333333,
    365,
    366.6666667,
    368.3333333,
    370,
    371.6666667,
    373.3333333,
    375,
    376.6666667,
    378.3333333,
    380,
    381.6666667,
    383.3333333,
    385,
    386.6666667,
    388.3333333,
    390,
    391.6666667,
    393.3333333,
    395,
    396.6666667,
    398.3333333,
    400,
    402.2727273,
    404.5454545,
    406.8181818,
    409.0909091,
    411.3636364,
    413.6363636,
    415.9090909,
    418.1818182,
    420.4545455,
    422.7272727,
    425,
    427.2727273,
    429.5454545,
    431.8181818,
    434.0909091,
    436.3636364,
    438.6363636,
    440.9090909,
    443.1818182,
    445.4545455,
    447.7272727,
    450,
    453.3333333,
    456.6666667,
    460,
    463.3333333,
    466.6666667,
    470,
    473.3333333,
    476.6666667,
    480,
    483.3333333,
    486.6666667,
    490,
    493.3333333,
    496.6666667,
    500,
    503.3333333,
    506.6666667,
    510,
    513.3333333,
    516.6666667,
    520,
    523.3333333,
    526.6666667,
    530,
    533.3333333,
    536.6666667,
    540,
    543.3333333,
    546.6666667,
    550,
    553.8461538,
    557.6923077,
    561.5384615,
    565.3846154,
    569.2307692,
    573.0769231,
    576.9230769,
    580.7692308,
    584.6153846,
    588.4615385,
    592.3076923,
    596.1538462,
    600,
]


start_Y = 1979
end_Y = 2020

# change month hear
start_M = 1
end_M = 12

# year loop
for year in range(start_Y, end_Y + 1):
    logList = []
    logCount = 0

    # month loop
    for month in range(start_M, end_M + 1):
        feb = is_leap(year)
        DAYS_IN_MONTH = [-1, 31, feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # change day hear
        start_D = 1
        end_D = DAYS_IN_MONTH[month]

        # days loop
        for day in range(start_D, end_D + 1):
            Y = year
            if month < 10:
                M = "0" + str(month)
            else:
                M = month
            if day < 10:
                D = "0" + str(day)
            else:
                D = day

            date_path = "D" + str(Y) + "-" + str(M) + "-" + str(D)
            date = str(D) + "/" + str(M) + "/" + str(Y)
            print(date)

            # Append an empty sublist inside the list
            n = 175
            dataList.append([0] * n)

            preimg = cv2.imread(str(date_path) + ".png")

            if preimg is None:
                print("There is no image present adding NA values :(")
                for i in range(174):
                    dataList[listCount][i + 1] = "?"

                log = "Image not present so added NA values"
                naCheck = 1
            else:
                img = cv2.cvtColor(preimg, cv2.COLOR_BGR2RGB)
                hsv_IMG = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
                h, s, v = cv2.split(hsv_IMG)

                # set img pixel size here
                h_pixel = 716
                v_pixel = 363

                for i in range(v_pixel):
                    for j in range(h_pixel):
                        tempH = h[i][j]
                        tempS = s[i][j]

                        if tempH < 141:
                            pos = 141 - (tempH + 1)

                            if tempS > 190:
                                dataList[listCount][pos + 1] += 1
                            else:
                                dataList[listCount][pos + 1] += 0

                        elif tempH < 181 and tempH > 160:
                            pos = 321 - (tempH + 1)

                            if tempS > 190:
                                dataList[listCount][pos + 1] += 1
                            else:
                                dataList[listCount][pos + 1] += 0

                log = "Image present and added values"
                naCheck = 0
            if naCheck == 0:
                # normalize data with realworld values
                total = 0
                for i in range(1, 162):
                    dataList[listCount][i] = dataList[listCount][i] * mulplyList[i - 1]

                    dataList[listCount][174] = (
                        dataList[listCount][174] + dataList[listCount][i]
                    )

                    if i == 1:
                        dataList[listCount][162] = (
                            dataList[listCount][162] + dataList[listCount][i]
                        )
                    elif i >= 2 and i <= 4:
                        dataList[listCount][163] = (
                            dataList[listCount][163] + dataList[listCount][i]
                        )
                    elif i >= 5 and i <= 8:
                        dataList[listCount][164] = (
                            dataList[listCount][164] + dataList[listCount][i]
                        )
                    elif i >= 9 and i <= 21:
                        dataList[listCount][165] = (
                            dataList[listCount][165] + dataList[listCount][i]
                        )
                    elif i >= 22 and i <= 38:
                        dataList[listCount][166] = (
                            dataList[listCount][166] + dataList[listCount][i]
                        )
                    elif i >= 39 and i <= 66:
                        dataList[listCount][167] = (
                            dataList[listCount][167] + dataList[listCount][i]
                        )
                    elif i >= 67 and i <= 96:
                        dataList[listCount][168] = (
                            dataList[listCount][168] + dataList[listCount][i]
                        )
                    elif i >= 97 and i <= 118:
                        dataList[listCount][169] = (
                            dataList[listCount][169] + dataList[listCount][i]
                        )
                    elif i >= 119 and i <= 133:
                        dataList[listCount][170] = (
                            dataList[listCount][170] + dataList[listCount][i]
                        )
                    elif i >= 134 and i <= 148:
                        dataList[listCount][171] = (
                            dataList[listCount][171] + dataList[listCount][i]
                        )
                    elif i >= 149 and i <= 160:
                        dataList[listCount][172] = (
                            dataList[listCount][172] + dataList[listCount][i]
                        )
                    elif i == 161:
                        dataList[listCount][173] = (
                            dataList[listCount][173] + dataList[listCount][i]
                        )

            # Set first rowvalue as date
            dataList[listCount][0] = date

            logList.append([0] * 2)
            logList[logCount][0] = date
            logList[logCount][1] = log

            listCount += 1
            logCount += 1

    logpath = "logfile" + str(Y) + "pi.txt"
    with open(logpath, "w") as f:
        write = csv.writer(f)
        write.writerows(logList)
        print("logfile for year ", Y, " was saved")

with open("Ozone_data.csv", "w") as f:
    # using csv.writer method from CSV package
    write = csv.writer(f)
    write.writerows(dataList)

print("Finally finished!")

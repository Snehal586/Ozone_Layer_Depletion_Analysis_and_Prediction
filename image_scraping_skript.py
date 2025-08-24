## Importing Necessary Modules
import requests  # to get image from the web
import shutil  # to save it locally
import csv


def is_leap(l_year):
    # cange value 29 if leap else 28 for feb month
    if l_year % 4 == 0 and (l_year % 100 != 0 or l_year % 400 == 0):
        feb = 29
    else:
        feb = 28
    return feb


listCount = 0


# change year hear
start_Y = 1979
end_Y = 2020

# change month hear
start_M = 1
end_M = 12

# year loop
for year in range(start_Y, end_Y + 1):
    logCount = 0
    logList = []
    # month loop
    for month in range(start_M, end_M + 1):
        # defining days in month
        feb = is_leap(year)
        DAYS_IN_MONTH = [-1, 31, feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # change day here
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

            # conacting date structure
            date_path = "Y" + str(Y) + "/M" + str(M)
            date = "D" + str(Y) + "-" + str(M) + "-" + str(D)
            pdate = str(D) + "/" + str(M) + "/" + str(Y)
            print(pdate)

            # defing file path
            if Y < 2018:
                image_url = (
                    "https://ozonewatch.gsfc.nasa.gov/ozone_maps/images/"
                    + date_path
                    + "/OZONE_"
                    + date
                    + "_G^716X363.IOMI_PAURA_V8F_MGEOS5FP_LGL.PNG"
                )
            else:
                image_url = (
                    "https://ozonewatch.gsfc.nasa.gov/ozone_maps/images/"
                    + date_path
                    + "/OZONE_"
                    + date
                    + "_G^716X363.IOMPS_PNPP_V21_MGEOS5FP_LGL.PNG"
                )

            # defining file name
            filename = str(date) + ".png"
            # defining path

            # Opening the url image, set stream to True, this will return the stream content.
            r = requests.get(image_url, stream=True)

            # Check if the image was retrieved successfully
            if r.status_code == 200:
                # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
                r.raw.decode_content = True

                # Open a local file with wb ( write binary ) permission.
                with open(filename, "wb") as f:
                    shutil.copyfileobj(r.raw, f)

                log = "Image sucessfully Downloaded :) "
                print(log, filename)
            else:
                log = "Image not Downloaded :("
                print(log)
            # Append loglist
            logList.append([0] * 2)
            logList[logCount][0] = pdate
            logList[logCount][1] = log

            # Adding count varibales
            listCount += 1
            logCount += 1

    # Saving  loglist in text file
    logfileName = "logfile" + str(Y) + ".txt"
    with open(logfileName, "w") as f:
        write = csv.writer(f)
        write.writerows(logList)
        print("logfile saved")


print("Finally finished!")

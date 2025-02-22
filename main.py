from requests import get
from datetime import date, timedelta
from csv import writer


def collect_data(year_a, month_a, day_a, year_b, month_b, day_b):

    csv_data = [['Date', 'Saint', 'Scripture', 'Lives']]
    from datetime import date, timedelta
    
    start_date = date(year_a, month_a, day_a)
    end_date = date(year_b, month_b, day_b)
    delta = timedelta(days=1)
   
    while start_date <= end_date:
       
        year = start_date.year
        month = start_date.month
        day = start_date.day
       
        api_url = f"https://orthocal.info/api/gregorian/{year}/{month}/{day}/"
        response = get(api_url)

        if response.status_code == 200:
            data = response.json()
            days_data = []
           
            date = f"{year}-{month}-{day}"

            saint = data["summary_title"]
           
            scriptures = []
            for scripture in data["readings"]:
                scriptures.append(scripture["short_display"])
               
            lives = []
            for life in data["stories"]:
                lives.append(life["title"] + ": " + life["story"])
           
            days_data.append(date)
            days_data.append(saint)
            days_data.append(scriptures)
            days_data.append(lives)
           
            csv_data.append(days_data)
           
        else:
            print(f"Error: {response.status_code}")

        start_date += delta

    #print(csv_data)
       
   
    with open('example.csv', 'w', newline='') as file:
        w = writer(file)
        w.writerow(csv_data[0])
        w.writerows(csv_data[1:])


def main():

    year_a = 2025
    month_a = 2
    day_a = 21

    year_b = 2026
    month_b = 2
    day_b = 21

    collect_data(year_a, month_a, day_a, year_b, month_b, day_b)


main()

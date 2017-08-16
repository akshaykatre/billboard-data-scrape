import billboard
import json
import datetime
import pdb
import os 

def get_data(chart, time):
    """ Returns the required chart from the billboard for any 
    given date """
    return billboard.ChartData(chart, date= time)

YEAR = 1970
ENDYEAR = 1975

def main():
    """ The function runs the scraper and makes json files in 'datafiles' folder """
    START_DATE = datetime.datetime(YEAR, 1, 1)
    ## Loop over the years from which to collect the data 
    for year in range(YEAR, ENDYEAR):
        print(year)
        end_date = datetime.datetime(year+1, 1, 1)
        ## Make the folder for data if it doesn't exist
        if os.path.exists("datafiles") == False:
            os.mkdir("datafiles")
        ## Open the json file in which to write the information. One
        ## json file per year
        with open("datafiles/"+str(year)+".json", mode="w", encoding="utf-8") as f:
            ## For each year, loop and collect top-100 in one week time frames
            ## The end date is set to the end of the year
            while START_DATE < end_date:
                artists = []
                titles = []
                date = []
                date_string = START_DATE.strftime('%Y-%m-%d')
                chartdata = get_data('hot-100', date_string)
                for songs in chartdata:
                    data = {}
                    artists.append(songs.artist)
                    titles.append(songs.title)
                    date.append(date_string)
                    data.update({'artist': songs.artist, 'title':songs.title, 'date':date_string})
                    feeds = json.dump(data, f)
                    print(file=f)
                START_DATE += datetime.timedelta(days=7)
        
if __name__ == "__main__":
    main()

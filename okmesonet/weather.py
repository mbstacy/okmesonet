from pandas import read_fwf, concat, options, read_pickle
from datetime import datetime, timedelta
import numpy as np
import os, pytz
#import pandas as pd

from os.path import expanduser
home = expanduser("~")
#Create Mesonet Cache Directory
if not os.path.exists(os.path.join( home,'.okmesonet/mesonet_cache')):
    os.makedirs(os.path.join( home,'.okmesonet/mesonet_cache'))

def get_mesonet_dataframe(start_date,end_date,site,local_time=None):
    local_data_cache = os.path.join( home,'.okmesonet/mesonet_cache/{0}{1}.p')
    url_template = "http://www.mesonet.org/index.php/dataMdfMts/dataController/getFile/{0}{1}/mts/TEXT/"
    day_count = (end_date - start_date).days +1
    df_pieces=[]
    for single_date in (start_date + timedelta(n) for n in range(day_count)):
        picklefile = local_data_cache.format(single_date.strftime('%Y%m%d'),site)
        if os.path.isfile(picklefile):
            # Read from Mesonet Cache
            df = read_pickle(picklefile)
            df=set_timezone(df,single_date, timezone=local_time)
        else:
            url = url_template.format(single_date.strftime('%Y%m%d'),site)
            df = read_fwf(url,header=2,
                          widths=[5,6,6,7,7,7,7,6,7,7,7,8,9,6,7,7,7,7,7,7,7,8,8,8],
                          na_values=['-999','-998','-997','-996','-995'],
                          skipfooter=1)
            # Save to Mesonet Cache
            df.to_pickle(picklefile)
            df=set_timezone(df,single_date, timezone=local_time)
        df_pieces.append(df)
    return concat(df_pieces)

def groupby(df,groupby,agg):
    grp =data.groupby(groupby)
    return grp.agg(agg)

def set_timezone(df,single_date, timezone=None):
    central = pytz.timezone("US/Central")
    utc = pytz.timezone("UTC")
    df["DATE"]=single_date.date()
    df['TIMESTAMP']=df.apply(lambda row:datetime(row['DATE'].year,row["DATE"].month,row["DATE"].day,int(row['TIME'] / 60),row['TIME'] % 60,0,0,utc),axis=1)
    if timezone:
        df['TIMESTAMP']=df.apply(lambda row:row['TIMESTAMP'].astimezone(central),axis=1)
        df['DATE']=df.apply(lambda row:row['TIMESTAMP'].date(),axis=1) 
    return df            

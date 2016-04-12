Oklahoma Mesonet Python Pandas
==============================

### Installation

        $ pip install https://github.com/mbstacy/okmesonet/zipball/master

##### Requirements
* Pandas

### Example

        from okmesonet import weather
        from datetime import datetime
        start_date = datetime(2010,3,1)
        end_date = datetime(2010,4,1)
        
        # UTC timezone
        weather.get_mesonet_dataframe(start_date,end_date,site)
        # Local Time
        weather.get_mesonet_dataframe(start_date,end_date,site,local_time=True) 
    
        Returns a Pandas Dataframe

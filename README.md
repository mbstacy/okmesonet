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

### Disclaimer

Data access may be restricted by organization and/or location. Please refer to
and follow policies found in the Oklahoma Mesonet Data Access Policy
(http://www.mesonet.org/index.php/site/about/data_access_and_pricing). The
authors and maintainers of okmesonet assume no responsibility for the use or
misuse of okmesonet.

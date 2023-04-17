import pandas as pd


class NJCleaner():

    def __init__(self, csv_path: str) -> None:
        #col_name = ['date','train_id','stop_sequence','from','from_id','to','to_id','scheduled_time','actual_time','delay_minutes','status','line','type']
        #self.data = pd.read_csv(route, skiprows=1, header=None, names=col_name)
        self.data = pd.read_csv(csv_path)


    def order_by_scheduled_time(self) -> pd.DataFrame:
        final_df = self.data.sort_values(by=['scheduled_time'])
        return final_df                  #új df-el tér vissza, self ugyanaz marad
    
    def drop_columns_and_nan(self) -> pd.DataFrame:
        df = self.data.drop(['from', 'to'], axis=1)
        df = df.dropna()
        return df

    

    def convert_date_to_day(self) -> pd.DataFrame:
        df = self.data
        df['day'] = pd.to_datetime(df['date']).dt.day_name()
        df = df.drop('date', axis=1)
        return df

    def convert_scheduled_time_to_part_of_the_day(self) -> pd.DataFrame:
        df = self.data
        df['part_of_the_day'] = pd.to_datetime(df['scheduled_time']).dt.hour.apply(lambda x: 
                                 'early_morning' if 4 <= x <= 7 
                                 else 'morning' if 8 <= x <= 11 
                                 else 'afternoon' if 12 <= x <= 15 
                                 else 'evening' if 16 <= x <= 19 
                                 else 'night' if 20 <= x <= 23 
                                 else 'late_night')
        df = df.drop('scheduled_time', axis=1)
        return df

    def convert_delay(self) -> pd.DataFrame:
        df = self.data
        df['delay'] = df['delay_minutes'].apply(lambda x:
                                0 if 0 <= x <= 5
                                else 1)
        return df


    def drop_unnecessary_columns(self) -> pd.DataFrame:
        df = self.data.drop(['train_id', 'actual_time', 'delay_minutes'], axis=1)       #scheduled_time -t eldobjuk convert_scheduled_time_to_part_of_the_day -ben
        return df

    def save_first_60k(self, filename: str):
        self.data.head(60000).to_csv(filename, index=False)

    def prep_df(self, filename='data/NJ.csv'):
        self.data = self.order_by_scheduled_time()
        self.data = self.drop_columns_and_nan()
        self.data = self.convert_date_to_day()
        self.data = self.convert_scheduled_time_to_part_of_the_day()
        self.data = self.convert_delay()
        self.data = self.drop_unnecessary_columns()
        self.save_first_60k(filename)
        



nj = NJCleaner('2018_03.csv')
nj.prep_df()

"""nj = NJCleaner('2018_03.csv')
nj.data = nj.order_by_scheduled_time()
nj.data = nj.drop_columns_and_nan()
nj.data = nj.convert_date_to_day()
nj.data = nj.convert_scheduled_time_to_part_of_the_day()
nj.data = nj.convert_delay()
nj.data = nj.drop_unnecessary_columns()
nj.save_first_60k('60k_by_me.csv')
print(nj.data)"""


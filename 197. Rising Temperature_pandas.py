import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather['recordDate'] = pd.to_datetime(weather['recordDate'])
    weather.sort_values(by='recordDate', inplace=True)
    copy = weather.copy()
    copy['recordDate'] = copy['recordDate'] + pd.to_timedelta(1, unit='D')
    merged = pd.merge(weather, copy, on='recordDate', suffixes=('_today', '_yesterday'))
    result = merged[merged['temperature_today'] > merged['temperature_yesterday']][['id_today']].rename(columns={'id_today': 'id'})
    return result

# Corona-Tracker
Convert Novel coronavirus(2019-nCoV) statistical data from the Chinese medical community(dxy.cn) to json format

# Requirements
```
python3
```

# Usage
1. Get infection statistics by country

    ![corona-tracker-all](./images/corona_tracker_all.png)
    ```
    CoronaTracker.get_all_statistics()
    ```

2. Get infection statistics for all countries

    ![corona-tracker-country](./images/corona_tracker_country.png)
    ```
    CoronaTracker.get_country_statistics()
    ```
## Silke's Ideas

**GOAL: trying to predict noise to apply certain mitigating measures.**
Causes of noise: federal government + possible norms exceeded (Dutch sources)
    https://www.health.belgium.be/nl/geluid-en-geluidshinder#:~:text=De%20belangrijkste%20oorzaken%20van%20deze,huishoudelijke%20apparaten%2C%20muziekinstallaties%2C%20%E2%80%A6.
    https://www.health.belgium.be/nl/geluidsnormen-voor-producten

**Preprocessing → remark: what is done by the original paper (+ are the origins of noises determinable?)**
- Outlier detection: eg. LC_WINDSPEED → not all graphs seem to be correct
- Wrong values or units eg. impossible measurements 
- Checks with other datasets for correctness eg. storm periods for large wind detections?

**What parameters could be related to the noise levels:** 
- Weather circumstances
- Holiday periods link → daily
- Day of the week (eg. Thursday = student going out day, Wednesday high school finishes earlier)
- Season (eg. winter everyone inside vs. summer outside → daylight hour: night vs. day?) → monthly
- Greenery (terrain data, dampening function → private garden main focus in paper link) 
- Peak hour car traffic (8AM - 5PM) → look hourly
- Air traffic
- Environment of measurement (shops, roads, schools) → see greenery and paper

**Methods:** 
- Random forest (library xgdboost)

**Visualisation ideas:** 
- Map with coloured ranges of predicted noise (link to something understandable in legend: aeroplane, baby crying etc.)
- Map with environment: schools/shops/student bars… vs. largest noise levels measured
- Wheater prediction app (give example) → make this for noise, where the different variables like precipitation can remain and just instead of temp use noise
- Kind of like the earthquake report, where you have spots that ‘pop off’ the map when/where the norms are exceeded
- Visual weather/noise map with colours

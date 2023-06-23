
from plyer import notification
from covid import Covid
covid = Covid()
india = covid.get_status_by_country_name("india")
confirmed=india['confirmed']
active_cases=india['active']
death_rate=india['deaths']
recoverd_cases=india['recovered']
    
title1="Latest Covid19 updates on India"
msg="confirmed cases:{} \nactive cases:{} \ndeath rate:{} \nrecovery rate:{}".format(confirmed,active_cases,death_rate,recoverd_cases)

notification.notify(title=title1,message=msg,app_icon=None ,timeout=60,toast=False)

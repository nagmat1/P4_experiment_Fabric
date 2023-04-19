from datetime import datetime
from datetime import timezone
from datetime import timedelta

slice_name = 'In_network_caching_exp'
#Set end host to now plus 2 day
end_date = (datetime.now(timezone.utc) + timedelta(days=2)).strftime("%Y-%m-%d %H:%M:%S %z")

try:
    slice = fablib.get_slice(name=slice_name)

    slice.renew(end_date)
except Exception as e:
    print(f"Exception: {e}")

from flask import Blueprint, jsonify

from .utils import MakeYamlCall

selector = Blueprint('selector', __name__)


@selector.route('/booking')
def booking():
    
    url = "https://www.booking.com/searchresults.en-us.html?label=gog235jc-1DCAEoggI46AdIM1gDaGWIAQGYATG4ARfIAQzYAQPoAQH4AQKIAgGoAgO4AoOts50GwAIB0gIkMjE0NzI2NTYtZGQ3NC00MWFmLTk1ZTktMGVmY2MzYWEwYjIy2AIE4AIB&sid=be36d7c2b0a515b8eb021c4eb78dd13a&aid=397594&ss=Plitvi%C4%8Dka+Jezera&sb_entire_place=1&ssne=Plitvi%C4%8Dka+Jezera&ssne_untouched=Plitvi%C4%8Dka+Jezera&efdco=1&lang=en-us&sb=1&src_elem=sb&dest_id=-92146&dest_type=city&checkin=2023-01-06&checkout=2023-01-08&group_adults=2&no_rooms=1&group_children=2&age=13&age=6&sb_travel_purpose=leisure&nflt=privacy_type%3D3%3Bprivacy_type_no_date%3D3&order=class_and_price"
    yaml_file = "booking.yml" 

    data = MakeYamlCall(url, yaml_file).data
    
    return jsonify(data)
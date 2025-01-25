import os
from django.conf import settings

# Used for inspecting objects easily
def save_obj(obj):
    str_obj = str(obj)
    if not os.path.exists(f"{settings.BASE_DIR}/rssfeed/sample_objects"):
        os.makedirs(f"{settings.BASE_DIR}/rssfeed/sample_objects")
    with open(f"{settings.BASE_DIR}/rssfeed/sample_objects/object.txt","w") as f:
                f.writelines(str_obj)

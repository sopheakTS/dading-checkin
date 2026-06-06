from supabase_client import supabase
from datetime import datetime

def checkin(user_id):
    supabase.table("attendance").insert({
        "employee_id": user_id,
        "checkin_time": datetime.now().isoformat(),
        "checkout_time": None,
        "date": datetime.now().date().isoformat()
    }).execute()


def checkout(user_id):
    supabase.table("attendance") \
        .update({"checkout_time": datetime.now().isoformat()}) \
        .eq("employee_id", user_id) \
        .is_("checkout_time", None) \
        .execute()
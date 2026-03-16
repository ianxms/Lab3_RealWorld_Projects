SEED_NUM = 9
FAVORITE_ARTIST = "BRUNO_MAJOR_AND_THE_BAND"
CONTROL_NUM = max(1, SEED_NUM)

def compute_access_level(control, artist):
    return control * 3 + len(artist)

def validate_access(level, control):
    threshold = control * 5
    return "ACCESS GRANTED" if level >= threshold else "ACCESS DENIED"

def audit_log(func):
    def wrapper(*args, **kwargs):
        print("Authorization Started")
        result = func(*args, **kwargs)
        print("Authorization Completed")
        return result
    return wrapper

@audit_log
def run_protocol(control, artist):
    level = compute_access_level(control, artist)
    decision = validate_access(level, control)
    return decision

# actually run it
print(run_protocol(CONTROL_NUM, FAVORITE_ARTIST))

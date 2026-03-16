def play_count_stream(limit):
    for i in range(limit):
        if i % 2 == 0:
            yield i**2

def monitor(func):
    def wrapper(*args, **kwargs):
        print("Processing Started")
        result = func(*args, **kwargs)
        print("Processing Completed")
        return result
    return wrapper

CONTROL_NUM = 9
FAVORITE_ARTIST = "BRUNO_MAJOR"
limit = CONTROL_NUM + len(FAVORITE_ARTIST)

@monitor
def run_stream(limit):
    total_plays = 0
    records = 0
    for play in play_count_stream(limit):
        print("Play Count:", play)
        total_plays += play
        records += 1
    return total_plays, records

total_plays, records = run_stream(limit)

print("Total Plays:", total_plays)
print("Number of Records Processed:", records)

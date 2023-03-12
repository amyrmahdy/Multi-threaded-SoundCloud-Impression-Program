import sys
import concurrent.futures
from playfunc import playing


workers = int(sys.argv[1])
views = int(sys.argv[2])
seconds = int(sys.argv[3])

with open("input.txt","r") as f:
    musics = f.read().split("\n")[:-1]

with concurrent.futures.ThreadPoolExecutor(max_workers = workers) as executor:
    joining = []
    for url_music in musics:
        future = executor.submit(playing,url_music,views,seconds)
        joining.append(future)
    for join in joining:
        join.result()

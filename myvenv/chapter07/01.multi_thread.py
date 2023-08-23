import threading


# function that will be used in thread
def work():
    print("[sub] start")
    keyword = input("[sub] Please enter a search term. >>>")
    print(f"[sub] Starting serach from {keyword}....")
    print("[sub] end")


# main thread
print("[main] start")

worker = threading.Thread(target=work)
worker.daemon = True
worker.start()

print("[main] The main thread carries out its own tasks.")
print("[main] end")

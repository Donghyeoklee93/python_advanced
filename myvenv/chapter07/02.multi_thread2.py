import threading
import time


def buyer():
    for i in range(5):
        print("[Buying] request data...")
        time.sleep(1)
        print("[Buying] analyze data...")
        time.sleep(1)
        print("[Buying] now is a good time to buy...")
        time.sleep(1)
        print("[Buying] buying...")
        time.sleep(1)


def seller():
    for i in range(5):
        print("[Selling] request data...")
        time.sleep(1)
        print("[Selling] analyze data...")
        time.sleep(1)
        print("[Selling] Should I cut my losses or take profits?...")
        time.sleep(1)
        print("[Selling] selling...")
        time.sleep(1)


print("[nain] start")
buyer = threading.Thread(target=buyer)
seller = threading.Thread(target=seller)
buyer.start()
seller.start()

buyer.join()
seller.join()

print("[main] end")

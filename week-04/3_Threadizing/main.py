# IMPORTS
import threading as thread
import functions

def threadize() -> None:

    layers = [functions.f, functions.g, functions.h]
    for layer in layers:
        threads= []
        for index , func in enumerate(layer):
            t = thread.Thread(target=func, name=str(index + 1))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()







import logging
import warnings
import datetime
import os


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    moment = datetime.datetime.now().strftime('%Y-%m-%m-%H%M%S')
    logdir = "./logs/"
    if not os.path.isdir(logdir):
        os.mkdir(logdir)
    logname = logdir + moment + ".log"

    logging.basicConfig(filename=logname,
                        filemode='a',
                        format='%(asctime)s,%(msecs)s %(levelname)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        level=logging.DEBUG)

    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

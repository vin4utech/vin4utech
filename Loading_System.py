from import_methods import *
from Main_Menu import text_Delay

time_sec = 0.02

# This part is for loading_System using Function
def loading_System():
    print()
    print()
    text_Delay('_'*5, time_sec)
    text_Delay('   Checking System Files....', 0.03)
    print('\n')
    text_Delay('_'*5, time_sec)
    text_Delay('   Checking Database Connection....', 0.03)
    print('\n')
    text_Delay('. '*30, 0.03)
    print('\n')
    text_Delay('_'*5, time_sec)
    text_Delay('   Connection OK......', 0.03)
    print('\n')
    time.sleep(0.3)
    os.system('cls')
import csv, pyautogui


#this is the new goulds pricing excel file, I saved it as a CSV in my practice material folder
file1 = r'C:\\Users\\trohweder\\Projects\\practice material\\Goulds2.csv'
#this one has all PFC goulds part numbers
file2 = r'C:\\Users\\trohweder\\Projects\\practice material\\PFC_GOULDS_PARTNUMBERS.csv'
f1 = open(file1, 'r')
f2 = open(file2, 'r')

#this is a list of all goulds parts in pfc's system
raw_pfc_part_list = list(csv.reader(f2))

#this generates a list of lists we can separate the part numbers and prices from
raw_part_list = list(csv.reader(f1))
raw_part_list = raw_part_list[3:]  #the first 3 are all labels and useless info
#[0][0] is the part number and [0][5] is the price

pfc_part_list = [i[0] for i in raw_pfc_part_list]
#this refines the pfc part list so that it is just a list of strings that are part numbers
part_list = [(i[0], i[5]) for i in raw_part_list]
#this makes a list of tuples that are all of the goulds parts and their prices

#this refines it down to the tuples of just parts PFC has on file
pricing_list = [i for i in part_list if i[0] in pfc_part_list]


#this is the multiplier for the products
multiplier = '0.42'
print(pricing_list[1])
#working on the auto entry for pricing, pricing screen must be fullscreen on the far left
def auto_entry():
    for i in pricing_list[1:3]:
        pyautogui.click(x=-1795,y=-105, duration=0.25)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.typewrite(i[0])
        pyautogui.press('enter')
        pyautogui.click(x=-1350,y=0, duration=0.25)
        pyautogui.typewrite(i[1], interval=0.2)
        pyautogui.press('enter')
        pyautogui.press('enter')
        pyautogui.press('enter')
        pyautogui.press('l')
        pyautogui.press('enter')
        pyautogui.typewrite(multiplier, interval=0.2)
        pyautogui.press('enter')
        pyautogui.click(x=-350,y=650, duration=0.25)
        print(i)
auto_entry()

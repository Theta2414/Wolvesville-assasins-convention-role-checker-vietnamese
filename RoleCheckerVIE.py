from tkinter import *

#Role list
role_list = ['bác sĩ','bảo vệ','quản ngục','kỹ nữ','mục sư','tiên tri','thầy bói','thám tử','thầy đồng',
            'thị trưởng','phù thủy','bán sói','sói trẻ','thằng ngố','tin tặc','côn đồ','đồ tể','lực sĩ',
            'xạ thủ','ná thủ','giám ngục','ma nữ','thiện xạ','thẩm phán','con bạc','pháp y','thầy cúng',
            'thợ rèn','sói thạch','sói mù','giáo chủ','xác sống','dân làng','tổng thống','người canh gác',
            'cảnh sát trưởng','hoa bé con','thần tình yêu','sói ác mộng','sói pháp sư','sói hắc ám',
            'sói hộ vệ','sói đầu đàn','sói tiên tri','thợ săn người','kẻ phóng hỏa','người gác đêm',
            'nhà phân tích','nhà ngoại cảm','người gọi hồn','thợ làm bánh','người thuyết giáo',
            'người đặt bẫy','người gắn cờ','kẻ báo thù','người rung chuông','người khai mệnh',
            'kẻ xúi giục','kẻ hỗn loạn','kẻ trộm mộ','kẻ vô danh','sói phân tách','sói mèo con',
            'sói thao túng','sói tà thuật','sói bão tố','sói đầm lầy','sói lừa đảo','sói mơ hồ',
            'sói biên kịch','sói điên cuồng','sói độc tố','sói hòa bình','sói bướng bỉnh','sói chiêu hồn',
            'sói phù thủy','kẻ đặt bom','nhà giả kim','nhân ngư','thợ săn quái thú','cậu bé miệng bự',
            'sát nhân hàng loạt','tiên tri tập sự','nghệ sĩ vĩ cầm','bà già khó tính','nhà thiên văn học',
            'người yêu hòa bình','thám tử ác ma','sát nhân ảnh thuật','kẻ hâm mộ ma sói']

#Function for the button "_"
def add1():
    test.config(state = 'normal')
    test.insert(END, "_")
    test.config(state = 'disabled')

#Function for the button "0"
def add2():
    test.config(state = 'normal')
    test.insert(END, "0")
    test.config(state = 'disabled')

#Function to add multiple underscores
def addmul20():
    test.config(state = 'normal')
    test.insert(END, "__0")
    test.config(state = 'disabled')

def addmul30():
    test.config(state = 'normal')
    test.insert(END, "___0")
    test.config(state = 'disabled')

def addmul40():
    test.config(state = 'normal')
    test.insert(END, "____0")
    test.config(state = 'disabled')

def addmul50():
    test.config(state = 'normal')
    test.insert(END, "_____0")
    test.config(state = 'disabled')

def backspace():
    test.config(state = 'normal')
    test.delete(len(test.get()) - 1, END)
    test.config(state = 'disabled')

#Function to standardize the input
def sta(sta_value):
    if sta_value[len(sta_value) - 1] == "0" or sta_value[len(sta_value) - 1] == " ":
        sta_value = sta_value.rstrip("0 ")
    
    test.config(state = 'normal')
    test.delete(0, END)
    test.insert(0, sta_value)
    test.config(state = 'disabled')
    
    return sta_value

#Function to analyze the word in entry and count the number of words and the number of characters
def count(count_value):
    
    wordcount = 0
    charcount = 0
    space = 0
    
    for i in range(len(count_value)):
        if (count_value[i] == "0") or (count_value[i] == " "):
            space += 1
        else:
            charcount += 1
    wordcount = space + 1
    
    return wordcount, charcount

#Function to sort list depends on the number of words and the number of characters
#Possolution is a sorted list checked the number of words and the number of characters
def find(wordcount_value, charcount_value, list_value):
    
    possolution_out = [ ]
    wordcount_sto = charcount_sto = 0
    
    for find in range(len(list_value)):
        sto = list_value[find]
        wordcount_sto, charcount_sto = count(list_value[find])
        if (wordcount_sto == wordcount_value) and (charcount_sto == charcount_value):
            possolution_out.append(list_value[find])
    
    return possolution_out

#Function to change the value in solution
def change(change_value):
    
    change_out = ""
    
    for change in range(len(change_value)):
        if (change_value[change] == " " or change_value[change] == "0"):
            change_out += "0"
        else:
            change_out += "_"
    
    return change_out

#Function to change the value in solution allowing spaces
def changeas(changeas_value):
    
    changeas_out = ""
    
    for changeas in range(len(changeas_value)):
        if (changeas_value[changeas] == " " or changeas_value[changeas] == "0"):
            changeas_out += "0"
        else:
            changeas_out += "_"
    
    return changeas_out

#Compare the word in input with values in posssolution
def compare(compare_value, possolution_value):
    
    mustsolution_out = [ ]
    
    for com in range(len(possolution_value)):
        if (change(possolution_value[com]) == change(compare_value)) or (changeas(possolution_value[com]) == changeas(compare_value)) :
            mustsolution_out.append(possolution_value[com])
    
    return mustsolution_out

#Compare the characters in input with the characters in mustsolution
#Mustsolution is a sorted list checked the location of underscores and spaces
def supersort(sup_value, mustsolution_value):
    
    finalsolution_out = [ ]
    char = False
    
    #Check if sup_value has characters
    for sup in range(len(sup_value)):
        if not(sup_value[sup] == "0" or sup_value[sup] == "_" or sup_value[sup] == " "):
            char = True
            break

    #Do this if it has characters
    if char:
        for com1 in range(len(mustsolution_value)):
            sto = mustsolution_value[com1]
            result = False
            for com2 in range(len(sup_value)):
                if not(sup_value[com2] == "0" or sup_value[com2] == "_" or sup_value[com2] == " "):
                    if sup_value[com2] == sto[com2]:
                        result = True
                    else:
                        break
            if result:
                finalsolution_out.append(mustsolution_value[com1])
    else:
        finalsolution_out = mustsolution_value

    return finalsolution_out

#
def hypersort(hypersort_value, role_list_value):
    
    possolution = [ ]
    mustsolution = [ ]
    finalsolution_out = [ ]
    wordcount = 0
    charcount = 0

    #Count
    wordcount, charcount = count(hypersort_value)

    #Sort lists
    possolution = find(wordcount, charcount, role_list_value)
    mustsolution = compare(hypersort_value, possolution)
    finalsolution_out = supersort(hypersort_value, mustsolution)
    
    return finalsolution_out

#Display the finalsolutions
def display():
    
    finalsolution = [ ]
    
    #Get the value
    entry = test.get()
    cal_value = sta(entry)

    #Sort
    finalsolution = hypersort(cal_value, role_list)

    #Clear the label to make sure that it is empty then print a new one
    label.config(text = finalsolution)

#If you want to add underscores until find a solution
def ufdisplay():
     
    finalsolution = [ ]
    
    #Get the value
    entry = test.get()
    cal_value = sta(entry)

    #Sort
    finalsolution = hypersort(cal_value, role_list)

    limit = 0
    
    while (len(finalsolution) == 0) and (limit < 5) and (len(cal_value) < 20):
        cal_value = cal_value + "_"
        test.config(state = "normal")
        test.insert(END, "_")
        test.config(state = "disabled")
        finalsolution = hypersort(cal_value, role_list)
        limit += 1

    #Clear the label to make sure that it is empty then print a new one
    label.config(text = finalsolution)

#Reset all values
def clear():

    test.config(state = 'normal')
    label.config(text = "")
    test.delete(0, END)
    test.config(state = 'disabled')

window = Tk()
window.geometry("1920x1200")
window.title("Role Check")
window.config(background = "#FB216D")

input_value = StringVar()

titletext = Label(window, text = "Role Checker", font=("Times New Roman", 36), background="#FB216D",  fg="white")
titletext.pack()

test = Entry(window, font = ("Arial", 24), textvariable = input_value, state = 'readonly')
test.pack()

button_underscore = Button(window, width = 8, height = 4, text = "_", font = (52), command = add1)
button_underscore.pack(side = LEFT)

button_space = Button(window, width = 8, height = 4, text = "0", font = (52), command = add2)
button_space.pack(side = LEFT)

button_20 = Button(window, width = 6, height = 3, text = "2", font = (52), command = addmul20)
button_20.pack(side = LEFT)

button_30 = Button(window, width = 6, height = 3, text = "3", font = (52), command = addmul30)
button_30.pack(side = LEFT)

button_40 = Button(window, width = 6, height = 3, text = "4", font = (52), command = addmul40)
button_40.pack(side = LEFT)

button_50 = Button(window, width = 6, height = 3, text = "5", font = (52), command = addmul50)
button_50.pack(side = LEFT)

label = Label(window, font = ("Arial", 24), fg = "white", bg = "#FB216D")
label.place(x=100, y=500)

checkbutton = Button(window, width = 8, height = 4, command = display, text = "CHECK")
checkbutton.pack(side = RIGHT)

ufcheckbutton = Button(window, width = 12, height = 4, command = ufdisplay, text = "Unfinished Check")
ufcheckbutton.pack(side = RIGHT)

clearbutton = Button(window, width = 8, height = 4, command = clear, text = "CLEAR" )
clearbutton.pack(side = RIGHT)

backspacebutton = Button(window, width = 8, height = 4, command = backspace, text = "Backspace" )
backspacebutton.pack(side = RIGHT)

window.bind("<Return>", lambda event: display())
window.bind("<space>", lambda event: add2())
window.bind(f"{1}", lambda event: add1())
window.bind(f"{2}", lambda event: addmul20())
window.bind(f"{3}", lambda event: addmul30())
window.bind(f"{4}", lambda event: addmul40())
window.bind(f"{5}", lambda event: addmul50())
window.bind("<Delete>", lambda event: clear())
window.bind("<BackSpace>", lambda event: backspace())
window.bind("<'>", lambda event: ufdisplay())

window.mainloop()

import tkinter as tk

window = tk.Tk()
window.title('Form Data Mahasiswa')
window.geometry

frame1 = tk.Frame(master=window)
frame1['relief'] = tk.GROOVE
frame1['borderwidth'] = 2
frame1.pack(side=tk.LEFT, fill=tk.Y)

frame2 = tk.Frame(master=window)
frame2['relief'] = tk.RIDGE
frame2.pack(side=tk.RIGHT)

list = {
    1: 'Nama Lengkap',
    2: 'NIM',
    3: 'Tanggal Lahir',
    4: 'Program Studi',
    5: 'Jurusan'
}
i = 4
for i in list:
    label = tk.Label(master=frame1)
    label['text'] = list[i], ':'
    label.grid(row=i, column=0, sticky=tk.W)

    entry = tk.Entry(master=frame2)
    entry['width'] = 50
    entry.grid(row=i, column=1, sticky=tk.W)
    i = i+1

    la = tk.Label(master=frame1)
    la['text'] = 'Sex :'
    la.grid(row=10, column=0, sticky=tk.W)
    va = tk.IntVar()
    ra1 = tk.Radiobutton(master=frame2, text='Pria', variable=va, value=1)
    ra1.grid(row=10, column=0, sticky=tk.W)

    ra2 = tk.Radiobutton(master=frame2, text='Wanita', variable=va, value=2)
    ra2.grid(row=10, column=1, sticky=tk.W)

button1 = tk.Button(master=frame2)
button1['text'] = 'Submit'
button1.grid(row=11, column=0, sticky=tk.W)

button2 = tk.Button(master=frame2)
button2['text'] = 'Batal'
button2.grid(row=11, column=1, sticky=tk.W)

window.mainloop()
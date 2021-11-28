import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import scrolledtext
from tkinter import ttk
from tkinter import messagebox
import sqlite3

window = tk.Tk()
window.title('DB_Screens')
window.geometry('942x381')

# Add some style
style = ttk.Style()
# Pick a theme
style.theme_use('default')

# Add tabs
tab = ttk.Notebook(window)
tab.grid(row=0, column=0, padx=5, pady=5)

# Search frames
frm_search = tk.Frame(window)
frm_search.grid(row=0, column=0, sticky='ewns')

frm_TL = tk.Frame(frm_search)
frm_TL.grid(row=0, column=0, sticky='ns', pady=36, padx=5)

frm_TM = tk.Frame(frm_search)
frm_TM.grid(row=0, column=1, sticky='ewns', padx=20)

# Action frames
frm_action = tk.Frame(window)
frm_action.grid(row=0, column=0)

frm_action_L = tk.Frame(frm_action)
# frm_action_L.grid(row=0, column=0)
# frm_action_L.pack(fill=tk.Y, side=tk.LEFT)
frm_action_L.place(x=20, y=20)

frm_action_R = tk.Frame(frm_action, borderwidth=2, relief="groove")
# frm_action_R.grid(row=0, column=1, sticky = 'ew')
# frm_action_R.pack(fill=tk.BOTH)
frm_action_R.place(x=300, y=15, width=212)

# Create Tabs
tab.add(frm_search, text='Search')
tab.add(frm_action, text='Action')


def query():
    #global records
    # txt.delete('1.0', tk.END)
    # Create or connect to database
    conn = sqlite3.connect('Screens_DB.db')
    # Create cursor
    cursor = conn.cursor()

    # Query records
    record = ''
    cursor.execute("SELECT *, oid FROM screens")
    records = cursor.fetchall()

    # print(records)

    # Take search values
    search_brand = search_brand_cb.get()
    search_model = search_ent_model.get()
    if search_model != 'All':
        search_model.upper()  # Convert search_model entry to upper case
    print(search_model)
    search_size = search_size_cb.get()
    search_resolution = search_res_cb.get()
    search_connector = search_conn_cb.get()
    search_touch = search_touch_cb.get()
    search_ears = search_ears_cb.get()
    search_grade = search_grade_cb.get()
    search_location = search_loc_cb.get()

    if search_size != 'All':  # Convert search_size to integer
        search_size = int(search_size)
    if search_connector != 'All':  # Convert search_connector to integer
        search_connector = int(search_connector)
    if search_ears != 'All':  # Convert search_ears to integer
        search_ears = int(search_ears)

    search = [search_brand, search_model, search_size, search_resolution, search_connector, search_touch, search_ears,
              search_grade, search_location]
    # search = [search_brand, search_model, int(search_size), search_resolution, int(search_connector), search_touch, int(search_ears), search_grade, search_location]
    # search = ['LG', 'B140BH2', 14, '1366x768', 30, 'No', 4, 'B', 'M1']
    # search = ['All', 'All', 'All', 'All', 'All', 'All', 'All', 'All', 'All']

    count = 0
    tv.delete(*tv.get_children())  # Erase the treeview
    for record in records:

        if search[0] == record[0] or search[0] == 'All':  # Check Brand
            if search[1] == record[1] or search[1] == 'All':  # Check Model
                if search[2] == record[2] or search[2] == 'All':  # Check Size
                    if search[3] == record[3] or search[3] == 'All':  # Check Resolution
                        if search[4] == record[4] or search[4] == 'All':  # Check Connector
                            if search[5] == record[5] or search[5] == 'All':  # Check Touch
                                if search[6] == record[6] or search[6] == 'All':  # Check Ears
                                    if search[7] == record[7] or search[7] == 'All':  # Check Grade
                                        if search[8] == record[8] or search[8] == 'All':  # Check Location

                                            if count % 2 == 0:
                                                tv.insert('', 'end', values=record,
                                                          tags=('oddrow',))  # insert odds only
                                            else:
                                                tv.insert('', 'end', values=record,
                                                          tags=('evenrow',))  # insert evens only
                                            count += 1
    # records = [] #Empty the memory


# Search window
############################################################################


# Label Screens Database
tk.Label(frm_TM, text='Screens Database', fg='blue', font=("Arial", 20)).pack()
frm_tv = tk.Frame(frm_TM)  # frame for Treeview
frm_tv.pack()

# Scrollbar
scroll = tk.Scrollbar(frm_tv)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

# Treeview display the results

area = ('Brand', 'Model', 'Size', 'Resolution', 'Connector', 'Touch', 'Ears', 'Grade', 'Loc', 'ID')

ac = ('all', 'n', 'e', 's', 'ne', 'nw', 'sw', 'c', 'r', 'g')

tv = ttk.Treeview(frm_tv, columns=ac, show='headings', height=9, yscrollcommand=scroll.set)
for i in range(10):
    tv.column(ac[i], width=70, anchor='c', stretch=tk.NO)
    tv.heading(ac[i], text=area[i])
tv.pack()

style.configure('Treeview', background='#D3D3D3', foreground='black', rowheight=27, fieldbackground='white')
style.map('Treeview', background=[('selected', 'blue')])

tv.tag_configure('oddrow', background='white')
tv.tag_configure('evenrow', background='#EBF5FB')

# Config scrollbar
scroll.config(command=tv.yview)


def reset_all():
    search_brand_cb.set('All')
    search_ent_model.delete(0, 'end')
    search_ent_model.insert(0, 'All')
    search_size_cb.set('All')
    search_res_cb.set('All')
    search_conn_cb.set('All')
    search_touch_cb.set('All')
    search_ears_cb.set('All')
    search_grade_cb.set('All')
    search_loc_cb.set('All')


# Search interface

# Brand
lbl_brand = tk.Label(frm_TL, text='Brand')
lbl_brand.grid(row=0, column=0)
brand_data = ['All', 'Mix', 'LG', 'Samsung', 'Sharp', 'IVO']
search_brand_cb = Combobox(frm_TL, values=brand_data, width=9)
# search_brand_cb.set('All')
search_brand_cb.current(0)
search_brand_cb.grid(row=0, column=1)

# Model
lbl_model = tk.Label(master=frm_TL, text='Model')
lbl_model.grid(row=1, column=0, padx=5, pady=5)
search_ent_model = tk.Entry(master=frm_TL, width=12)
search_ent_model.insert(0, 'All')
search_ent_model.grid(row=1, column=1, padx=5, )

# Size
lbl_size = tk.Label(frm_TL, text='Size')
lbl_size.grid(row=2, column=0)
size_data = ['All', 12, 13, 14, 15, 17]
search_size_cb = Combobox(frm_TL, values=size_data, width=9)
# search_size_cb.set('All')
search_size_cb.current(0)
search_size_cb.grid(row=2, column=1)

# Resolution
lbl_res = tk.Label(frm_TL, text='Resolution')
lbl_res.grid(row=3, column=0, padx=5, pady=5)
res_data = ['All', '1366x768', '1600x900', '1920x1080', '2560x1440', '3840x2160']
search_res_cb = Combobox(frm_TL, values=res_data, width=9)
# search_res_cb.set('All')
search_res_cb.current(0)
search_res_cb.grid(row=3, column=1, padx=5, pady=5)

# Connection
lbl_conn = tk.Label(frm_TL, text='Connector')
lbl_conn.grid(row=4, column=0)
conn_data = ['All', 30, 40]
search_conn_cb = Combobox(frm_TL, values=conn_data, width=9)
# search_conn_cb.set('All')
search_conn_cb.current(0)
search_conn_cb.grid(row=4, column=1)

# Touch
lbl_touch = tk.Label(frm_TL, text='Touch')
lbl_touch.grid(row=5, column=0, padx=5, pady=5)
touch_data = ['All', 'Yes', 'No']
search_touch_cb = Combobox(frm_TL, values=touch_data, width=9)
# search_touch_cb.set('All')
search_touch_cb.current(0)
search_touch_cb.grid(row=5, column=1, padx=5, pady=5)

# Ears   
lbl_ears = tk.Label(frm_TL, text='Ears')
lbl_ears.grid(row=6, column=0)
ears_data = ['All', '0', '2', '4']
search_ears_cb = Combobox(frm_TL, values=ears_data, width=9)
# search_ears_cb.set('All')
search_ears_cb.current(0)
search_ears_cb.grid(row=6, column=1)

# Grade
lbl_grade = tk.Label(frm_TL, text='Grade')
lbl_grade.grid(row=7, column=0, padx=5, pady=5)
grade_data = ['All', 'A', 'B', 'C']
search_grade_cb = Combobox(frm_TL, values=grade_data, width=9)
# search_grade_cb.set('All')
search_grade_cb.current(0)
search_grade_cb.grid(row=7, column=1, padx=5, pady=5)

# Location    
lbl_loc = tk.Label(frm_TL, text='Location')
lbl_loc.grid(row=8, column=0)
loc_data = ['All', 'S1', 'S2', 'S3', 'M1', 'M2', 'M3', 'L1', 'L2', 'L3']
search_loc_cb = Combobox(frm_TL, values=loc_data, width=9)
# search_loc_cb.set('All')
search_loc_cb.current(0)
search_loc_cb.grid(row=8, column=1)

search_btn = tk.Button(frm_TL, text='Search', font=("Arial Bold", 10), command=query)
search_btn.grid(row=9, column=1, sticky='ew', padx=5, pady=5)

reset_btn = tk.Button(frm_TL, text='Reset all', font=("Arial Bold", 10), command=reset_all)
reset_btn.grid(row=9, column=0, sticky='ew', padx=5, pady=10)

about_btn = tk.Button(frm_TM, text='About')
about_btn.pack(anchor='e')

query()  # Pre search (fill window with all records on start)


# Action Window
#############################################################

# Opperations

# fill up preset settings
def preset():
    brand_cb.set('Mix')
    # ent_model.insert(0, 'All')
    size_cb.set(14)
    res_cb.set('Select')
    conn_cb.set(30)
    touch_cb.set('No')
    ears_cb.set(4)
    grade_cb.set('C')


# Reset all settings
def reset():
    brand_cb.set('Select')
    ent_model.delete(0, tk.END)
    # ent_model.insert(0, '')
    size_cb.set('Select')
    res_cb.set('Select')
    conn_cb.set('Select')
    touch_cb.set('Select')
    ears_cb.set('Select')
    grade_cb.set('Select')
    loc_cb.set('Select')


# Enable Add Record widgets and buttons
def enable_add_widgets():
    brand_cb.config(state=tk.NORMAL)
    ent_model.config(state=tk.NORMAL)
    size_cb.config(state=tk.NORMAL)
    res_cb.config(state=tk.NORMAL)
    conn_cb.config(state=tk.NORMAL)
    touch_cb.config(state=tk.NORMAL)
    ears_cb.config(state=tk.NORMAL)
    grade_cb.config(state=tk.NORMAL)
    loc_cb.config(state=tk.NORMAL)

    preset_back_btn.config(state=tk.NORMAL)
    submit_save_delete_btn.config(state=tk.NORMAL)
    reset_btn.config(state=tk.NORMAL)

    show_record_btn.config(state=tk.NORMAL)
    delete_btn.config(state=tk.NORMAL)
    edit_btn.config(state=tk.NORMAL)
    add_btn.config(state=tk.NORMAL)


# Dissable Add Record widgets
def disable_add_widgets():
    brand_cb.config(state=tk.DISABLED)
    ent_model.config(state=tk.DISABLED)
    size_cb.config(state=tk.DISABLED)
    res_cb.config(state=tk.DISABLED)
    conn_cb.config(state=tk.DISABLED)
    touch_cb.config(state=tk.DISABLED)
    ears_cb.config(state=tk.DISABLED)
    grade_cb.config(state=tk.DISABLED)
    loc_cb.config(state=tk.DISABLED)


def fill():
    try:
        # Create or connect to database
        conn = sqlite3.connect('Screens_DB.db')
        # Create cursor
        cursor = conn.cursor()
        cursor.execute('SELECT * from screens WHERE oid = ' + id_ent.get())
        record = cursor.fetchall()

        enable_add_widgets()

        brand_cb.set(record[0][0])
        ent_model.delete(0, tk.END)
        ent_model.insert(0, record[0][1])
        size_cb.set(record[0][2])
        res_cb.set(record[0][3])
        conn_cb.set(record[0][4])
        touch_cb.set(record[0][5])
        ears_cb.set(record[0][6])
        grade_cb.set(record[0][7])
        loc_cb.set(record[0][8])

        disable_add_widgets()

        # Commit changes
        conn.commit()

        # Close connection
        conn.close()


    except Exception as e:
        messagebox.showwarning("Warning", e)
        add_rec()


def del_action():
    try:

        # Create or connect to database
        conn = sqlite3.connect('Screens_DB.db')
        # Create cursor
        cursor = conn.cursor()
        cursor.execute('DELETE from screens WHERE oid = ' + id_ent.get())  # Delete record

        # Commit changes
        conn.commit()
        # Close connection
        conn.close()


    except Exception as e:
        messagebox.showwarning("Warning", e)
        # add_rec()


# Show Record Actions
def show_rec():
    fill()
    disable_add_widgets()
    preset_back_btn.config(state=tk.DISABLED)
    submit_save_delete_btn.config(state=tk.DISABLED)
    reset_btn.config(state=tk.DISABLED)
    lbl_header.config(text='  Record ' + id_ent.get())
    del_txt = 'Record\n' + id_ent.get() + '\ndeleted'
    label_message.config(text=del_txt, fg='red')


# Delete a record
def delete():
    lbl_header.config(text='Delete Record ' + id_ent.get())
    fill()  # Fill up delete cells
    lbl_header.config(text='Delete Record ' + id_ent.get())

    preset_back_btn.config(state=tk.DISABLED)
    reset_btn.config(state=tk.DISABLED)
    submit_save_delete_btn.config(state=tk.NORMAL)

    submit_save_delete_btn.config(text='Delete', command=del_action)

    show_record_btn.config(state=tk.DISABLED)
    delete_btn.config(state=tk.DISABLED)
    edit_btn.config(state=tk.DISABLED)
    add_btn.config(state=tk.DISABLED)

    id_ent.delete(0, tk.END)  # Clear ID box after delete is done

    # OK button
    btn_ok_message = tk.Button(frm_action_L, text='OK', command=lambda: [add_rec(), btn_ok_message.destroy(),
                                                                         show_record_btn.config(state=tk.NORMAL),
                                                                         delete_btn.config(state=tk.NORMAL),
                                                                         edit_btn.config(state=tk.NORMAL),
                                                                         add_btn.config(
                                                                             state=tk.NORMAL)])  # Many command commands
    btn_ok_message.grid(row=7, column=3)

    # Erase the treeview after deleting
    tv.delete(*tv.get_children())


def add_rec():
    # global preset_btn, reset_btn, submit_btn
    id_ent.delete(0, tk.END)
    reset()

    label_message.config(text='')  # Erase label message

    # edit_add_btn.config(text = 'Edit Record', fg = 'blue', command = edit_rec)

    preset_back_btn.config(text='Preset', command=preset)
    submit_save_delete_btn.config(text='Submit', command=submit)

    lbl_header.config(text='  Add Record', fg='green')

    enable_add_widgets()
    preset_back_btn.config(state=tk.NORMAL)
    submit_save_delete_btn.config(state=tk.NORMAL)
    reset_btn.config(state=tk.NORMAL)

    query()  # Refresh records after new record was added


def save_edit():
    try:
        # Create or connect to database
        conn = sqlite3.connect('Screens_DB.db')
        # Create cursor
        cursor = conn.cursor()

        entry_values = {
            'brand': brand_cb.get(),
            'model': (ent_model.get()).upper(),
            'size': int(size_cb.get()),
            'resolution': res_cb.get(),
            'connector': int(conn_cb.get()),
            'touch': touch_cb.get(),
            'ears': int(ears_cb.get()),
            'grade': grade_cb.get(),
            'location': loc_cb.get(),
            'oid': int(id_ent.get())
        }

        cursor.execute('''UPDATE screens SET
                brand = :brand,
                model = :model,
                size = :size,
                resolution = :resolution,
                connector = :connector,
                touch = :touch,
                ears = :ears,
                grade = :grade,
                location = :location

                WHERE oid = :oid''', entry_values)

        # Commit changes
        conn.commit()
        # Close connection
        conn.close()

        query()  # Refresh records after new record was edited (updated)
        add_rec()

    except Exception as e:
        ret = messagebox.showwarning("Warning", e)
        add_rec()


def edit_rec():
    show_rec()

    lbl_header.config(text='  Edit Record ' + id_ent.get(), fg='blue')
    enable_add_widgets()

    preset_back_btn.config(state=tk.DISABLED)
    submit_save_delete_btn.config(state=tk.NORMAL)
    reset_btn.config(state=tk.DISABLED)
    submit_save_delete_btn.config(text='Update', command=save_edit)


# Create submit fuction
def submit():
    # Check if all enties are fill in
    values = [brand_cb.get(), size_cb.get(), res_cb.get(), conn_cb.get(), touch_cb.get(), ears_cb.get(), ears_cb.get(),
              grade_cb.get(), loc_cb.get()]
    if 'Select' in values:
        label_message.config(text='Fill in\nall\nentries', fg='red')  # Message Label config
        return
    # Check if model entry is empty
    model_space = ent_model.get()
    if not model_space.strip():
        label_message.config(text='Fill in\nModel\nentry', fg='red')  # Message Label config
        return

    # Create or connect to database
    conn = sqlite3.connect('Screens_DB.db')
    # Create cursor
    cursor = conn.cursor()
    # Insert into Table

    entry_values = {
        'brand': brand_cb.get(),
        'model': (ent_model.get()).upper(),
        'size': int(size_cb.get()),
        'resolution': res_cb.get(),
        'connector': int(conn_cb.get()),
        'touch': touch_cb.get(),
        'ears': int(ears_cb.get()),
        'grade': grade_cb.get(),
        'location': loc_cb.get()
    }

    cursor.execute(
        "INSERT INTO screens VALUES (:brand, :model, :size, :resolution, :connector, :touch, :ears, :grade, :location)",
        entry_values)

    # global last_added_record, btn_done_message
    last_added_record = cursor.lastrowid  # obtain last added record
    print(last_added_record)  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    label_text = 'Label the\n screen with:\n\n ID - ' + str(last_added_record) + '\n Loc. - ' + str(
        loc_cb.get())  # Mark label message

    label_message.config(text=label_text)  # Message Label config

    disable_add_widgets()  # Disable add widgets
    preset_back_btn.config(state=tk.DISABLED)
    submit_save_delete_btn.config(state=tk.DISABLED)
    reset_btn.config(state=tk.DISABLED)

    show_record_btn.config(state=tk.DISABLED)
    delete_btn.config(state=tk.DISABLED)
    edit_btn.config(state=tk.DISABLED)
    add_btn.config(state=tk.DISABLED)

    # DONE button
    btn_done_message = tk.Button(frm_action_L, text='Done', command=lambda: [enable_add_widgets,
                                                                             label_message.config(text=''),
                                                                             btn_done_message.destroy(),
                                                                             enable_add_widgets()])

    btn_done_message.grid(row=7, column=3)

    preset_back_btn.focus_set()  # Set focus on preset button after submitting record
    # Commit changes
    conn.commit()
    # Close connection
    conn.close()

    reset()  # Resset all enties after

    ##    label_text = 'Last added\n screen:\n\nID - ' + str(last_added_record) + '\n Loc - ' + str(loc_cb.get()) # Last record message
    ##    label_message.config(text = label_text, fg = 'green') # Message Last Label config
    ##    btn_done_message.destroy() # Remove "Done" button
    query()  # Refresh records after new record was added


# Base Window ##################################################################################


# Base heater Label
lbl_header = tk.Label(frm_action_R, text='', font=("Arial Bold", 15), width=14)
lbl_header.grid(row=0, column=0, columnspan=3)

# Brand
lbl_brand = tk.Label(frm_action_R, text='Brand')
lbl_brand.grid(row=1, column=0)
brand_data = ['Mix', 'LG', 'Samsung', 'Sharp', 'IVO']
brand_cb = Combobox(frm_action_R, values=brand_data, width=9)
brand_cb.set('Select')
brand_cb.grid(row=1, column=1)

# Model
lbl_model = tk.Label(frm_action_R, text='Model')
lbl_model.grid(row=2, column=0)
ent_model = tk.Entry(frm_action_R, width=12)
ent_model.grid(row=2, column=1, padx=5, pady=5)

# Size
lbl_size = tk.Label(frm_action_R, text='Size')
lbl_size.grid(row=3, column=0)
size_data = [12, 13, 14, 15, 17]
size_cb = Combobox(frm_action_R, values=size_data, width=9)
size_cb.set('Select')
size_cb.grid(row=3, column=1)

# Resolution
lbl_res = tk.Label(frm_action_R, text='Resolution')
lbl_res.grid(row=4, column=0)
res_data = ['1366x768', '1600x900', '1920x1080', '2560x1440', '3840x2160']
res_cb = Combobox(frm_action_R, values=res_data, width=9)
res_cb.set('Select')
res_cb.grid(row=4, column=1, padx=5, pady=5)

# Connection
lbl_conn = tk.Label(frm_action_R, text='Connector')
lbl_conn.grid(row=5, column=0)
conn_data = [30, 40]
conn_cb = Combobox(frm_action_R, values=conn_data, width=9)
conn_cb.set('Select')
conn_cb.grid(row=5, column=1)

# Touch
lbl_touch = tk.Label(frm_action_R, text='Touch')
lbl_touch.grid(row=6, column=0)
touch_data = ['Yes', 'No']
touch_cb = Combobox(frm_action_R, values=touch_data, width=9)
touch_cb.set('Select')
touch_cb.grid(row=6, column=1, padx=5, pady=5)

# Ears   
lbl_ears = tk.Label(frm_action_R, text='Ears')
lbl_ears.grid(row=7, column=0)
ears_data = [0, 2, 4]
ears_cb = Combobox(frm_action_R, values=ears_data, width=9)
ears_cb.set('Select')
ears_cb.grid(row=7, column=1)

# Grade
lbl_grade = tk.Label(frm_action_R, text='Grade')
lbl_grade.grid(row=8, column=0)
grade_data = ['A', 'B', 'C']
grade_cb = Combobox(frm_action_R, values=grade_data, width=9)
grade_cb.set('Select')
grade_cb.grid(row=8, column=1, padx=5, pady=5)

# Location    
lbl_loc = tk.Label(frm_action_R, text='Location')
lbl_loc.grid(row=9, column=0)
loc_data = ['S1', 'S2', 'S3', 'M1', 'M2', 'M3', 'L1', 'L2', 'L3']
loc_cb = Combobox(frm_action_R, values=loc_data, width=9)
loc_cb.set('Select')
loc_cb.grid(row=9, column=1)

# Header Label
lbl_header = tk.Label(frm_action_R, text='  Add Record:', font=("Arial Bold", 15))
lbl_header.grid(row=0, column=0, columnspan=3)

preset_back_btn = tk.Button(frm_action_R, text='Preset', font=("Arial Bold", 10), fg='blue', command=preset, width=5)
preset_back_btn.grid(row=10, column=0, padx=5)

submit_save_delete_btn = tk.Button(frm_action_R, text='Submit', font=("Arial Bold", 10), fg='blue', command=submit,
                                   width=8)
submit_save_delete_btn.grid(row=10, column=1, padx=5, pady=5)

reset_btn = tk.Button(frm_action_R, text='Reset', font=("Arial Bold", 10), command=reset, fg='blue', width=5)
reset_btn.grid(row=10, column=2, padx=5)

id_lbl = tk.Label(frm_action_L, text='Rec ID:')
id_lbl.grid(row=0, column=0)

id_ent = tk.Entry(frm_action_L, width=5)
id_ent.grid(row=0, column=1)

show_record_btn = tk.Button(frm_action_L, text='Show Record', font=("Arial Bold", 10), fg='blue', command=show_rec)
show_record_btn.grid(row=2, column=0, sticky='ew', padx=5, pady=5, columnspan=2)

delete_btn = tk.Button(frm_action_L, text='Delete Record', font=("Arial Bold", 10), fg='blue', command=delete)
delete_btn.grid(row=3, column=0, sticky='ew', padx=5, pady=5, columnspan=2)

edit_btn = tk.Button(frm_action_L, text='Edit Record', font=("Arial Bold", 10), fg='blue', command=edit_rec)
edit_btn.grid(row=4, column=0, sticky='ew', padx=5, pady=5, columnspan=2)

add_btn = tk.Button(frm_action_L, text='Add Record', font=("Arial Bold", 10), fg='blue', command=add_rec)
add_btn.grid(row=5, column=0, sticky='ew', padx=5, pady=5, columnspan=2)

# Message Label
label_message = tk.Label(frm_action_L, text=' ', fg='red', font=("Arial Bold", 15), borderwidth=2, relief="groove",
                         width=10, height=6)
# label_message  = tk.Label(frm_action_R, text = ' ', fg = 'red', font=("Arial Bold", 15),  borderwidth=6, relief="ridge", width = 10, height = 6)
label_message.grid(row=1, column=3, rowspan=6, padx=15, pady=5)

# Show Record Label
##lbl_show = tk.Label(frm_action_L, text = ' ',  borderwidth=2, relief="groove", width = 45)
##lbl_show.grid(row=2, column=2, padx = 10)

add_rec()

# window.after(3000, lambda: window.geometry('400x600'))


window.mainloop()

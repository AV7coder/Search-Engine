from tkinter import Button, Frame, simpledialog, messagebox , Tk, Label
import wikipedia
import pyautogui
# imports
root = Tk()
root.geometry('450x200')
root.title("Searchito")
root.configure(bg="black")
def search_btn_function():
    query = simpledialog.askstring("Search", "Enter your search: ")
    result = wikipedia.summary(query, sentences=100)
    try:
        # window = Tk()
        # window.geometry('1300x750')
        # window.title(f"Searchito-{query}")
        # window.configure(bg="lightpink")
        # title = Label(
        #             window,
        #             text=result,
        #             bg="lightpink",
        #             fg="red",
        #             font="algerian 12 bold",
        #             )
        # title.config(width=1300,)
        # title.pack()
        pyautogui.alert(result)
    except:
        messagebox.showinfo("No results available.")
search_btn_frame = Frame(root, bg="hotpink")
search_btn = Button(search_btn_frame,
                 text="Search",
                 height=3,
                 cursor="hand2",
                 bg="lightblue",
                 fg="blue",
                 font="algerian 68 bold italic",
                 command=search_btn_function)
search_btn.pack(fill="both")
search_btn_frame.pack(fill="both", pady=10)

while 1:
    root.mainloop()
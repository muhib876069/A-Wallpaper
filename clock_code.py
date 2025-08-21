import tkinter as tk
import time
from datetime import datetime

def update_clock():
    now = datetime.now()
    
    
    current_time = {
        "day": now.day,
        "month": now.month,
        "year": now.year,
        "dayOfWeek": now.strftime("%A"),
        "hour": now.hour,
        "minute": now.minute,
        "second": now.second,
    }
    
    
    total_seconds = 24 * 60 * 60
    elapsed_seconds = (now.hour * 3600) + (now.minute * 60) + now.second
    day_progress = (elapsed_seconds / total_seconds) * 100
    
    
    time_text = f"{current_time['hour']:02d}:{current_time['minute']:02d}:{current_time['second']:02d}"
    date_text = f"{current_time['dayOfWeek']}, {current_time['day']}/{current_time['month']:02d}/{current_time['year']}"
    progress_text = f"dayProgress: {day_progress:.2f}%"
    
    
    time_label.config(text=time_text)
    date_label.config(text=date_text)
    progress_label.config(text=progress_text)
    
    
    root.after(1000, update_clock)

# Prime window
root = tk.Tk()
root.title("Live Code Style Clock")
root.configure(bg="#1e1e1e") 
root.attributes("-fullscreen", True) 

# display colors and font colors
time_color = "#dcdcaa"  
date_color = "#9cdcfe"  
progress_color = "#ce9178"  
background = "#1e1e1e"  

# font
time_font = ("Consolas", 80, "bold")
date_font = ("Consolas", 30)
progress_font = ("Consolas", 25)

# Time display
time_label = tk.Label(
    root, 
    font=time_font, 
    fg=time_color, 
    bg=background,
    justify="center"
)
time_label.pack(pady=100)

# Date display
date_label = tk.Label(
    root, 
    font=date_font, 
    fg=date_color, 
    bg=background
)
date_label.pack(pady=20)

# Text
progress_label = tk.Label(
    root, 
    font=progress_font, 
    fg=progress_color, 
    bg=background
)
progress_label.pack(pady=50)

# display frame
json_frame = tk.Frame(root, bg=background)
json_frame.pack(pady=30)

# Display
json_text = tk.Label(
    json_frame,
    font=("Consolas", 18),
    fg="#D43054",  
    bg=background,
    justify="left",
    anchor="w"
)
json_text.pack()

def update_json_display():
    now = datetime.now()
    day_progress = (now.hour * 3600 + now.minute * 60 + now.second) / 86400 * 100

    
    display_text = (
        "const currentTime = {\n"
        f"    day: {now.day}\n" 
        f"    month: {now.month:02d},\n"
        f"    year: {now.year},\n"
        f"    dayOfWeek: \"{now.strftime('%A')}\",\n"
        f"    hour: {now.hour},\n"
        f"    minute: {now.minute},\n"
        f"    second: {now.second},\n"
        f"    dayProgress: {day_progress:.2f}%\n"
        "};"
    )
    json_text.config(text=display_text)
    root.after(1000, update_json_display)

# closing button
close_btn = tk.Button(
    root,
    text="X",
    font=("Consolas", 20),
    command=root.destroy,
    bg="#c0370d",
    fg="white",
    bd=0,
    padx=15,
    pady=5
)
close_btn.place(relx=0.95, rely=0.02, anchor="ne")

# starting clock
update_clock()
update_json_display()

root.mainloop()
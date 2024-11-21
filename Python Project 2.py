import tkinter as tk
import datetime
import time
import threading
import pygame

# Initialize Pygame for sound
pygame.mixer.init()

# Load the alarm sound
pygame.mixer.music.load("alarm_sound.mp3.wav")  # Replace with your sound file

# List to store past alarms
past_alarms = []


def set_alarm():
    alarm_time = entry.get()
    if alarm_time:
        past_alarms.append(alarm_time)  # Store the alarm time in past alarms
        while True:
            current_time = datetime.datetime.now().strftime("%H:%M")
            if current_time == alarm_time:
                label.config(text="Alarm ringing!")
                pygame.mixer.music.play(-1)  # Play the sound indefinitely
                break
            time.sleep(60)


def start_alarm_thread():
    thread = threading.Thread(target=set_alarm)
    thread.start()


def stop_alarm():
    pygame.mixer.music.stop()
    label.config(text="")


def show_past_alarms():
    past_alarms_window = tk.Toplevel(root)
    past_alarms_window.title("Past Alarms")

    # Create a label for past alarms
    label = tk.Label(past_alarms_window, text="Past Alarms:")
    label.pack(pady=10)

    # Create a listbox to display past alarms
    listbox = tk.Listbox(past_alarms_window)
    for alarm in past_alarms:
        listbox.insert(tk.END, alarm)
    listbox.pack(pady=10)

    # Add a button to close the past alarms window
    close_button = tk.Button(past_alarms_window, text="Close", command=past_alarms_window.destroy)
    close_button.pack(pady=10)


# Create the main window
root = tk.Tk()
root.title("Alarm Clock")

# Create a menu
menu = tk.Menu(root)
root.config(menu=menu)

# Add a "File" menu with an option to view past alarms
file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="View Past Alarms", command=show_past_alarms)

# Create and place the widgets
label = tk.Label(root, text="Enter alarm time (HH:MM):")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

set_button = tk.Button(root, text="Set Alarm", command=start_alarm_thread)
set_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop Alarm", command=stop_alarm)
stop_button.pack(pady=10)

# Run the application
root.mainloop()
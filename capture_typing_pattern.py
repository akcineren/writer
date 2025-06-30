from pynput import keyboard
import time
import json
import statistics

print("Type your sentence. Press Enter when done.")

intervals = []
last_time = None
sentence = ''

# Flag to stop listener
done = False

def on_press(key):
    global last_time, intervals, sentence, done
    try:
        if key.char:
            current_time = time.time()
            if last_time is not None:
                interval = (current_time - last_time) * 1000  # ms
                intervals.append(interval)
            last_time = current_time
            sentence += key.char
    except AttributeError:
        # Handle special keys
        if key == keyboard.Key.enter:
            done = True
            # Stop listener
            return False

with keyboard.Listener(on_press=on_press) as listener:
    while not done:
        time.sleep(0.01)

if intervals:
    mean_interval = statistics.mean(intervals)
    std_interval = statistics.stdev(intervals) if len(intervals) > 1 else 0.0
    print(f"Mean interval: {mean_interval:.2f} ms")
    print(f"Std deviation: {std_interval:.2f} ms")
    with open('typing_intervals.json', 'w') as f:
        json.dump({'intervals': intervals, 'mean': mean_interval, 'std': std_interval}, f)
else:
    print("Not enough data captured.") 
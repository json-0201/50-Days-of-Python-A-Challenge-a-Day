# Spelling Checker

def spelling_checker():
    """A simple implementation of a spelling checker using textblob module."""
    from textblob import TextBlob

    while True:
        word = input("Enter the word: ")

        if TextBlob(word).correct() == word.lower():
            return word
        else:
            ans = input(f"Did you mean to type \"{TextBlob(word).correct()}\"?: ")
            if ans.lower() in ["yes", "y"]:
                break
            else:
                continue

    return TextBlob(word).correct()

print(spelling_checker())


# Extra Challenge: Create an Alarm Clock

def alarm():
    """A simulation of an alarm clock."""
    from datetime import datetime
    import winsound, re

    exp = "\d\d:\d\d"

    while True:
        time_alarm = input("Set time for alarm, (HH:MM): ")
        if re.search(exp, time_alarm):
            print(f"Your alarm is set for {time_alarm}")
            break
        else:
            print("Enter a valid time! ex.(15:30)")
        
    while True:
        time_current = datetime.now().strftime("%H:%M")
        if time_alarm == time_current:
            winsound.Beep(500, 4000) # 500Hz, 4000milliseconds
            break

    return

alarm()

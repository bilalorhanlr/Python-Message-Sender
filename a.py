import pyautogui as pt
import time

# Kullanıcıdan mesaj sayısını ve mesaj içeriğini al
limit = int(input("Enter the limit (number of messages): "))
message = input("Enter the message to send: ")

# Kullanıcıya hazırlanması için 10 saniye ver
print("You have 10 seconds to focus on the message input area...")
time.sleep(10)

# Mesajları gönderme döngüsü
for i in range(limit):
    pt.typewrite(message)  # Mesajı yaz
    pt.press("enter")      # Enter tuşuna basarak mesajı gönder
    time.sleep(0.5)        # Mesajlar arasında 0.5 saniye bekle (isteğe bağlı)
    
print(f"{limit} messages sent successfully!")
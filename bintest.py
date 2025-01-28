while True:
  print("Do you want to translate from English to Binary (Enter: '1') or Binary to English? (Enter: '2')")
  option = int(input("Enter Here:"))

  if option == 1:
    print("Please enter your message in English that you want translated to Binary.")
    EtoB = input()
    binary = " ".join(format(ord(c), "b") for c in EtoB)
    print("Your Message in Binary is: ", binary)
    print("\n")


  if option == 2:
    print("Please enter your message in Binary that you want translated to English.")
    BtoE = input()
    binary_text = BtoE
    normal = " ".join(chr(int(c, 2)) for c in binary_text.split(" "))
    print("Your Message in English is: ", normal)
    print("\n")

import CTkMessagebox as CTkMessagebox
import PIL.Image
import customtkinter

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.message = "\n\n"
        self.casear_encrypted_text = ""
        self.casear_decrypted_text = ""
        self.play_encrypted_text = ""
        self.play_decrypted_text = ""

        self.list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm',
                      'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.title("Cipher Desktop GUI App by ARA")
        self.geometry(f"{1252}x{750}")

        self.grid_columnconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)

        self.background_label = customtkinter.CTkLabel(self, text="", fg_color="transparent")
        self.background_label.grid(row=0, column=0, sticky="nsew", padx=(0, 30))
        self.background_label.grid_rowconfigure(2, weight=1)
        self.background_label.configure(bg_color="transparent")

        image = PIL.Image.open("bg.jpg")
        bg_image = customtkinter.CTkImage(image, size=(1252, 750))
        self.background_label.configure(image=bg_image, compound="center", fg_color="transparent")
        self.background_label.grid_columnconfigure(0, weight=0)
        self.background_label.grid_rowconfigure((0, 1, 2, 3), weight=1)

        self.sidebar_frame = customtkinter.CTkFrame(self.background_label, width=500, corner_radius=60,
                                                    fg_color="#FFFFFF")
        self.sidebar_frame.configure(bg_color="#FFFFFF")
        self.sidebar_frame.grid(row=0, column=0, sticky="esnw", padx=(0, 750), pady=(0, 0))
        self.sidebar_frame.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.optionmenu_1 = customtkinter.CTkOptionMenu(self.sidebar_frame, dynamic_resizing=False, width=275,
                                                        height=50, values=["Casear", "Playfair", "Monoalphapetic"],
                                                        text_color="#324E9F", fg_color="#F2F5FA",
                                                        button_hover_color="#6C8BB7", dropdown_hover_color="#6C8BB7",
                                                        dropdown_fg_color="#F2F5FA", dropdown_text_color="#324E9F",
                                                        button_color="#87A2CF", )
        self.optionmenu_1.grid(row=0, column=0, padx=50, pady=60, sticky="esnw")
        self.optionmenu_1.place(relx=0.5, rely=0.2, anchor="center")
        self.optionmenu_2 = customtkinter.CTkOptionMenu(self.sidebar_frame, dynamic_resizing=False, width=275,
                                                        height=50, values=["Encrypt", "Decrypt", ],
                                                        text_color="#324E9F", fg_color="#F2F5FA",
                                                        button_hover_color="#6C8BB7", dropdown_hover_color="#6C8BB7",
                                                        dropdown_fg_color="#F2F5FA", dropdown_text_color="#324E9F",
                                                        button_color="#87A2CF", )
        self.optionmenu_2.grid(row=0, column=0, padx=50, pady=60, sticky="esnw")
        self.optionmenu_2.place(relx=0.5, rely=0.3, anchor="center")
        self.plain_text_entry = customtkinter.CTkEntry(self.sidebar_frame, width=275, height=50,
                                                       placeholder_text="Enter plain text",
                                                       placeholder_text_color="#87A2CF", text_color="#324E9F",
                                                       fg_color="#F2F5FA", border_color="#87A2CF")
        self.plain_text_entry.grid(row=0, column=0, padx=50, pady=60, sticky="esnw")
        self.plain_text_entry.place(relx=0.5, rely=0.4, anchor="center")
        self.plain_text_entry2 = customtkinter.CTkEntry(self.sidebar_frame, width=275, height=50,
                                                        placeholder_text="Enter shift key",
                                                        placeholder_text_color="#87A2CF", text_color="#324E9F",
                                                        fg_color="#F2F5FA", border_color="#87A2CF")
        self.plain_text_entry2.grid(row=1, column=0, padx=50, pady=60, sticky="esnw")
        self.plain_text_entry2.place(relx=0.5, rely=0.5, anchor="center")

        self.plain_text_entry3 = customtkinter.CTkEntry(self.sidebar_frame, width=275, height=50,
                                                        placeholder_text="Enter playfair key",
                                                        placeholder_text_color="#87A2CF", text_color="#324E9F",
                                                        fg_color="#F2F5FA", border_color="#87A2CF")
        self.plain_text_entry3.grid(row=2, column=0, padx=50, pady=60, sticky="esnw")
        self.plain_text_entry3.place(relx=0.5, rely=0.6, anchor="center")

        self.cipher_button = customtkinter.CTkButton(self.sidebar_frame, width=250, corner_radius=60,
                                                     fg_color="#87A2CF", hover_color="#6C8BB7", height=40,
                                                     text="Do operation", command=self.get_in,
                                                     bg_color="#FFFFFF")
        self.cipher_button.grid(row=3, column=0, padx=10, pady=10, sticky="esnw")
        self.cipher_button.place(relx=0.5, rely=0.7, anchor="center")
        self.cipher_button2 = customtkinter.CTkButton(self.sidebar_frame, width=250, corner_radius=60,
                                                      fg_color="#87A2CF", hover_color="#6C8BB7", height=40,
                                                      text="Clear History", command=self.clear,
                                                      bg_color="#FFFFFF")
        self.cipher_button2.grid(row=3, column=0, padx=10, pady=10, sticky="esnw")
        self.cipher_button2.place(relx=0.5, rely=0.8, anchor="center")

    #########################################################################################################################################################################################################################################################
    def clear(self):
        self.message = "\n\n"
        self.casear_encrypted_text = ""
        self.casear_decrypted_text = ""
        self.play_encrypted_text = ""
        self.play_decrypted_text = ""

    def caesar_encrypt(self, plain_text, shift):
        self.casear_encrypted_text = ""
        if shift > 26:
            shift %= 26
        for char in plain_text:
            if char.isalpha():
                shifted = ord(char) + shift
                if char.islower():
                    if shifted > ord('z'):
                        shifted -= 26
                    elif shifted < ord('a'):
                        shifted += 26
                elif char.isupper():
                    if shifted > ord('Z'):
                        shifted -= 26
                    elif shifted < ord('A'):
                        shifted += 26
                self.casear_encrypted_text += chr(shifted)
            else:
                self.casear_encrypted_text += char
        self.message += plain_text.upper() + " is encrypted to -> " + self.casear_encrypted_text.upper() + "\n\n"

    def caesar_decrypt(self, plain_text, shift):

        self.casear_decrypted_text = ""
        sh = -shift

        for char in plain_text:
            if char.isalpha():
                shifted = ord(char) + sh
                if char.islower():
                    if shifted > ord('z'):
                        shifted -= 26
                    elif shifted < ord('a'):
                        shifted += 26
                elif char.isupper():
                    if shifted > ord('Z'):
                        shifted -= 26
                    elif shifted < ord('A'):
                        shifted += 26
                self.casear_decrypted_text += chr(shifted)
            else:
                self.casear_decrypted_text += char
        self.message += plain_text.upper() + " is decrypted to -> " + self.casear_decrypted_text.upper() + "\n\n"

    #########################################################################################################################################################################################################################################################

    def toLowerCase(self, text):
        return text.lower()

    def removeSpaces(self, text):
        return ''.join(text.split())

    ###################################################################################
    def generateKeyTable(self, key):
        # generates the 5x5 key square
        keyT = [['' for i in range(5)] for j in range(5)]
        dicty = {chr(i + 97): 0 for i in range(26)}

        for i in range(len(key)):
            if key[i] != 'j':
                dicty[key[i]] = 2
        dicty['j'] = 1

        i, j, k = 0, 0, 0
        while k < len(key):
            if dicty[key[k]] == 2:
                dicty[key[k]] -= 1
                keyT[i][j] = key[k]
                j += 1
                if j == 5:
                    i += 1
                    j = 0
            k += 1

        for k in dicty.keys():
            if dicty[k] == 0:
                keyT[i][j] = k
                j += 1
                if j == 5:
                    i += 1
                    j = 0

        return keyT

    def search(self, keyT, a, b):
        # Search for the characters of a digraph in the key square and return their position
        arr = [0, 0, 0, 0]

        if a == 'j':
            a = 'i'
        elif b == 'j':
            b = 'i'

        for i in range(5):
            for j in range(5):
                if keyT[i][j] == a:
                    arr[0], arr[1] = i, j
                elif keyT[i][j] == b:
                    arr[2], arr[3] = i, j

        return arr

    def mod5(self, a):
        # Function to find the modulus with 5
        if a < 0:
            a += 5
        return a % 5

    def decrypt_playfair(self, str, keyT):
        self.play_decrypted_text = ""
        str1 = str
        ps = len(str)
        i = 0
        while i < ps:
            a = self.search(keyT, str[i], str[i + 1])
            if a[0] == a[2]:
                str = str[:i] + keyT[a[0]
                ][self.mod5(a[1] - 1)] + keyT[a[0]][self.mod5(a[3] - 1)] + str[i + 2:]
            elif a[1] == a[3]:
                str = str[:i] + keyT[self.mod5(a[0] - 1)][a[1]] + \
                      keyT[self.mod5(a[2] - 1)][a[1]] + str[i + 2:]
            else:
                str = str[:i] + keyT[a[0]][a[3]] + keyT[a[2]][a[1]] + str[i + 2:]
            i += 2

        return str

    def decryptByPlayfairCipher(self, str, key):
        ks = len(key)
        key = self.removeSpaces(self.toLowerCase(key))
        str = self.removeSpaces(self.toLowerCase(str))
        keyT = self.generateKeyTable(key)
        return self.decrypt_playfair(str, keyT)

    def Diagraph(self, text):
        Diagraph = []
        group = 0
        for i in range(2, len(text), 2):
            Diagraph.append(text[group:i])

            group = i
        Diagraph.append(text[group:])
        return Diagraph

    ###################################################################################

    def FillerLetter(self, text):
        k = len(text)
        if k % 2 == 0:
            for i in range(0, k, 2):
                if text[i] == text[i + 1]:
                    new_word = text[0:i + 1] + str('x') + text[i + 1:]
                    new_word = self.FillerLetter(new_word)
                    break
                else:
                    new_word = text
        else:
            for i in range(0, k - 1, 2):
                if text[i] == text[i + 1]:
                    new_word = text[0:i + 1] + str('x') + text[i + 1:]
                    new_word = self.FillerLetter(new_word)
                    break
                else:
                    new_word = text
        return new_word

    def generateKeyTable1(self, word, list1):
        key_letters = []
        for i in word:
            if i not in key_letters:
                key_letters.append(i)

        compElements = []
        for i in key_letters:
            if i not in compElements:
                compElements.append(i)
        for i in list1:
            if i not in compElements:
                compElements.append(i)

        matrix = []
        while compElements != []:
            matrix.append(compElements[:5])
            compElements = compElements[5:]
        return matrix

    def search1(self, mat, element):
        for i in range(5):
            for j in range(5):
                if (mat[i][j] == element):
                    return i, j

    def encrypt_RowRule(self, matr, e1r, e1c, e2r, e2c):
        char1 = ''
        if e1c == 4:
            char1 = matr[e1r][0]
        else:
            char1 = matr[e1r][e1c + 1]

        char2 = ''
        if e2c == 4:
            char2 = matr[e2r][0]
        else:
            char2 = matr[e2r][e2c + 1]

        return char1, char2

    def encrypt_ColumnRule(self, matr, e1r, e1c, e2r, e2c):
        char1 = ''
        if e1r == 4:
            char1 = matr[0][e1c]
        else:
            char1 = matr[e1r + 1][e1c]

        char2 = ''
        if e2r == 4:
            char2 = matr[0][e2c]
        else:
            char2 = matr[e2r + 1][e2c]

        return char1, char2

    def encrypt_RectangleRule(self, matr, e1r, e1c, e2r, e2c):
        char1 = ''
        char1 = matr[e1r][e2c]

        char2 = ''
        char2 = matr[e2r][e1c]

        return char1, char2

    def encryptByPlayfairCipher(self, Matrix, plainList):
        CipherText = []
        for i in range(0, len(plainList)):
            c1 = 0
            c2 = 0
            ele1_x, ele1_y = self.search1(Matrix, plainList[i][0])
            ele2_x, ele2_y = self.search1(Matrix, plainList[i][1])

            if ele1_x == ele2_x:
                c1, c2 = self.encrypt_RowRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
            # Get 2 letter cipherText
            elif ele1_y == ele2_y:
                c1, c2 = self.encrypt_ColumnRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
            else:
                c1, c2 = self.encrypt_RectangleRule(
                    Matrix, ele1_x, ele1_y, ele2_x, ele2_y)

            cipher = c1 + c2
            CipherText.append(cipher)
        return CipherText

    def playfair(self, plain_text, key_in):
        self.play_encrypted_text = ""
        self.play_decrypted_text = ""
        text_Plain = plain_text
        text_Plain = self.removeSpaces(self.toLowerCase(plain_text))
        PlainTextList = self.Diagraph(self.FillerLetter(text_Plain))
        if len(PlainTextList[-1]) != 2:
            PlainTextList[-1] = PlainTextList[-1] + 'z'

        key = key_in
        key = self.toLowerCase(key)
        Matrix = self.generateKeyTable1(key, self.list1)

        CipherList = self.encryptByPlayfairCipher(Matrix, PlainTextList)

        CipherText = ""
        for i in CipherList:
            CipherText += i
        self.play_encrypted_text = CipherText
        decreypted_text = self.decryptByPlayfairCipher(plain_text, key)
        self.play_decrypted_text = decreypted_text

        if self.optionmenu_2.get() == "Encrypt":
            self.message += plain_text.upper() + " is encrypted to -> " + self.play_encrypted_text.upper() + "\n\n"
        elif self.optionmenu_2.get() == "Decrypt":
            self.message += plain_text.upper() + " is decrypted to -> " + self.play_decrypted_text.upper() + "\n\n"

    #########################################################################################################################################################################################################################################################
    def mono_encryption(self, plain_text):
        normal_char = list('abcdefghijklmnopqrstuvwxyz')
        coded_char = list('QWERTYUIOPASDFGHJKLZXCVBNM')
        plain_text = plain_text.lower()
        encrypted_text = ""

        for char in plain_text:
            if char.isalpha() and char.islower():
                index = normal_char.index(char)
                encrypted_text += coded_char[index]
            elif char.isalpha() and char.isupper():
                index = normal_char.index(char.lower())
                encrypted_text += coded_char[index].upper()
            else:
                encrypted_text += char
        self.message += plain_text.upper() + " is encrypted to -> " + encrypted_text.upper() + "\n\n"

        return encrypted_text

    def mono_decryption(self, plain_text):
        normal_char = list('abcdefghijklmnopqrstuvwxyz')
        coded_char = list('QWERTYUIOPASDFGHJKLZXCVBNM')

        decrypted_text = ""
        plain_text=plain_text.upper()

        for char in plain_text:
            if char.isalpha() and char.islower():
                index = coded_char.index(char)
                decrypted_text += normal_char[index]
            elif char.isalpha() and char.isupper():
                index = coded_char.index(char.upper())
                decrypted_text += normal_char[index].upper()
            else:
                decrypted_text += char
        self.message += plain_text+ " is decrypted to -> " +decrypted_text.upper() + "\n\n"

        return decrypted_text


    #########################################################################################################################################################################################################################################################
    def show_checkmark(self):
        # Use the function from the imported module
        CTkMessagebox.CTkMessagebox(
            message=self.message,
            icon="check",
            title="Successfully ciphered",
            title_color="#324E9F",
            option_1="Thanks",
            fg_color="#F2F5FA",
            bg_color="#A6BED8",
            width=450,
            height=150,
            button_color="#6C8BB7",
            text_color="#324E9F",
            button_hover_color="#324E9F",
            button_width=100,
            button_height=25,
            cancel_button="circle",
            cancel_button_color="#324E9F",
            fade_in_duration=10,
            sound=True,
            icon_size=(30, 30)
        )
    def error(self, error):
        CTkMessagebox.CTkMessagebox(
            title="Error",
            title_color="#324E9F",
            message=error + "!!!",
            icon="cancel",
            fg_color="#F2F5FA",
            bg_color="#A6BED8",
            width=300,
            height=120,
            button_color="#6C8BB7",
            text_color="#324E9F",
            button_hover_color="#324E9F",
            button_width=100,
            button_height=25,
            cancel_button="circle",
            cancel_button_color="#324E9F",
            fade_in_duration=10,
            sound=True,
            icon_size=(30, 30)
        )

    def error_dig(self):
        CTkMessagebox.CTkMessagebox(
            title="Error",
            title_color="#324E9F",
            message="Shift should be a number" + "!!!",
            icon="cancel",
            fg_color="#F2F5FA",
            bg_color="#A6BED8",
            width=300,
            height=120,
            button_color="#6C8BB7",
            text_color="#324E9F",
            button_hover_color="#324E9F",
            button_width=100,
            button_height=25,
            cancel_button="circle",
            cancel_button_color="#324E9F",
            fade_in_duration=10,
            sound=True,
            icon_size=(30, 30)
        )

    def error_letter(self, txt):
        CTkMessagebox.CTkMessagebox(
            title="Error",
            title_color="#324E9F",
            message=txt + " should contain only letters (A...Z) or (a...z)" + "!!!",
            icon="cancel",
            fg_color="#F2F5FA",
            bg_color="#A6BED8",
            width=300,
            height=120,
            button_color="#6C8BB7",
            text_color="#324E9F",
            button_hover_color="#324E9F",
            button_width=100,
            button_height=25,
            cancel_button="circle",
            cancel_button_color="#324E9F",
            fade_in_duration=10,
            sound=True,
            icon_size=(30, 30)
        )

    def get_in(self):
        s1 = self.optionmenu_1.get()
        s2 = self.optionmenu_2.get()
        plain_text = self.plain_text_entry.get()
        shift = self.plain_text_entry2.get()
        key = self.plain_text_entry3.get()
        error = ""
        if s1 == "Casear":
            if plain_text == "" and shift == "":
                error += "Plain text and shift are empty"
            elif shift == "":
                error += "Shift is empty"
            elif plain_text == "":
                error += "Plain text is empty"

            if plain_text != "" and shift != "":
                if shift.isdigit():  # Check if shift contains only digits
                    if plain_text.isalpha():  # Check if plain_text and key are only alphabetic
                        shift = int(shift)
                        if (s2 == "Encrypt"):
                            self.caesar_encrypt(plain_text, shift)
                            self.show_checkmark()
                        else:
                            self.caesar_decrypt(plain_text, shift)
                            self.show_checkmark()
                    else:
                        self.error_letter("Plain text")
                else:
                    self.error_dig()
            else:
                self.error(error)
        elif s1 == "Playfair":
            if plain_text == "" and key == "":
                error += "Plain text and key are empty"
            elif key == "":
                error += "key is empty"
            elif plain_text == "":
                error += "Plain text is empty"

            if plain_text != "" and key != "":
                if plain_text.isalpha() and key.isalpha():  # Check if plain_text and key are only alphabetic
                    if (s2 == "Encrypt"):
                        self.playfair(plain_text, key)
                        self.show_checkmark()
                    else:
                        self.playfair(plain_text, key)
                        self.show_checkmark()
                else:
                    self.error_letter("Plain text and key")

            else:
                self.error(error)
        elif s1=="Monoalphapetic":
            if plain_text == "":
                error += "Plain text is empty"
            if plain_text != "" :
                if plain_text.isalpha():  # Check if plain_text and key are only alphabetic
                    if (s2 == "Encrypt"):
                        self.mono_encryption(plain_text)
                        self.show_checkmark()
                    else:
                        self.mono_decryption(plain_text)
                        self.show_checkmark()
                else:
                    self.error_letter("Plain text ")
            else: self.error(error)

if __name__ == "__main__":
    app = App()
    app.mainloop()

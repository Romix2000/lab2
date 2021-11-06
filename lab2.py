ABC=input("введіть:")

test_input=str(input("введіть: ")) 

if ABC == 'A':
  
  def compressed (word):
    letter_dict = {}
    for letter in test_input:
      if letter not in letter_dict:
        letter_dict[letter] = 1
      else:
        letter_dict[letter] = letter_dict[letter]+1
    return letter_dict

  print(compressed(test_input))







elif ABC =='B':

    def split(word):
        return [char for char in word]


    def percentage(part, whole):
     percentage = 100 * float(part) // float(whole)
     return str(percentage) + "%"


    a = 0;b = 0; c = 0;d = 0;e = 0;f = 0;g = 0;h = 0;i = 0;j = 0;k = 0;l = 0;m = 0;n = 0;o = 0;p = 0;q = 0;r = 0;s = 0
    t = 0;u = 0; v = 0;w = 0;x = 0;y = 0;z = 0



    list = (split(test_input))
    lenght = len(test_input)

    for character in range(lenght):
        if list[character] == ' ':
            lenght = lenght - 1
        if list[character] == 'a' or list[character] == 'A':
            a = a + 1
        elif list[character] == 'b' or list[character] == 'B':
            b = b + 1
        elif list[character] == 'c' or list[character] == 'C':
            c = c + 1
        elif list[character] == 'd' or list[character] == 'D':
            d = d + 1
        elif list[character] == 'e' or list[character] == 'E':
            e = e + 1
        elif list[character] == 'f' or list[character] == 'F':
            f = f + 1
        elif list[character] == 'g' or list[character] == 'G':
            g = g + 1
        elif list[character] == 'h' or list[character] == 'H':
            h = h + 1
        elif list[character] == 'i' or list[character] == 'I':
            i = i + 1
        elif list[character] == 'j' or list[character] == 'J':
            j = j + 1
        elif list[character] == 'k' or list[character] == 'K':
            k = k + 1
        elif list[character] == 'l' or list[character] == 'L':
            l = l + 1
        elif list[character] == 'm' or list[character] == 'M':
            m = m + 1
        elif list[character] == 'n' or list[character] == 'N':
            n = n + 1
        elif list[character] == 'o' or list[character] == 'O':
            o = o + 1
        elif list[character] == 'p' or list[character] == 'P':
            p = p + 1
        elif list[character] == 'q' or list[character] == 'Q':
            q = q + 1
        elif list[character] == 'r' or list[character] == 'R':
            r = r + 1
        elif list[character] == 's' or list[character] == 'S':
            s = s + 1
        elif list[character] == 't' or list[character] == 'T':
            t = t + 1
        elif list[character] == 'u' or list[character] == 'U':
            u = u + 1
        elif list[character] == 'v' or list[character] == 'V':
            v = v + 1
        elif list[character] == 'w' or list[character] == 'W':
            w = w + 1
        elif list[character] == 'x' or list[character] == 'X':
            x = x + 1
        elif list[character] == 'y' or list[character] == 'Y':
            y = y + 1
        elif list[character] == 'z' or list[character] == 'Z':
            z = z + 1


    print(percentage(a, lenght), " - відсоток букв А в реченні")
    print(percentage(b, lenght), " - відсоток букв B в реченні")
    print(percentage(c, lenght), " - відсоток букв C в реченні")
    print(percentage(d, lenght), " - відсоток букв D в реченні")
    print(percentage(e, lenght), " - відсоток букв E в реченні")
    print(percentage(f, lenght), " - відсоток букв F в реченні")
    print(percentage(g, lenght), " - відсоток букв G в реченні")
    print(percentage(h, lenght), " - відсоток букв H в реченні")
    print(percentage(i, lenght), " - відсоток букв I в реченні")
    print(percentage(j, lenght), " - відсоток букв J в реченні")
    print(percentage(k, lenght), " - відсоток букв K в реченні")
    print(percentage(l, lenght), " - відсоток букв L в реченні")
    print(percentage(m, lenght), " - відсоток букв M в реченні")
    print(percentage(n, lenght), " - відсоток букв N в реченні")
    print(percentage(o, lenght), " - відсоток букв O в реченні")
    print(percentage(p, lenght), " - відсоток букв P в реченні")
    print(percentage(q, lenght), " - відсоток букв Q в реченні")
    print(percentage(r, lenght), " - відсоток букв R в реченні")
    print(percentage(s, lenght), " - відсоток букв S в реченні")
    print(percentage(t, lenght), " - відсоток букв T в реченні")
    print(percentage(u, lenght), " - відсоток букв U в реченні")
    print(percentage(v, lenght), " - відсоток букв V в реченні")
    print(percentage(w, lenght), " - відсоток букв W в реченні")
    print(percentage(x, lenght), " - відсоток букв X в реченні")
    print(percentage(y, lenght), " - відсоток букв Y в реченні")
    print(percentage(z, lenght), " - відсоток букв Z в реченні")

  

else:
 
    test_input = test_input.replace(',', ' ')
    test_input = test_input.split()
    test_input.sort()
    print(test_input)
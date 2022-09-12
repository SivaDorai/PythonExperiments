import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def rotationalCipher(input_str, rotation_factor):
  # Write your code here
  response  =  ""

  for i in list(input_str):
    if i.isalpha():
      print(ascii(chr(ord(i)+rotation_factor)))
      if rotation_factor > 26:
        rf = rotation_factor%26
      if str(i).isupper():
        i = chr(ord(i) - rf)
      else:
        if ord(i)+rf> 122:
          i = chr(ord(i)+rf-26)
        else:
          i = chr(ord(i) + rf)
      response += str(i)
    elif i.isdigit():
      if rotation_factor>9:
        rf =rotation_factor% 10
      j = str(int(i) + rf)
      if int(j)>9:
        j = j[0]
      response = response + str(i)
    else:
      i = i
      response += str(i)


  return response

print(rotationalCipher("abcdZXYzxy-999.@",200))
print(39%10)
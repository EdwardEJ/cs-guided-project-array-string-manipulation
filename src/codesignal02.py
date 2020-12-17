def alphabeticShift(inputString: str) -> str:
    shiftedAlphabet = ''
    for i in inputString:
      if i == 'z':
        shiftedAlphabet += 'a'
      else:
        shiftedAlphabet += chr(ord(i) + 1)
    return shiftedAlphabet

print(alphabeticShift("crazy"))
import base64

def obfuscator():
    file = input("file:\n")
    print("mode 1: base64 encoded code gets decoded while running\n"
          "mode 2:code gets base64 encoded in string and decoded while running !!code is plain text!!"
          "\nmode 3: code is 2 times base64 encoded, one time it gets decoded in the string, one time while executing")
    mode = input(">>")
    with open(file) as f:
        code = f.read()
    if mode == "1":
        code_bytes = code.encode()
        base64_bytes = base64.b64encode(code_bytes)
        b64_code = base64_bytes.decode()
        b64_code = b64_code.replace('"""', "'''")
        obf_code = 'import base64\ncode = (b"""' + b64_code + '""")\nexec(base64.b64decode(code))'

        with open(f"obfuscated-{file}", 'w') as f:
            f.write(obf_code)
            print(obf_code)

    elif mode == "2":
        obf_code = 'import base64\ncode = base64.b64encode(b"""' + code + '""")\nexec(base64.b64decode(code))'

        with open(f"obfuscated-{file}", 'w') as f:
            f.write(obf_code)
            print(obf_code)
    elif mode == "3":
        code_bytes = code.encode()
        base64_bytes = base64.b64encode(code_bytes)
        base64_bytes2 = base64.b64encode(base64_bytes)
        b64_code = base64_bytes2.decode()
        b64_code = b64_code.replace('"""', "'''")
        obf_code = 'import base64\ncode = base64.b64decode(b"""' + b64_code + '""")\nexec(base64.b64decode(code))'

        with open(f"obfuscated-{file}", 'w') as f:
            f.write(obf_code)
            print(obf_code)

    elif mode == "4":
        code_bytes = code.encode()
        base64_bytes = base64.b64encode(code_bytes)
        b64_code = base64_bytes.decode()
        b64_code = b64_code.replace('"""', "'''")
        b64_code = b64_code.replace("m", "#hoafhoiawgfzoaw#")
        b64_code = b64_code.replace("b", "#zagflwibgaizwfglajfblaw#")
        obf_code = 'import base64\ncode = (b"""' + b64_code + '""")\nexec(base64.b64decode(code.replace(b"#hoafhoiawgfzoaw#", b"m").replace(b"#zagflwibgaizwfglajfblaw#", b"b")))'

        with open(f"obfuscated-{file}", 'w') as f:
            f.write(obf_code)
            print(obf_code)
    elif mode == "5":
        loop_obf = int(input("how many times should it get obfuscated?"))
        code_bytes = code.encode()
        base64_bytes = base64.b64encode(code_bytes)
        b64_code = base64_bytes.decode()
        b64_code = b64_code.replace('"""', "'''")
        b64_code = b64_code.replace("m", "#hoafhoiawgfzoaw#")
        b64_code = b64_code.replace("b", "#zagflwibgaizwfglajfblaw#")
        obf_code = 'import base64\ncode = (b"""' + b64_code + '""")\nexec(base64.b64decode(code.replace(b"#hoafhoiawgfzoaw#", b"m").replace(b"#zagflwibgaizwfglajfblaw#", b"b")))'
        for i in range(loop_obf - 1):
            code_bytes = obf_code.encode()
            base64_bytes = base64.b64encode(code_bytes)
            b64_code = base64_bytes.decode()
            b64_code = b64_code.replace('"""', "'''")
            b64_code = b64_code.replace("m", "#hoafhoiawgfzoaw#")
            b64_code = b64_code.replace("b", "#zagflwibgaizwfglajfblaw#")
            obf_code = 'import base64\ncode = (b"""' + b64_code + '""")\nexec(base64.b64decode(code.replace(b"#hoafhoiawgfzoaw#", b"m").replace(b"#zagflwibgaizwfglajfblaw#", b"b")))'

        with open(f"obfuscated-{file}", 'w') as f:
            f.write(obf_code)
            print(obf_code)
    else:
        print("Error")


if __name__ == "__main__":
    obfuscator()

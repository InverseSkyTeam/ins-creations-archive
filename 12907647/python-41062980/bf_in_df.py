let tape:list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
let position:int = 0
let i:int = 0
let x:int = 0
let command:str = inputln("输入BrainFuck语言语句:")
while i < length(command){
    if command[i] == "<"{
        if position > 0{
            position = position - 1
        }
    }elif command[i] == ">"{
        if position < length(tape){
            position = position + 1
        }
    }elif command[i] == "+"{
        if tape[position] < 255{
            tape[position] = tape[position] + 1
        }else{
            tape[position] = 0
        }
    }elif command[i] == "-"{
        if tape[position] > 0{
            tape[position] = tape[position] - 1
        }else{
            tape[position] = 255
        }
    }elif command[i] == ","{
        tape[position] = ord(inputln(""))
    }elif command[i] == "."{
        print(chr(tape[position]))
    }elif command[i] == "["{
        if tape[position] == 0{
            i = i + 1
            while command[i] != "]" or x != 0{
                if command[i] == "["{
                    x = x + 1
                }elif command[i] == "]"{
                    x = x - 1
                }
                if i != length(command){
                    i = i + 1
                }
            }
        }
    }elif command[i] == "]"{
        if tape[position] != 0{
            i = i - 1
            while command[i] != "[" or x != 0{
                if command[i] == "["{
                    x = x - 1
                }elif command[i] == "]"{
                    x = x + 1
                }
                if i != 0{
                    i = i - 1
                }
            }
        }
    }
    i = i + 1
}
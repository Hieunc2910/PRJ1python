# Cho văn bản T và 2 mẫu P1, P2 đều là các xâu ký tự (không chứa ký tự xuống dòng, độ dài không vượt quá 1000). Hãy thay thế các xâu P1 trong T bằng xâu P2.
# Dữ liệu
# · Dòng 1: xâu P1
# · Dòng 2: xâu P2
# · Dòng 3: văn bản T
# Kết quả:
# · Ghi văn bản T sau khi thay thế
# Ví dụ
# Dữ liệu
# AI
# Artificial Intelligence
# Recently, AI is a key technology. AI enable efficient operations in many fields.
# Kết quả
# Recently, Artificial Intelligence is a key technology. Artificial Intelligence enable efficient operations in many fields.
import sys
input_text = sys.stdin.read()
input_text = input_text.split("\n")
P1=input_text[0]
P2=input_text[1]
T=input_text[2:]
for i in range(len(T)):
    T[i]=T[i].replace(P1,P2)
    print(T[i])

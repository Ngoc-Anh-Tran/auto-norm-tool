#pip install requests
#pip install pandas
#pip install numpy

import requests
import pandas as pd
import numpy as np

#Định nghĩa các đường dẫn cần thiết
url = 'http://10.124.68.92:11993/norm'
file_input = 'data/input.txt'
file_output = "data/output.txt"

#Norm qua API servic
def test_norm_para(text):
    data = {"sample": text}
    norm = requests.post(url, json = data)
    text_output = norm.json().get("sample") #output trả về là mảng các câu
    result = " . ".join(text_output) #nên cần join lại thành đoạn, phân cách bằng kí tự " . "
    return  result
    
#Đọc file txt
#Thêm cột norm_text để chứa kết quả sau norm
df = pd.read_csv(file_input,delimiter = "\t", names = ["Id", "raw_text", "norm_text"])

#Norm tất cả text và lưu ở cột norm_text
df["norm_text"] = df["raw_text"].apply(test_norm_para)

#Lưu kết quả ra file txt mới
np.savetxt(file_output, df[["Id","norm_text"]], fmt='%s')

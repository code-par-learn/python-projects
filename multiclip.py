import sys
import clipboard
import json
repo="clipboard.json"
def save_items(filepath, data):
    with open(filepath,"w") as f:
        json.dump(data,f)
def load_data(filepath):
    try:
        with open(filepath,"r") as f:
            data=json.load(f)
            return data 
    except:
        return {}             
if len(sys.argv)==2:
    command=sys.argv[1]
    data=load_data(repo)
    if command=="save":
        key=input("Enter a key: ")
        data[key]=clipboard.paste()
        save_items(repo,data)
        print("Data Saved")
    elif command=="load":
        key=input("Enter a key: ")
        if key not in  data:
            print("invalid key")
        else:
            clipboard.copy(data[key])
            print("Data Loaded")
    elif command=="list":
        print(data)

    else:
        print("invalid command")      
else:
    print("pls pass exactly one command")              

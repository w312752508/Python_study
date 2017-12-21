import json,os,pickle
file = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
a = {"a":"k"}
# with open(r"%s\data\test" % file, "wb") as file_cl:
#     pickle.dump(a,file_cl)
with open(r"%s\data\test" % file, "rb") as file_cl:
    cl = pickle.load(file_cl)
print(cl)
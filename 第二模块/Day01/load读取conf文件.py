import configparser
conf = configparser.ConfigParser()
conf.read("example.ini")
# conf.remove_section("test")
conf.remove_option("test" , "hostname")
conf.set("test" , "port" , "2000")
conf.write(open("new_example.ini","w"))
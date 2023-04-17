def main():
    try:
        f =open("file1.txt","w")
        f.write("first file creation in python")
        print("file created and text written")
    except OSError:
        print("file not found")
    finally:
        f.close()    
main()
    
    
try: 
    f = open('file.txt')
    if f.name == 'file.txt':
        raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print('Error !')

else:
    print(f.read())
    f.close()

finally:
    print("executed finally")
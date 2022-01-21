import easyocr
from save_thread_result import ThreadWithResult
from shutil import rmtree,copyfileobj
from os import path,listdir,unlink,makedirs


def recognizer(file)->str:
    folder = 'uploads'
    thread = ThreadWithResult(target=create_txt,args=(file.filename,folder,))
    thread.start()
    clean_dir(folder=folder)

    img_path = path.join(folder,file.filename)
    with open(img_path, 'wb') as buffer:
        copyfileobj(file.file,buffer)

    
    reader = easyocr.Reader(['en'],gpu=True)
    result = reader.readtext(img_path)

    text = ''
    for line in result:
        text += line[1]+'\n'
    thread.join()
    dict_obj = thread.result

    with open(dict_obj['path'],'a') as f:
        f.write(text)

    return dict_obj['path'],dict_obj['name']



def clean_dir(folder:str):
    
    try:
        for filename in listdir(folder):
            file_path = path.join(folder, filename)
            try:
                if path.isfile(file_path) or path.islink(file_path):
                    unlink(file_path)
                elif path.isdir(file_path):
                    rmtree(file_path)
            except Exception as e:
                print(e)
    except:
        makedirs(folder, exist_ok=False)

def create_txt(filename:str,save_dir:str)-> str:
    filename = filename.rsplit('.',1)[0]+'.txt'
    filepath = path.join(save_dir,filename)
    f = open(filepath,'w')
    f.close()
    return dict(path = filepath,name = filename)
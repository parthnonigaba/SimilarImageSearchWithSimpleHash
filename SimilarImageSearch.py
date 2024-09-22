from PIL import Image
import imagehash
import os

similarImages =[]

def getallfiles(sourcedir):
    """retruns Lists of all files in the specified directory."""
    my_list =[]
    for filename in os.listdir(sourcedir):
        filepath = os.path.join(sourcedir, filename)
        if filepath.startswith('.'):
            continue
        my_list.append(filepath)

    return my_list

sourcefolder='/Users/parthgaba/Downloads/p/'

sourceimage_list=getallfiles(sourcefolder)

destinationfolder='/Users/parthgaba/Desktop/Twitter/twitter_data/images 2/'

cutoff = 5  # maximum bits that could be different between the hashes. 



for sourceimage in sourceimage_list:
    print("......................................................")
    hash0 = imagehash.average_hash(Image.open(sourceimage)) 
    for destfile in getallfiles(destinationfolder):
        hash1 = imagehash.average_hash(Image.open(destfile)) 

        if hash0 - hash1 < cutoff:
            print('images are similar........'+destfile)
            similarImages.append(destfile)
        #else:
            #print('images are not similar')

    print(f"{len(similarImages)} images are found for {sourceimage} :")
    print(f"All similar images to {sourceimage} are following :")

    for similarimage in similarImages:
        print(similarimage)

    print("......................................................")
    

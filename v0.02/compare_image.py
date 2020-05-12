import CPGMS_Feature
import CPIMS_Feature
import CPORB_Feature
import CPdHash_Feature

if __name__ == '__main__':

    #img1_path = sys.argv[1]
    #img2_path = sys.argv[2]
    
    img1_path = "./data/12021.jpg"
    img2_path = "./data/12023.jpg"

    CPGMS = CPGMS_Feature.CPGMS(img1_path,img2_path)
    CPIMS = CPIMS_Feature.CPIMS(img1_path,img2_path)
    CPORB = CPORB_Feature.CPORB(img1_path,img2_path)
    CPdHash = CPdHash_Feature.CPdHash(img1_path,img2_path)

    print("=========================GMS MATCHING========================")
    print(CPGMS)
    print("=========================ORB MATCHING========================")
    print(CPORB)
    print("=========================IMS MATCHING========================")
    print(CPIMS)
    print("=========================dHash MATCHING========================")
    print("0                            31")
    #print(CPdHash)
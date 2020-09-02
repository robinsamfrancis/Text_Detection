import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('test image.jpg')

# tesseract reads the image only in rgb but opencv is in bgr so we convert the image to rgb

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#prints the text in the image
print(pytesseract.image_to_string(img))


#Detecting individual Characters
print(pytesseract.image_to_boxes(img))   #print the values a block in every character
hImg,wImg,_ = img.shape
boxes= (pytesseract.image_to_boxes(img)) #puts a box corresponding to every chara
for b in boxes.splitlines():
    print(b)
    b= b.split(' ')  #Changing the result to list ('') from the space
    print(b)
    x,y,w,h = int(b[1]), int(b[2]),int(b[3]), int(b[4])
    cv2.rectangle(img,(x,hImg-y),(w,hImg-h),(0,0,255,3)) # Setting the bounding boxes. The height and y values are subtracted to make the boxes fit
    cv2.putText(img,b[0],(x,hImg-y+25),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2) #B[0] BECOZ CHARACTER IS THE FIRST ELEMENT IN LIST


#Detecting words
hImg,wImg,_ = img.shape
boxes= (pytesseract.image_to_data(img))  #puts the boxes corresponding to every word
print(boxes)
for x,b in enumerate  (boxes.splitlines()):

    ### A lot of times when dealing with iterators (An iterator is an object that contains a countable number of values)
    ### we also get a need to keep a count of iterations. Python eases the programmers’ task by providing a built-in
    ### function enumerate() for this task.

    if x!=0:
        b = b.split()

    print(b)
    if len(b)== 12:#since  there are 12 values
        x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])  # 6,7,8,9 becoz we want only that
        cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,255,3))
        cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)



#Detecting Numbers
hImg,wImg,_ = img.shape
cong = r'--oem 3--psm 6 outputbase digits'
boxes= pytesseract.image_to_boxes(img, config= cong)
for b in boxes.splitlines():
    #print(b)
    b= b.split(' ')
    print(b)
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])  # 6,7,8,9 becoz we want only that
    cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,255,3))
    cv2.putText(img,b[0],(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)

cv2.imshow('result', img)
cv2.waitKey(0)

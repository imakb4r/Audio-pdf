import PyPDF2
from gtts import gTTS

#filelocation = askopenfilename()

# creating a pdf file object
pdfFileObj = open(f"C:/Users/Akba4/Downloads/Website-Terms-of-Use-39515.pdf", 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    
# printing number of pages in pdf file
print(pdfReader.numPages)

# creating a page object
pageObj = pdfReader.getPage(0)

# extracting text from page
String_text = pageObj.extractText()

# closing the pdf file object
pdfFileObj.close()

final_file = gTTS(text=String_text, lang="en")
final_file.save("Generated Speech.mp3")

print("Success!")

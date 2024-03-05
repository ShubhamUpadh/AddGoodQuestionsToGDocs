from AddQuestionsToOutputtxt import QuestionRev
from UploadDataToDrive import uploadData
print("exporting questions")
exportQuestions = QuestionRev()
exportQuestions.execute()
print("export finished")
print("uploading data to drive")
uploadQuestions = uploadData()
uploadQuestions.execute()
print("upload finished")
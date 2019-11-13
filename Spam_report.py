




def spam_report(emails_body):
     '''Generates the spam report '''

     virus_detected = False
     string_report = "Scanning in process ... \n"
     words = 'virus'  ################ list from RE
     i = 0
     # check for virus
     for email in emails_body:

          if words not in str(email[0]):
               virus_detected = False
          else:
               virus_detected = True
               string_report += "Message from: " + email[2]+ "\n"
               string_report += "Sent on:" + email[4]
               string_report +='\nVIRUS DETECTED ! \n'


               string_report += "**************************************************\n"


     return string_report



# Hospital-Queue-Screen
An application that can be used in hospitals for patients to track their queue to see the doctor they are appointed to.
In this directory I'm including .py files for the screens of the doctor, the patient, and the queue screen that is going to be displayed at the top of the doctor's office. The .ui files that are also included are the interfaces of the different windows just mentioned.
This project uses MySQL server algorithms to store and access data of patients. The patient can use the patient screen application to enter their information and the doctor will be able to see it on their screen.

## How to use:
- Run `hospitalQueuePatientScreen.py` for the patients to use
- The patient should enter the required information on the screen adn then press `GÖNDER`
- A doctor should run `hospitalQueueDoctorScreen.py` and enter the required information on the screen
- After the information has been filled, the doctor can press `SIRADAKİ HASTA` to view all of their patients waiting in line on the secondary monitor (if it's connected) automatically.
- Every time `SIRADAKİ HASTA` is clicked, new patients in the queue will come into the view of the screen
